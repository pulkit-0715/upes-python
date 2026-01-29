def is_leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True   
            else:
                return False 
        else:
            return True      
    else:
        return False         

day = int(input("day="))
month = int(input("month="))
year = int(input("year="))

days_in_month = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if is_leap(year):
    days_in_month[2] = 29

day += 1


if day > days_in_month[month-1]:
    day = 1
    month += 1


if month > 12:
    month = 1
    year += 1

print(f"day={day} month={month} year={year}")