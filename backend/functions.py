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


def fete_via_date(day,month): 
    
    result = []
    
    if month <= 12 and day <= len(data["months"][str(month)]): 
        if day < 10 and month < 10 : 
            print (day,month)
            result.append("Le 0"+str(day)+"/0"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
            day = "0"+str(day)
            month = "0"+str(month)
        elif day >= 10 and month < 10 : 
            result.append("Le "+str(day)+"/0"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
            month = "0"+str(month)
        else : 
            result.append("Le "+str(day)+"/"+str(month)+" nous fêtons : "+data["months"][str(month)][day]+"")
        
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
    
    result = [] 
    _name = _name.capitalize()
    i = 0 
    for month in data["months"].values():
        for names in month:
            if _name in names:
                indice = [i for i, s in enumerate(month) if _name in s]
                day = indice[0]
                _month = int(month[0])
                if day < 10 and _month < 10 :
                    result.append("La fête de "+_name+" est le 0"+str(day)+"/0"+str(_month))
                elif day >= 10 and _month < 10 : 
                    result.append("La fête de "+_name+" est le "+str(day)+"/0"+str(_month))
                else : 
                    result.append("La fête de "+_name+" est le "+str(day)+"/"+str(_month))
                i = i + 1 
    if len(result) > 1 : 
        result.append(_name+" est fêté "+str(i)+" fois dans l'année.")
        
    return result

                
def demain(): 
    demain = day + 1 
    print (demain,month)
    return fete_via_date(demain,month)

def hier() : 
    hier = day - 1 
    return fete_via_date(hier,month)

def aujourdhui() : 
    return fete_via_date(day,month) 

def toutes_les_fetes() : 
    return data