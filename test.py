import json
import requests
from datetime import *

data = json.load(open('api/2.json', 'r'))
today = date.today()
            
def getTodayDate():

    date = []
    date.append(today.strftime("%m"))
    date.append(today.strftime("%m"))
    date.append(today.strftime("%y"))
    return date 

def is_a_closed_day(day,month) : 

    day = str(day)
    month = str(month)
    year = today.strftime("%Y")
    daymonth = month+"-"+day
    url = "https://calendrier.api.gouv.fr/jours-feries/metropole/"+year+".json"

    resp = requests.get(url=url)
    data = resp.json() 
    
    for key, value  in data.items() : 
        if daymonth in key : 
            _return = []
            _return.append("Le "+str(day)+"/"+month+"/"+year+" est un jour férié : "+value)   
            return _return
    

def getCelebrationFromDate(day,month): 
    
    original_day = day 
    day = day - 1 
    result = []
    
    if month <= 12 and day <= len(data["months"][str(month)]): 
        if original_day < 10 and int(month) < 10 : 
            result.append("Le 0"+str(original_day)+"/0"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
        elif original_day >= 10 and int(month) < 10 : 
            result.append("Le "+str(original_day)+"/0"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
        else : 
            result.append("Le "+str(original_day)+"/"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
        
        return result 
    
    else : 
        result.append("Out of range !")
        return result

def getCelebrationFromName(_name): 
    
    _name = _name.lower()
    result = []
    i = 0 
    for name in data['months'].items():
        if _name in name[1] : 
            list = name[1] # extract list from tuple() to use index() function
            month = name[0]
            day = list.index(_name) + 1 
            if day < 10 and int(month) < 10 : 
                result.append("La fête de "+_name+" est le 0"+str(day)+"/0"+str(month))
            elif day >= 10 and int(month) < 10 : 
                result.append("La fête de "+_name+" est le "+str(day)+"/0"+str(month))
            else : 
                result.append("La fête de "+_name+" est le "+str(day)+"/"+str(month))
            i = i + 1 
            
    if len(result) > 1 : 
        result.append(_name+" est fêté "+str(i)+" fois dans l'année.")
        
    return result

def today_celebration() : 
    
    date = getTodayDate()
    day = int(date[0])
    month = int(date[1])
    is_a_closed_day(day,month)
    # getCelebrationFromDate (day,month)

    # Check first, it doay is a clodes day. 
    # Otherwise, display the celebration name and date 

# print (today_celebration())
# print (is_a_closed_day("01","01"))


# print (getCelebrationFromDate(3,3))
# print (getCelebrationFromName("Benoit"))
