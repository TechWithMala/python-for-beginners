#Date and time demo...

#import datetime module to use date time objects
import datetime
print(datetime.datetime.now()) #YYYY-MM-DD HH:MM:SS.microsecond

#create a date object using datetime module's datetime() constructor
print(datetime.datetime(2020, 1, 20)) #YYYY MM DD, rest of the parameters(HH:MM:SS.microsecond) are optional

#format datetime objects into readable format using strftime() function
dt = datetime.datetime(2020, 11, 20)
print("Short version of day of a week...")
print(dt.strftime(("%a")))

print("Full version of day of a week...")
print(dt.strftime(("%A")))

print("Short version of name of a month...")
print(dt.strftime(("%b")))

print("Full version of name of a month...")
print(dt.strftime(("%B")))
