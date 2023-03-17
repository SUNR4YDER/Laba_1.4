date = input()
day = date[0:2]
month = date[3:5]
year = date[8:]
if(int(day)>31):
    print("Неправильно указан номер дня")
elif(int(month)>12):
    print("Неправильно указан номер месяца")
else:
    if(int(day)*int(month)==int(year)):
        print("Дата является магической")
    else:
        print("Дата не является магической")