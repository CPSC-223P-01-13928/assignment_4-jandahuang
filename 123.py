import calendar
import string


def report_daily(data, date):
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    
    display = "===================================\
        = Daily Report ================================="
                
    display += "Date                   Time  Temp\
        erature  Humanity  Rainfall"
        
    display += "\n================ =============== ======\
        ======== ==========="
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name(int(date[4:6]) + \
                str(int(date[6:8])), ", " + str(int(date[0:4])))
            print(type(date[0:4]))
            
    a = "20211126232921"
    # display += "\n"       