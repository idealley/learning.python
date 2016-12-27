# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
import datetime

def leap_year(year):
    if ((year % 4 is 0) and (year % 100 is not 0)) or (year % 400 is 0):
        return 366
    return 365        


def length_month(month, year):
    long_month = [1,3,5,7,8,10,12]
    if month in long_month:
        return 31
    elif month == 2 and leap_year(year) == 366:
        return 29
    elif month == 2:    
        return 28
    return 30


def days_old(day, month, year):
    now = datetime.datetime.now()
    days = length_month(month, year) - day + now.day

    days += sum([length_month(month, year) for month in range(month + 1, 12 + 1)]) 
    days += sum([leap_year(year) for year in range(year + 1, now.year)]) # We do not need to count the current year as we calculate it bellow
    days += sum([length_month(m, now.year) for m in range(1, now.month)]) # We do not need the current month as we have already added it (now.day)

    return days

print("Samuel: ", days_old(10, 3, 1981))
print("Nicolas: ", days_old(17, 3, 1974))
print("Steph: ", days_old(11, 10, 1953))
print("Sara: ", days_old(9, 10, 1982))
print("France: ", days_old(19, 1, 1958))