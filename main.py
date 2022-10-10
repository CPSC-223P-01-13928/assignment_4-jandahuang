from weather import*
myfile = 'weather.dat'

mychoice = 0
while(True):
    print("         ***TUFFY TITIAN WEATHER LOGER MAIN MENU")
    print()
    print("1.Set data FileName")
    print("2.Add Weather Data")
    print("3.Print Daily Report")
    print("4.Print Historical Report")
    print("9.Exit the program")
    mychoice = int(input("Enter menu choice:"))
    print()
    
    if mychoice == 1:
        myfile = input("Enter Data Filename: ")
        weather = read_data(file_name = myfile)
    elif mychoice == 2:
        dt = input("Enter date: ")
        tm = input("Enter time ")
        t = int(input("Enter temperature: "))
        h = int(input("Enter temperature: "))
        r = float(input("Enter temperature: "))
        weather[dt + tm] = {'t':t, 'h': h, 'r': r}
        write_data(data = weather, file_name = myfile)
    elif mychoice == 3:
        d = input("Enter date: ")
        display = report_daily(data = weather, date = d)
        print(display)
    elif mychoice == 4:
        display = report_historical(data = weather)
        print(display)
    elif mychoice == 9:
        break