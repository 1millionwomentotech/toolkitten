#1millionwomentotech Summer of Code
#Rocio Pena / rossyp44-gold#4215

from datetime import datetime, timedelta
from random import random

#---------------Week01 Day01------------------------------------------------

print("\n============A Few Things to Try - Week01 Day01============")

#Hours in a year. How many hours are in a year?
print("One year has", 365 * 24, "hours")

#Minutes in a decade. How many minutes are in a decade?
#1 decade = 10 years. each year has 24 hours and each hour has 60 minutes
print("One decade has", 365 * 10 * 24 * 60, "minutes")

#Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate-or not-as you want.)
#I'm 38 years old and a year has 365days * 24hrs * 60min * 60sec
print("I'm approximately", 38*365*24*60*60, "seconds old")

#Andreea Visanoiu: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
#1 year has a total in seconds of 365d * 24h * 60m * 60s 
print("Andreea is", round(48618000 / (365*24*60*60), 2), "years old. " +
	  "More specifically", timedelta(seconds=48618000), "old. She surely wish :|")


print("\n=============Optional Exercises - Week01 Day01=============")

#How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
#Assuming +1 every millisecond
#with 32 bits the max possible number is (2^32)-1
#1 day has 24h * 60min * 60sec * 1000milliseconds
max_number_32_bits = (2**32)-1
milliseconds_in_a_day = (24*60*60*1000)
overflow_32 = max_number_32_bits/milliseconds_in_a_day 
print("With 32-bits, in approximately", round(overflow_32), "days, the system will crash")

#How about a 64-bit system?
#same logic as before
max_number_64_bits = (2**64)-1
overflow_64 = max_number_64_bits/milliseconds_in_a_day 
print("With 64-bits, it'll be", round(overflow_64), 
	  "days OR", "{:,}".format(round(overflow_64/365/100)), "centuries. Enough for a human life?")

#Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.
#So, my DoB is March/10/1980 7:25am and at the moment of running this program I'm this much seconds old
now = datetime.now()
b_date = datetime(1980, 3, 10, 7, 25)
diff = now - b_date
print("I'm", int(diff.total_seconds()), "seconds old. I was born on March/10/1980 7:25am")
print("I'm", "{:,}".format(int(diff.total_seconds())), "seconds old. In a more readable format :)")


#---------------Week01 Day02------------------------------------------------
#No homework :)

#---------------Week01 Day03------------------------------------------------

print("\n============A Few Things to Try - Week01 Day03============")

#Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. 
#For example, if you type in I want a raise, it should yell back like this:
#WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
msg = input("Please type a message for your not very lovely boss: ")
print("WHADDAYA MEAN \"" + msg.upper() + "\"?!? YOU'RE FIRED")

#Table of contents. Here's something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
#Table of Contents
#Chapter 1: Getting Started     page 1 
#Chapter 2: Numbers             page 9 
#Chapter 3: Letters             page 13

print("\nTable of Contents")
print("Chapter 1: Getting Started".ljust(35), "page 1")
print("Chapter 2: Numbers".ljust(35), "page 9")
print("Chapter 3: Letters".ljust(35), "page 13")

print("\n")
print("Table of Contents2".center(60))
print("Homework  :".rjust(30, '-') + "  " + "Numbers and Strings".ljust(30, '-'))
print("Hackathon  :".rjust(30, '-') + "  " + "Continent Counter".ljust(30, '-'))
print("Lecture  :".rjust(30, '-') + "  " + "Flow Control".ljust(30, '-'))
print("Q&A  :".rjust(30, '-') + "  " + "Pair Programming".ljust(30, '-'))

print("\n=============Optional Exercises - Week01 Day03=============")

#Random Numbers - Optional
#Research how to generate a random number with Python.
#Then try to generate your random Civilization III world by generating a land 'X' tile or a water 'o' tile randomly:
# oooXXXoo
# oooXoXoo
# XXXooXoo

for i in range(8):
	row = ''
	for j in range(8):
		rand = random()
		if rand <= 0.5:
			row += "o"
		else:
			row += "X"
	print(row)	







