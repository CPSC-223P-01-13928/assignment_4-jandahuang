import calendar
from dataclasses import dataclass
from http.client import _DataType
import json
from calendar import month_name

def read_data(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def write_data(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data,f)

def max_temperature(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if date[key]['t'] > x:
                x = data[key]['t']
    return x

def min_temperature(data, date):
    x = 9999
    for key in data:
        if date == key[:8]:
            if date[key]['t'] < x:
                x = data[key]['t']
    return x

def max_humidity(data, date):
    x = 0
    for key in data:
        if date == key[:8]:
            if date[key]['h'] > x:
                x = data[key]['h']
    return x

def min_humidity(data, date):
    x = 9999
    for key in data:
        if date == key[:8]:
            if date[key]['h'] < x:
                x = data[key]['h']
    return x

def tot_rain(data, date):
    sum = 0
    for key in data:
        if date == key[:8]:
           sum += date[key]['r']
    return sum

def report_daily(data, date):
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    
    display = "========================= DAILY REPORT ========================\
            Date                      Time  Temperature  Humidity  Rainfall\
            ====================  ========  ===========  ========  ======== "
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name(int(date[4:6]) + \
                str(int(date[6:8])), ", " + str(int(date[0:4])))
            
            tm = key[8:10] + ": " + key[10:12] + ": " + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']
            display += f'{m:22}{tm:8}{t:13}{h:10}{r:10.2f}' + "\n"
    
    return display

def report_historical():
    display = "============================== HISTORICAL REPORT ===========================\			  
        Minimum      Maximum   Minumum   Maximum     Total\
        Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\
        ====================  ===========  ===========  ========  ========  ======== "
        
        