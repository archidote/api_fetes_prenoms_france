from flask import Flask, request
import json 
from test import getCelebrationFromDate, getCelebrationFromName

def get_programming_language(programming_language_name):
   return in_memory_datastore[programming_language_name]

def update_programming_language(lang_name, new_lang_attributes):
   lang_getting_update = in_memory_datastore[lang_name]
   lang_getting_update.update(new_lang_attributes)
   return lang_getting_update

def delete_programming_language(lang_name):
   deleting_lang = in_memory_datastore[lang_name]
   del in_memory_datastore[lang_name]
   return deleting_lang


with open('api/2.json') as f:
   in_memory_datastore = json.load(f)
   
app = Flask(__name__)
   

@app.get('/fetes')
def list_programming_languages():
    return (in_memory_datastore)

@app.route('/fetes/nom/<name>')
def get_celebration_from_name(name):
    return {name:getCelebrationFromName(name)}
 
@app.route('/fetes/date/<day>/<month>')
def get_celebration_from_date(day,month):
   
     day = int(day) ; month = int (month)
     return {"result":getCelebrationFromDate(day,month)}
 