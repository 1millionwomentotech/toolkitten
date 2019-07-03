hours_year = 24 * 365
minutes_decade = 60 * 24 * 365 * 10
age_seconds = 60 * 60 * 24 * 365 * 33
andreea = 48618000 / 60 / 60 / 24 / 365

print("How many hours are in a year? ")
print("Easy: ", hours_year)

print("And how many minutes in decade? ")
print("Easy: ", minutes_decade)

print("If I'm 33 years old, how many second old am I? ")
print("Easy: ", age_seconds)

print("If Andreea is 48618000 seconds old, how old is she in years? ")
print("Easy: ", andreea, ". So young to start learning how to code! :D ")

bit32 = (2**32) / 1000 / 60 / 60 / 24
bit64 = (2**64) / 1000 / 60 / 60 / 24

print("Okay, let's do something a bit harder, how many days does it take for a 32-bit system to timeout? ")
print("Easy: ", bit32)

print("What about a 64-bit system? ")
print("Easy: ", bit64)

print("-------------------------------------")
# Figure out your age
import datetime
currentDate = datetime.datetime.now()

deadline= input ('Plz enter your date of birth (mm/dd/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
#print (deadlineDate)
daysLeft = deadlineDate - currentDate
#print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)

months=(years-yearsInt)*12
monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)
daysInt=int(days)

hours = (days-daysInt)*24
hoursInt=int(hours)

minutes = (hours-hoursInt)*60
minutesInt=int(minutes)

seconds = (minutes-minutesInt)*60
secondsInt =int(seconds)

print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))

