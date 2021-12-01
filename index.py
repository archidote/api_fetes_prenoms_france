import requests

def getCelebrationFromDate(date): 
    url = "http://localhost/celebrationDays/celebrationFrenchDaysAPI.json"
    params = dict(
    )

    resp = requests.get(url=url, params=params)
    data = resp.json() 

    for item in data["celebration"]:
        if item["date"] == date:
            return "La fête de "+item["name"]+" est le "+item["date"]+""


def getName(name):

    url = "http://localhost/celebrationDays/celebrationFrenchDaysAPI.json"
    params = dict(
    )

    resp = requests.get(url=url, params=params)
    data = resp.json() 

    for item in data["celebration"]:
        if item["name"] == name:
            return "La fête de "+item["name"]+" est le "+item["date"]+""

print(getName("Véronique"))
print(getCelebrationFromDate("28/02"))
