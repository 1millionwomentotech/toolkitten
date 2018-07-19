# day1

import datetime

hoursInYear= 365*24
hoursInLeadYear = 366*24
minutesInDecade = 365.25*10*24*60 #allowing leap year

print('Hours in a year     : '+(str)(hoursInYear))
print('Hours in lead year  : '+(str)(hoursInLeadYear))
print('Minutes in a decade : '+(str)(minutesInDecade))

print('Seconds in my age (21) : '+ (str)(21*365*24*60*60))

now = datetime.datetime.now()
myBirth = datetime.datetime.strptime("16/10/1997","%d/%m/%Y")

age = (now-myBirth)

print('My age accurately : ' + (str)(age))

