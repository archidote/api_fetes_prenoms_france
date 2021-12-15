import json 
import requests
from datetime import date
from collections import OrderedDict

data = json.load(open('api/celebrationFrenchDaysAPI.json', 'r'))

def getCelebrationFromDate(date): 

    for item in data["celebrations"]:
        if item["date"] == date:
            return "La fête de "+item["name"]+" est le "+item["date"]+""


def getCelebrationFromName(name):

    for item in data["celebrations"]:
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

    for key in data:
        print(data[key]+" : "+key+"")

    # TO DO : get the day from the date 

print(getCelebrationFromName("Philippe"))
print(getCelebrationFromDate("02/05"))
print(getFrenchClosedDay())
#print(getCelebrationFromDate(getTodayCelebration()))
