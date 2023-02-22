from flask import *
import json 
from backend.functions import *

with open('database/calendar.json') as f:
   in_memory_datastore = json.load(f)
   
app = Flask(__name__)
   

@app.route('/fetes', methods=['GET', 'POST'])
def all():
   if request.method == 'GET' :    
      month = request.args.get('month', type = int)
      if month : 
         return get_celebrations_of_month(month)
      else :
         return in_memory_datastore
   # elif request.method == 'POST' : 
   #    month = request.json["month"]
   #    return {"result:":get_celebrations_of_month(month)}
   
@app.route('/fetes/<day>/<month>')
def get_celebration_from_date(day,month):
   
     day = int(day) ; month = int (month)
     return {"result":getCelebrationFromDate(day,month)}

@app.route('/fetes/<name>')
def get_name(name):
    return {name:get_celebration_from_name(name)}
 
@app.route('/today')
def get_today_celebration():
    return {"result":celebration(0)}
 
@app.route('/tomorrow')
def get_tomorrow_celebration():
    return {"result":celebration(1)}

@app.route('/yesterday')
def get_yesterday_celebration():
    return {"result":celebration(1)}

