import json
import requests
from datetime import *

data = json.load(open('api/2.json', 'r'))
            
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

def getCelebrationFromDate(month,day): 
    day = day - 1 
    if month <= 12 and day <= len(data["months"][str(month)]): 
        print (data["months"][str(month)][day])
    else : 
        return "Out of range !"

def getCelebrationFromName(n): 
    for name in data['months'].items():
        if n in name[1] : 
            list = name[1] # extract list from tuple() to use index() function
            month = name[0]
            day = list.index(n) + 1 
            print ("La fête de "+n+" est le "+str(day)+"/"+str(month))
            # print pour afficher les fêtes multiple et return pour afficher les fêtes unique 
            return ""
print (getCelebrationFromDate(1,3))
print (getCelebrationFromName("Philippe"))
