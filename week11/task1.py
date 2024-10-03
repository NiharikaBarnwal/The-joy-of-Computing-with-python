import calendar

def check_leap(year):
    if year%400==0 or (year%100!=0 and year%4==0):
        return True
    else:
        return False

def check_valid_date(date,month,year,leap):
    if(month==2 and leap):
        if date<30:
            return True
    elif(month==2 and not leap):
        if date<28:
            return True
    elif(month==7 or month==8):
        if date<32:
            return True
    elif(month%2!=0 and month<7):
        if date<32:
            return True
    elif(month%2==0 and month>7 and month<12):
        if date<32:
            return True
    else:
        if date<31:
            return True
    return False

def get_day(day_index):
    list_of_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return list_of_days[day_index]

# year
while(1):
    year = int(input("Enter year (1970-2024):"))
    if year<1970 or year>2024:
        print("Enter a year in the range 1970 to 2024")
    else:
        break

# month
while(1):
    month = int(input("Enter month (1-12):"))
    if month<1 or month>12:
        print("Enter a month in the range 1 to 12")
    else:
        break

leap=check_leap(year)

# valid date
while(1):
    date = int(input("Enter date:"))
    if check_valid_date(date,month,year,leap):
        break
    else:
        print("Enter a valid date")

day_index=calendar.weekday(year,month,date)
day=get_day(day_index)
print(date,'/',month,'/',year,'falls on',day)