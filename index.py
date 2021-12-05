import requests
from datetime import date

from requests.sessions import get_netrc_auth

def getCelebrationFromDate(date): 
    url = "http://localhost/celebrationDays/celebrationFrenchDaysAPI.json"
    params = dict(
    )

    resp = requests.get(url=url, params=params)
    data = resp.json() 

    for item in data["celebration"]:
        if item["date"] == date:
            return "La fête de "+item["name"]+" est le "+item["date"]+""


def getCelebrationFromName(name):

    url = "http://localhost/celebrationDays/celebrationFrenchDaysAPI.json"
    params = dict(
    )

    resp = requests.get(url=url, params=params)
    data = resp.json() 

    for item in data["celebration"]:
        if item["name"] == name:
            return "La fête de "+item["name"]+" est le "+item["date"]+""

def getTodayCelebration():
    today = date.today()
    d = today.strftime("%d/%m")
    return d 

    return ""

print(getCelebrationFromName("Philippe"))
print(getCelebrationFromDate("02/05"))
#print(getCelebrationFromDate(getTodayCelebration()))
