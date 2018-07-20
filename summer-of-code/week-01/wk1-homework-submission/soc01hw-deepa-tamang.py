### DAY - 1 ###

# Hours in a year
print("1. How many hours are there in a year?")
diy = 365
hid = 24
hours_in_year = diy * hid
print("Ans. There are",hours_in_year,"hours in a year.")

# Minutes in a decade
print("\n2. How many minutes are in a decade?")
years_in_decade = 10
min_in_hour = 60
min_in_decade = years_in_decade * diy * hid * min_in_hour
print("Ans. There are",min_in_decade,"minutes in a decade.")

# Your age in seconds
print("\n.3. How many seconds old are you?")

my_age = 24
age_in_sec = 24*diy*hid*min_in_hour*60
print("Age in seconds: ",age_in_sec)

#Andreea Visanoiu'age
print("\n4. I'm 48618000 seconds old. Calculate my age.  - @Andreea Visanoiu")
curr_age_in_sec = 48618000
age_in_yr = curr_age_in_sec/(60 * 60 * 24 * 365)
print("Ans. @Andreea's age is",age_in_yr)

#TOUGH QUESTIONS

#Timeout calculations
print("\nHow many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?")
totalIntFlow32 = (2**31-1)/(100*60*60*24) #Since it counts the time it has been running  in 1/100 of a second
print("Total days to timeout for 32 bit system: ", totalIntFlow32)
print("\nWhat about a 64 bit system?")
totalIntFlow64 = (2**63-1)/(100*60*60*24)
print("Total days to timeout for 64 bit system: ",totalIntFlow64)



#Calculate your age accurately based on your date of birth
import time
import datetime
from datetime import timedelta

curr_date = datetime.datetime.now()
print("\n6. Calculate your age accurately based on your birthday.")
date_entry = input('\nEnter your date of birth in YYYY-MM-DD format : ')
year,month,day = map(int, date_entry.split('-'))

try:
	time_entry = input('Enter the time of birth as HH:MM:SS format : ')
except KeyboardInterrupt:
	time_entry = "00:00:00"
except EOFError:
	time_entry = "00:00:00"
finally:
	hour, minute, second = map(int, time_entry.split(':'))

full_dob = datetime.datetime(year, month, day, hour, minute, second)
diff = curr_date - full_dob
age_in_sec = diff.total_seconds()
myyear = age_in_sec/(60*60*24*365)
mymonth = (myyear -int(myyear))*12
mydays = (mymonth - int(mymonth))*30
myhr = (mydays - int(mydays))*24
mymin = (myhr - int(myhr))*60
mysec = (mymin - int(mymin))*60
print("\nAns. My accurate age based on my birthday: {0}yrs {1}months {2}days {3}hrs {4}min {5:.2f}sec".format(int(myyear),int(mymonth),int(mydays),int(myhr),int(mymin),round(mysec,2)))

### DAY - 3 ###

#Full name greeting
print("Full name greeting")
fname = input("First name: ")
mname = input("Middle name: ")
lname = input("Last name: ")
full_name = fname + ' ' + mname + ' ' + lname
print("Hello,",full_name)

#Bigger, better favorite number
print("Favorite number")
num = input("Enter your favorite number: ")
bignum = int(num) + 1
print("The bigger better favorite number can be "+ str(bignum))

# Angry Boss
print("Angry boss's reply")
print("\nAngry Boss: What do you want??\n")
answer = input("Your answer: ")
reply = "WHADDAYA MEAN \""+ answer.upper() + "\"?!? YOU'RE FIRED!!"
print("\nAngry Boss replied, "+ reply)

# Random numbers generation

