import json
import requests
from datetime import *

########################################## CORE DATA #########################################
data = json.load(open('database/calendrier.json', 'r'))
today = date.today()
    
def getTodayDate():

    date = []
    date.append(today.strftime("%d"))
    date.append(today.strftime("%m"))
    date.append(today.strftime("%y"))
    return date 

_date = getTodayDate()
day = int(_date[0])
month = int(_date[1])
year = int(_date[2])

########################################## </CORE DATA> #########################################

def est_ce_un_jour_ferie(day,month) : 
    
    day = str(day)
    month = str(month)
    year = today.strftime("%Y")
    daymonth = month+"-"+day
    url = "https://calendrier.api.gouv.fr/jours-feries/metropole/"+year+".json"

    resp = requests.get(url=url)
    data = resp.json() 
    
    _return = []
    for key, value  in data.items() : 
        if daymonth in key : 
            _return = "Le "+str(day)+"/"+month+"/"+year+" est un jour férié : "+value

    if len(_return) < 1 : 
        _return = "Le "+str(day)+"/"+month+"/"+year+" n'est pas un jour férié."
        
    return _return 


def getCelebrationFromDate(day,month): 
    
    original_day = day 
    day = day - 1 
    result = []
    
    if month <= 12 and day <= len(data["months"][str(month)]): 
        if original_day < 10 and month < 10 : 
            result.append("Le 0"+str(original_day)+"/0"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
            day = "0"+str(original_day)
            month = "0"+str(month)
        elif original_day >= 10 and month < 10 : 
            result.append("Le "+str(original_day)+"/0"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
            month = "0"+str(month)
        else : 
            result.append("Le "+str(original_day)+"/"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
        
        result.append(est_ce_un_jour_ferie(day,month))
        return result 
    
    else : 
        result.append("Le mois ou le jour renseigné n'est pas correct.")
        return result
    
    
def fetes_du_mois(month): 
    if month >= 1 and month <= 12 : 
        return data["months"][(str(month))]
    else : 
        return ["Mois inexistant ! ("+str(month)+")"]

def fete_via_nom(_name): 
    
    _name = _name.capitalize()
    print (_name)
    result = []
    i = 0 
    for name in data['months'].items():
        if _name in name[1] : 
            list = name[1] # extract list from tuple() to use index() function
            month = name[0]
            day = list.index(_name) + 1 
            if day < 10 and int(month) < 10 : 
                result.append("La fête de "+_name+" est le 0"+str(day)+"/0"+str(month))
                # result.append(est_ce_un_jour_ferie(day,month))
            elif day >= 10 and int(month) < 10 : 
                result.append("La fête de "+_name+" est le "+str(day)+"/0"+str(month))
                # result.append(est_ce_un_jour_ferie(day,month))
            else : 
                result.append("La fête de "+_name+" est le "+str(day)+"/"+str(month))
                # result.append(est_ce_un_jour_ferie(day,month))
            i = i + 1 
            
    if len(result) > 1 : 
        result.append(_name+" est fêté "+str(i)+" fois dans l'année.")
        
    return result

def demain(): 
    demain = day + 1 
    return getCelebrationFromDate(demain,month)

def hier() : 
    hier = day - 1 
    return getCelebrationFromDate(hier,month)

def aujourdhui() : 
    return getCelebrationFromDate(day,month) 

def toutes_les_fetes() : 
    return data

print (fete_via_nom("benoit"))