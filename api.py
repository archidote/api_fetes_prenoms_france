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
   # elif request.method == 'POST' : 
   #    month = request.json["month"]
   #    return {"result:":get_celebrations_of_month(month)}
   
@app.route('/fetes/<day>/<month>')
def get_celebration_from_date(day,month):
   
     day = int(day) ; month = int (month)
     return {"result":getCelebrationFromDate(day,month)}

@app.route('/fetes/<name>')
def get_name(name):
    return {"result":fete_via_nom(name)}
 
@app.route('/aujourdhui')
def get_today_celebration():
    return {"result":aujourdhui()}
 
@app.route('/tomorrow')
def get_tomorrow_celebration():
    return {"result":demain()}

@app.route('/yesterday')
def get_yesterday_celebration():
    return {"result":hier}

@app.route('/')
def racine():
    return {"result":"Consultez la documentation : "}
