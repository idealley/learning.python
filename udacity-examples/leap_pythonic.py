def is_leap_baby(year):
    if ((year % 4 is 0) and (year % 100 is not 0)) or (year % 400 is 0):
        return "{0}, {1} is a leap year".format(True, year)
    return "{0} is not a leap year".format(year)

print(is_leap_baby(2014))
print(is_leap_baby(2012))