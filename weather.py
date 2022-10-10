import json
import calendar

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
    display = "========================= DAILY REPORT ========================\n"
    display += "       Date                      Time  Temperature  Humidity  Rainfall\n"
    display += "       ====================  ========  ===========  ========  ======== "
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name(int(date[4:6]) + \
                str(int(date[6:8])), ", " + str(int(date[0:4])))
            
            tm = key[8:10] + ": " + key[10:12] + ": " + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']
            display += f'{m<22}' + f'{tm<10}' + f'{t>11}' + f'{h>10}' + f'{r>10}' + "\n"
    
    return display


def report_historical(data):
    display = "============================== HISTORICAL REPORT ===========================\n"
    display += "              Minimum      Maximum   Minumum   Maximum     Total/n"
    display += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display += "====================  ===========  ===========  ========  ========  ======== \n"

    h = ''
    print("1")
    for key in data[0:8]:
        print("in loop")
        if h == key[0:8]:
            continue
        else:
            h == key[0:8]
            m = calendar.month_name[int(h[4:6])] + " " + str(int(h[6:8])) + "," + str(int(h[0:4]))
    
    print("2")
    min_temp = min_temperature(data, h)
    max_temp = max_temperature(data, h)
    min_hum = min_humidity(data, h)
    rain = tot_rain(data, h)

    display += f'{m:20}' + f'{min_temp:13}' + f'{max_temp:13}' + f'{min_hum:10}' + f'{rain:10:2f}' + "\n"
    return display
