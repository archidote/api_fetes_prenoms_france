import json
import requests
from datetime import *

data = json.load(open('api/celebrationFrenchDaysAPI.json', 'r'))

def getCelebrationFromDate(date): 
    x = ""
    for item in data["celebrations"]:
        if item["date"] == date:
            x = 1
            print ("La fête de "+item["name"]+" est le "+item["date"]+"")
    if x == "": 
        return "Votre date : "+date+" n'est pas conforme"
    else : 
        return ""
    
    # Ok, tested 


def getCelebrationFromName(name):
    x = "" 
    for item in data["celebrations"]:
        if name in item["name"] :
            x = 1
            print ("La fête de "+item["name"]+" est le "+item["date"]+"")
    if x == "": 
        return "Aucune fête n'est associé au prénom : "+name
    else : 
        return ""

    # OK, tested 

def getTodayDate():

    today = date.today()
    d = today.strftime("%d/%m")
    return d 

def isTodayAClosedDay() : 

    today = date.today()
    d = today.strftime("%Y/%m/%d")   
    year = today.strftime("%Y")

    url = "https://calendrier.api.gouv.fr/jours-feries/metropole/"+year+".json"

    resp = requests.get(url=url)
    data = resp.json() 

    for dateAttribut in data:        
        if d in data :
            return "Jour férié"
        else : 
            return ""

def getFrenchClosedDay() : 

    today = date.today()
    year = today.strftime("%Y")

    url = "https://calendrier.api.gouv.fr/jours-feries/metropole/"+year+".json"

    resp = requests.get(url=url)
    data = resp.json() 

    for key in data:
        print(data[key]+" : "+key+"")
    return ""



print(getCelebrationFromName("Antoine"))
print(getCelebrationFromName("Philippe"))
print(getCelebrationFromName("dsf"))
print(getCelebrationFromDate("01/02"))
print(getCelebrationFromDate("30/02"))
print(getFrenchClosedDay())
print(isTodayAClosedDay())
print(isTodayAClosedDay())
#print("Aujourd'hui nous fêtons les : "+getCelebrationFromDate(getTodayDate()))
