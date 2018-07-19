#Day 1
#=======================================================================


#How many hours are in a year?

import calendar
year = int(input("enter a year: "))
if calendar.isleap(year):
    days=366
else:
    days=365
hours=days*24
print("The number of hours in a year is " + str(hours))


#How many minutes are in a decade?

days_in_decade = (365*8)+(366*2)#there are 2 leap years in a decade
hours_in_decade=days_in_decade*24
minutes_in_decade=hours_in_decade*60
print(days_in_decade)
print("The number of minutes in a decade is " +str(minutes_in_decade))


#How many seconds old are you?

import datetime
my_date = datetime.datetime(1995,7,24,12,0,0)
today = datetime.datetime.now()
date_difference = today-my_date
print("my age in seconds is "+str(round(date_difference.total_seconds())))


#Andreea Visanoiu​ is 48618000 seconds old. Calculate @Andreea Visanoiu's age. #725320264

import math
Andreea_sec = 48618000
Andreea_age = math.floor(Andreea_sec/3600/24/365)
print("Andreea's age is "+str(Andreea_age))


#How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?

#How many days does it take for a 64-bit system to timeout, if it has a bug with integer overflow?


#Calculate your age accurately based on your birthday

my_date = datetime.datetime(1995,7,24,12,0,0)
today = datetime.datetime.now()
date_difference = today-my_date
print("My age is "+str(date_difference.days//365))

#Day 3
#=======================================================================


#Full Name Greeting

first = input("please enter your first name: ")
middle = input("please enter your middle name: ")
last = input("please enter your last name: ")
print("Hello %s %s %s, we are delighted to have you onboard:)" % (first,middle,last))


#Bigger, better favorite number.

fav = int(input("Please enter your favourite number: "))
print("%d can be your bigger and better favourite number :)" % (fav+1))


#Angry Boss

want = input("What do you want?: ")
print("WHADDAYA MEAN \""+want.upper()+"\"?!? YOU'RE FIRED!!")


#Table of Content

header ="Table of Contents"
content = [["Chapter 1:", "Getting Started", "page 1"],["Chapter 2:", "Numbers", "page 9"],["Chapter 3:", "Letters", "page 13"]]
print(header+"\n")
for i in content:
    print(i[0].ljust(11, ' ')+i[1].ljust(23,' ')+i[2])
