from flask import *
import json 
from backend.functions import *
 
app = Flask(__name__)
   

@app.route('/fetes', methods=['GET', 'POST'])
def all():
   if request.method == 'GET' :    
      month = request.args.get('month', type = int)
      if month : 
         return fetes_du_mois(month)
      else :
         return toutes_les_fetes()
   
@app.route('/fetes/<jour>/<mois>')
def fete_prenom_depuis_date(jour,mois):
     jour = int(jour) ; mois = int (mois)
     return {"result":fete_via_date(jour,mois)}

@app.route('/fetes/<prenom>')
def fete_prenom(prenom):
    return {"result":fete_via_nom(prenom)}
 
@app.route('/aujourdhui')
def fete_du_jour():
    return {"result":aujourdhui()}
 
@app.route('/demain')
def fete_demain():
    return {"result":demain()}

@app.route('/hier')
def fete_hier():
    return {"result":hier()}

@app.route('/')
def racine():
    return {"result":"Consultez la documentation : "}
