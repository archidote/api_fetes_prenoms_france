from datetime import date

from datetime import date

def getTodayCelebration():
    today = date.today()
    d = today.strftime("%d/%m")
    return d 

print(getTodayCelebration())