import json
import requests
from datetime import *

data = json.load(open('database/calendar.json', 'r'))
today = date.today()
    
def getTodayDate():

    date = []
    date.append(today.strftime("%d"))
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
        _return = []
        if daymonth in key : 
            _return.append(True)
            _return.append("Le "+str(day)+"/"+month+"/"+year+" est un jour férié : "+value)   
            return _return
        else : 
            _return.append(False)
            _return.append("Le "+str(day)+"/"+month+"/"+year+" n'est pas un jour férié.")   
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
    
    
def get_celebrations_from_month(month): 
    return data["months"][(str(month))]

def get_celebration_from_name(_name): 
    
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

def celebration(today_or_tomorrow) : 
    
    print (today_or_tomorrow)
    date = getTodayDate()
    day = int(date[0])
    month = int(date[1])
    
    _return = ""
    
    if today_or_tomorrow == 1 : 
        day = int(date[0]) + 1 
    
    closed_or_not = is_a_closed_day(day,month)
    
    if  closed_or_not[0] == True : 
        print (1)
        _return = closed_or_not[1]
    else : 
        print (2)
        _return =  closed_or_not[1] 
        
    return _return









# print (today_celebration())
# print (is_a_closed_day("01","01"))
# print (getCelebrationFromDate(3,3))
# print (get_celebration_from_name("Benoit"))
