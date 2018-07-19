#!/usr/bin/env python3
import random
# Day1
# Hours in a year
print(365 * 24)
# Minutes ina decade
print(10*365*24)
# My age in a seconds
print(27*365*24*60*60)
# Andrea Visanoiu age
print(48618000/365/24/60/60)

#Day2
# ---

#Day3
#Full name greeting
first_name = input("What is your fist name? ")
middle_name = input("What is your middle name? ")
last_name = input("What is your last name? ")
print("Nice to meet you "+ first_name + " "+middle_name+" "+last_name)

#Bigger, better favourite number
favourite_number = input("What is your favourite number? ")
print("What a great number! But I think the better is " + str(int(favourite_number)-1))

#Angry Boss
employee_question = input("What do you want? ")
print("WHADDYA MEAN " + "\"" + employee_question.upper() + "\"?! YOU ARE FIRED!!")

#Table of contents
print("Table of Contents \n".center(48))
print("Chapter 1: "+"Getting Started".ljust(30)+"page 1")
print("Chapter 2: "+"Numbers".ljust(30)+"page 9")
print("Chapter 3: "+"Letters".ljust(30)+"page 13")

#More Arithmetic 
print(pow(7,2))
print(365%7)
print(abs(-7))

#Random Number
print(random.randint(1,99))
print(random.choice(["o", "X"]))

#Day4

#99 Bottles of Beer on the Wall
bottle_song = " of Beer on the Wall."
num_bottle = 99
bottle = " Bottles"

while num_bottle !=0:
    if num_bottle ==1:
        bottle = " Bottle"
    print(str(num_bottle) + bottle + bottle_song)
    num_bottle -= 1

#Deaf grandma
shout = ""
while True:
    shout = input("What is your favourite color grandma? ")
    if shout == "BYE":
        break
    if bytes(shout, 'utf8').isupper():
        print("NO, NOT SINCE "+ str(random.randint(1930,1950)))
    else:
        print("HUH?! SPEAK UP, GIRL!")

#Deaf grandma extended
shout = ""
shout_counter = 0
while True:
    shout = input("What is your favourite color grandma? ")
    if shout == "BYE":
        shout_counter += 1
        if(shout_counter == 3):
            break
    else:
        shout_counter = 0
    if bytes(shout, 'utf8').isupper():
        print("NO, NOT SINCE "+ str(random.randint(1930,1950)))
    else:
        print("HUH?! SPEAK UP, GIRL!")

#Leap years
starting_year = int(input("Type starting year"))
ending_year = int(input("Type ending year"))
while starting_year != ending_year + 1:
    if starting_year%4== 0:
        if starting_year%100!=0 or starting_year%400 ==0:
            print(starting_year)
    starting_year +=1

#Building and sorting an array
array = []
while True:
    word = input("Type a word ")
    if word !="":
        array.append(word)
    else:
        break

array.sort()
for x in array:
    print(x)

#Function that prints out "moo" n times
def say_moo(num):
  while num !=0:
    print("moo")
    num -= 1
say_moo(5)

#Old-school Roman numerals
def old_roman_numeral(number: int):
    roman_numral = ""
    while number>0:
        if number >= 1000:
            roman_numral += "M"
            number -= 1000
        elif number >=500:
            roman_numral += "D"
            number -= 500
        elif number >=100:
            roman_numral += "C"
            number -= 100
        elif number >= 50:
            roman_numral += "L"
            number -= 50
        elif number >= 10:
            roman_numral += "X"
            number -= 10
        elif number >= 5:
            roman_numral += "V"
            number -= 5
        elif number >= 1:
            roman_numral += "I"
            number -= 1
    return roman_numral
        

print(old_roman_numeral(2438))
