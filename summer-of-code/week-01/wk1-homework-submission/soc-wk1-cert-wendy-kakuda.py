import numpy as np
import datetime
from datetime import date
# Day One============
hourSec = (60*60)
daySec = (24 * hourSec)
yearSec = (365 * daySec)
dayMin=(24*60)
yearHr = (365*24)
aAge =48618000
thirtyTwoBit =2147483647
sixtyFourBit =9223372036854775807
b_date = (1978, 7, 21, 15, 00)

print("======Hours in a year=======")
print(yearHr)

print("======Minutes in a decade=======")
print((dayMin*365) * 10)

print("======My age in secs=======")
print(39 * yearSec)

print("======Andreea Visanoiu​'s Age=======")
print(aAge/yearSec)

print("======Andreea's Age=======")
print(aAge/yearSec)

print("======32-bit timeout in days=======")
print(thirtyTwoBit/daySec)

print("======64-bit timeout in days=======")
print(sixtyFourBit/daySec)

print("======My exact age from birthdate=======")
print()

# Day 3
print("======PERSONAL GREETINGS========")
first_name = (input("What is your first name? "))
middle_name = (input("What is your middle name?"))
last_name = (input("What is your last name?"))
greeting = ("Hello "+first_name+" "+middle_name+" "+last_name+" and welcome!")
print(greeting)

print("=======LUCKY NUMBER=========")
fav_num = input("What is your favourite number?")
new_num = int(fav_num) + 1
print("I have a good feeling that "+str(new_num)+" will be a lot luckier for you! Try it!")

print("=======ANGRY BOSS=========")
request = input("What do you want!!")
print("WHADDAYA MEAN \""+request.upper()+"\"?!? BACK TO WORK OR YOU ARE FIRED!!")

print("=======TOC=========")
title = "Table of Contents"
ch1 = "Chapter 1: Getting Started page 1"
ch2 = "Chapter 2: Numbers page 9"
ch3 = "Chapter 3: Letters page 13"
print(title.ljust(50, ' '))
print(ch1.ljust(1, ' '), ch2.center(1, ' '), ch3.rjust(1, ' '))

print("========RANDOM NUMBER TILES 11 x 11=======")
civ_cont = np.random.random_integers(0, 1, size=(11,11))
print(civ_cont)

print("========RANDOM X & O TILES 11 x 11 =======")
civ_arr = ['x', 'o']
civ_cont = np.random.choice(civ_arr, size=(11,11))
print(civ_cont)


