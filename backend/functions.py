import json
import unicodedata
from datetime import *

########################################## <Données communes> #########################################

CALENDRIER = json.load(open('database/calendrier.json', 'r'))

AUJOURDHUI = date.today()
    
def date_du_jour():

    date = []
    date.append(AUJOURDHUI.strftime("%d"))
    date.append(AUJOURDHUI.strftime("%m"))
    date.append(AUJOURDHUI.strftime("%y"))
    date.append(AUJOURDHUI.strftime("%Y"))
    return date 

_date = date_du_jour()

JOUR = int(_date[0])
MOIS = int(_date[1])
ANNEE = int(_date[2])
ANNEE_ENTIERE = int(_date[3])

########################################## </Données communes> #########################################

def fete_via_date(jour,mois): 
    
    result = []
    
    if mois <= 12 and jour <= len(CALENDRIER["mois"][str(mois)]): 
        if jour < 10 and mois < 10 : 
            result.append("Le 0"+str(jour)+"/0"+str(mois)+" nous fêtons : "+CALENDRIER["mois"][str(mois)][jour]+"")
        elif jour >= 10 and mois < 10 : 
            result.append("Le "+str(jour)+"/0"+str(mois)+" nous fêtons : "+CALENDRIER["mois"][str(mois)][jour]+"")
        else : 
            result.append("Le "+str(jour)+"/"+str(mois)+" nous fêtons : "+CALENDRIER["mois"][str(mois)][jour]+"")
        
        return result 
    
    else : 
        result.append("Le mois ou le jour renseigné n'est pas correct.")
        return result
    
    
def fetes_du_mois(mois): 
    
    if mois >= 1 and mois <= 12 : 
        return CALENDRIER["mois"][(str(mois))]
    else : 
        return ["Mois inexistant ! ("+str(mois)+")"]

def fete_via_nom(_name): 
    
    result = [] 
    _name = _name.capitalize()
    i = 0 
    for mois in CALENDRIER["mois"].values():
        for names in mois:
            if _name in names:
                indice = [i for i, s in enumerate(mois) if _name in s]
                jour = indice[0]
                _mois = int(mois[0])
                if jour < 10 and _mois < 10 :
                    result.append("La fête de "+_name+" est le 0"+str(jour)+"/0"+str(_mois))
                elif jour >= 10 and _mois < 10 : 
                    result.append("La fête de "+_name+" est le "+str(jour)+"/0"+str(_mois))
                else : 
                    result.append("La fête de "+_name+" est le "+str(jour)+"/"+str(_mois))
                i = i + 1 
    if len(result) > 1 : 
        result.append(_name+" est fêté "+str(i)+" fois dans l'année.")
        
    return result

                
def demain(): 
    demain = AUJOURDHUI + timedelta(days = 1)
    jour_demain = demain.strftime("%d")
    mois_demain = demain.strftime("%m")
    return fete_via_date(int(jour_demain),int(mois_demain))

def hier() : 
    hier = AUJOURDHUI - timedelta(days = 1)
    jour_hier = hier.strftime("%d")
    mois_hier = hier.strftime("%m")
    return fete_via_date(int(jour_hier),int(mois_hier))

def aujourdhui() : 
    return fete_via_date(JOUR,MOIS) 

def toutes_les_fetes() : 
    return CALENDRIER

def bissextile(annee): 
    if(annee%4==0 and annee%100!=0 or annee%400==0):
        return True 
    else:
        return False 
        
def num_mois_to_str(num): 
    if num <= 12 and num > 0 : 
        num = str(num)
        mois = json.load(open('database/mois.json', 'r'))
        return mois[num]

def convert_to_non_accent(string):
    """ Function to convert accent characters to non accent
    characters.
    :param string: String to be converted.
    :type string: str
    :return: str
    """
    return ''.join(ch for ch in unicodedata.normalize('NFKD', string)
                   if not unicodedata.combining(ch))