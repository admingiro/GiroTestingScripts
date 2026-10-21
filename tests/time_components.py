#time_components.py
import datetime

def get_actual_date():
    now = datetime.datetime.now()
    return (now.strftime('%d%m%Y'))

#print("CAPAS"+get_actual_date())
