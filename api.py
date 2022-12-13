from flask import Flask, request
import json 
from backend.functions import *

with open('database/calendar.json') as f:
   in_memory_datastore = json.load(f)
   
app = Flask(__name__)
   

@app.get('/fetes')
def all():
   month = request.args.get('month', type = int)
   if month : 
      return get_celebrations_from_month(month)
   else :
      return in_memory_datastore
   
@app.route('/fetes/<day>/<month>')
def get_celebration_from_date(day,month):
   
     day = int(day) ; month = int (month)
     return {"result":getCelebrationFromDate(day,month)}

@app.route('/fetes/<name>')
def get_celebration_from_name(name):
    return {name:get_celebration_from_name(name)}
 
@app.route('/today')
def get_today_celebration():
    return {"result":celebration(0)}
 
@app.route('/tomorrow')
def get_tomorrow_celebration():
    return {"result":celebration(1)}

