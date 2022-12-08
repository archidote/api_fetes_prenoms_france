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
    original_day = day 
    day = day - 1 
    result = []
    if month <= 12 and day <= len(data["months"][str(month)]): 
        result.append("Le "+str(original_day)+"/"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
        return result 
    else : 
        return "Out of range !"

def getCelebrationFromName(_name): 
    _name = _name.lower()
    result = []
    for name in data['months'].items():
        if _name in name[1] : 
            list = name[1] # extract list from tuple() to use index() function
            month = name[0]
            day = list.index(_name) + 1 
            result.append("La fête de "+_name+" est le "+str(day)+"/"+str(month))
    return result

print (getCelebrationFromDate(3,3))
print (getCelebrationFromName("Benoit"))
