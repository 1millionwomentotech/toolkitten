# Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)

print("Lets see how many Days / Months / Hours / Minutes / Seconds Old you are!")

name = input("Enter Your Name: ")

years = int(input("Enter your age in years: "))

months = int(input("Enter the number of months since your birthday: "))

days = int(input("Enter the number of days since your birthday: "))

days += ((years * 12) + months) * 30

hours = days * 24

minutes = hours * 60

seconds = minutes * 60

print("{} is {} days, {} hours, {} minutes, {} seconds old!".format(name, days, hours, minutes, seconds))

###############################################################################################################

# Hours in a year. How many hours are in a year?
# Minutes in a decade. How many minutes are in a decade?

print("Let's Print The Number of Hours in a Year:")

# 1 year = 365 Days
# 1 day = 24 hours

total_hours = 365 * 24

print("There are 365 * 24 = {} hours in a year".format(total_hours))

print("\n\nLet's Print The Number of Minutes in a Decade:")

# 1 decade = 10 years
# 1 year = 365 Days
# 1 day = 24 hours
# 1 hour = 60 minutes

print("There are 10 * 365 * 24 * 60 = {} minutes in a decade.".format(10 * 365 * 24 * 60))

#############################################################################################################

#32-bit and 64-bit Integer Overflow (Days & Date)

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#2 ^^ 31 & 2 ^^ 63 are the maximum values for 32-bit & 64-bit Integer Overflow
# 2 ^^ 63 = 2 ^^ 31 + 2 ^^ 32 (When bases are same, powers can be added)

d1 = (2**31) / (60 * 60 * 24)
d2 = (2 **32) / (60 * 60 * 24)

print("32-bit Integer Overflow will happen in {} days.".format(d1))
print("64-bit Integer Overflow will happen in {} days.".format(d2))

int_overflow = datetime.now()
int_overflow32 = datetime.date(int_overflow + timedelta(days = d1))
int_overflow64 = datetime.date(int_overflow + timedelta(days = d2))

print("\nCounting from today i.e. {}".format(int_overflow))
print("32-bit Integer Overflow will happen on {}".format(int_overflow32))
print("64-bit Integer Overflow will happen on {}".format(int_overflow64))

##########################################################################################################
