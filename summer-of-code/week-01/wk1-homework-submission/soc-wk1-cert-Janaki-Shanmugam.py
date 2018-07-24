#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:43:43 2018

@author: shanmugamjanaki
"""
"""Day 1"""

# hours in a year
yr_hrs = 365*24
print("There are", yr_hrs, "hours in a year.")

#minutes in a decade
dec_mins = 10*yr_hrs*60
print("There are", dec_mins, "minutes in a decade.")

from datetime import date
from datetime import timedelta
from datetime import datetime

#calculate age (in years)
birthday = date(1988,10,7)
def calc_age_yrs(birthday):
    today = date.today()
    return today.year - birthday.year - ((today.month,today.day) < (birthday.month,birthday.day))
print("I am", calc_age_yrs(birthday), "years old.")


#calculate age (in seconds)
birthday = datetime(1988,10,7,8,44,0)
age_secs = (datetime.now() - birthday).total_seconds()
print("I am", age_secs, "seconds old.")

# calculate birthdate (reverse)
#birthday = datetime.now() - timedelta(0,939606855.727789)
birthday = datetime.now() - timedelta(0,48618000)
print ("Andrea's birthday is on", birthday.strftime("%d %b %Y"), ".")

"""Day 3"""

# Greeting
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name (Or type enter to skip): ")
last_name = input("Enter your last name: ")
print("Hi", first_name, middle_name, last_name, "!")

#Bigger, better number
fav_no = input("Enter your favourite number: ")
bb_no = int(fav_no) + 1
print("Have you considered the number", bb_no, "? It is bigger and better!")

#Angry boss
rude_ans = input("WHAT DO YOU WANT?: " )
print('WHADDYA MEAN "', rude_ans, '"?!? YOU\'RE FIRED!!' )

#Table of Contents
print("Table of Contents \n"
      "Chapter 1:".ljust(1), "Getting Started".center(25), "page 1".rjust(10),"\n"
      "Chapter 2:".ljust(1), "Numbers".center(25), "page 9".rjust(10), "\n"
      "Chapter 3:".ljust(1), "Letters".center(25), "page 13".rjust(10))

"""Day 4"""
# 99 bottles of beer on the wall
b = 99
while b >= 0:
    if b > 1:
        print("bottles of beer on the wall,", b, "bottles of beer.")
        print("Take one down and pass it around,", b-1, "bottles of beer on the wall.")
    if b == 2:
        print("bottles of beer on the wall,", b, "bottles of beer.")
        print("Take one down and pass it around,", b-1, "bottle of beer on the wall.")
    if b == 1:
        print("bottle of beer on the wall,", b, "bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    if b == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    b -= 1

#Deaf Grandma
from numpy import random
grandma_yr = random.randint(1930,1950)
grandma = input("Say something to Grandma: ")
while grandma != "BYE":
    if (grandma.isupper()) == False:
        print("HUH!? SPEAK UP, GIRL!")
        grandma = input("Say something to Grandma: ")
    if grandma.isupper():
        if grandma != "BYE":
            print("NO, NOT SINCE", grandma_yr, "!")
            grandma = input("Say something to Grandma: ")
        if grandma == "BYE":
            print("NO, NOT SINCE", grandma_yr, "!")
            grandma = input("Say something to Grandma: ")
            if grandma == "BYE":
                print("NO, NOT SINCE", grandma_yr, "!")
                grandma = input("Say something to Grandma: ")
                if grandma == "BYE":
                    print("BYE!")
                    break

#Leap years
year_start = int(input("Enter starting year: "))
year_end = int(input("Enter ending year: "))
leap_count = 0
print("These are the leap years:")
for i in range(year_start,year_end+1):
    if i%4 == 0:
        if i%100 != 0 or (i%100 == 0 and i%400 == 0):
            leap_count += 1
            print(str(i))

#Sorting array/list
word_input = None
word_list = []
while True:
    word_input = input("Enter one word at a time (or press 'Enter' to end list): ")
    word_list.append(word_input)
    if not word_input:
        break
word_list.remove("")
print(sorted(word_list))

#Table of Contents
toc = ["Table of Contents", "Chapter 1:", "Getting Started", "page 1",
       "Chapter 2:", "Numbers", "page 9", "Chapter 3:", "Letters", "page 13"]
print(toc[0].center(50),"\n\n",
      toc[1].ljust(1), toc[2].center(25), toc[3].rjust(10),"\n",
      toc[4].ljust(1), toc[5].center(25), toc[6].rjust(10),"\n",
      toc[7].ljust(1), toc[8].center(25), toc[9].rjust(10))

#function - print moo
def say_moo_5(n):
    print("moo"*n)
say_moo_5(5)

#OldSchool Roman numerals
number_input = int(input("Enter a number between 1 and 3000: "))
def ORM(number_input):
    old_roman_numeral = []
    numerals = ["M","D","C","L","X","V","I"]
    integers = [1000,500,100,50,10,5,1]
    for i in range(len(integers)):
        R = int(number_input/int(integers[i]))
        if R != 0:
            old_roman_numeral.append(R*numerals[i])
            number_input -= R*int(integers[i])
    return (''.join(old_roman_numeral))
ORM(number_input)

#Modern Roman numerals
number_input = int(input("Enter a number between 1 and 3000: "))
def MRM(number_input):
    modern_roman_numeral = []
    numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    for i in range(len(integers)):
        R = int(number_input/int(integers[i]))
        if R != 0:
            modern_roman_numeral.append(R*numerals[i])
            number_input -= R*int(integers[i])
    return(''.join(modern_roman_numeral))
MRM(number_input)
