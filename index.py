import json 
from datetime import date

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

print(getCelebrationFromName("Philippe"))
print(getCelebrationFromDate("02/05"))
#print(getCelebrationFromDate(getTodayCelebration()))
