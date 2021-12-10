import json 
import requests
from datetime import date
from collections import OrderedDict

data = json.load(open('celebrationFrenchDaysAPI.json', 'r'))

def getCelebrationFromDate(date): 

    for item in data["celebration"]:
        if item["date"] == date:
            return "La fête de "+item["name"]+" est le "+item["date"]+""


def getCelebrationFromName(name):

    for item in data["celebration"]:
        if item["name"] == name:
            return "La fête de "+item["name"]+" est le "+item["date"]+""

def getTodayCelebration():

    today = date.today()
    d = today.strftime("%d/%m")
    return d 

def getFrenchClosedDay() : 

    today = date.today()
    year = today.strftime("%Y")

    url = "https://calendrier.api.gouv.fr/jours-feries/metropole/"+year+".json"

    resp = requests.get(url=url)
    data = resp.json() 

    # TO-DO : try to reverse the order of the json array. 

    return data 
print(getCelebrationFromName("Philippe"))
print(getCelebrationFromDate("02/05"))
print(getFrenchClosedDay())
#print(getCelebrationFromDate(getTodayCelebration()))
