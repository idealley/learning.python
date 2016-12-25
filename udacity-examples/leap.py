def is_leap_baby(day,month,year):
    if year%4==0:
        if year%100==0:
            if year%400!=0:
                return 'this is not a leap year'
            else:
                return 'this is a leap year'  
        else:
            return 'this is a leap year'  
    else:
        return 'this is not a leap year' 
                
print(is_leap_baby (9, 10, 2014))