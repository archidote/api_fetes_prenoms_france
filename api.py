from flask import *
from backend.functions import *
from waitress import serve

app = Flask(__name__)
app.debug = True

@app.route('/fetes', methods=['GET', 'POST'])
def all():
   if request.method == 'GET' :    
      mois = request.args.get('mois', type = int)
      if mois : 
         return {num_mois_to_str(mois):fetes_du_mois(mois)}
      else :
         return toutes_les_fetes()
   
@app.route('/fete/<jour>/<mois>')
def fete_prenom_depuis_date(jour,mois):
     jour = int(jour) ; mois = int (mois)
     return {"result":fete_via_date(jour,mois)}

@app.route('/fete/<prenom>')
def fete_prenom(prenom):
    return {"result":fete_via_nom(prenom)}
 
@app.route('/fete/aujourdhui')
def fete_du_jour():
    return {"result":aujourdhui()}
 
@app.route('/fete/demain') # Gérer le 29/02 (bissexitle only) 
def fete_demain():
    return {"result":demain()}

@app.route('/fete/hier') # Gérer le 29/02 (bissexitle only) 
def fete_hier():
    return {"result":hier()}

@app.route('/bissextile') # Gérer le 29/02 (bissexitle only) 
def type_annee():
    return {ANNEE_ENTIERE:bissextile(ANNEE_ENTIERE)}

@app.route('/bissextile/<annee>')
def type_annee_choix(annee):
    annee = int(annee)
    return {annee:bissextile(annee)}

@app.route('/')
def racine():
    return {"result":"Consultez la documentation : https://github.com/archidote/api_fetes_prenoms_france"}

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)