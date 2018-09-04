####################################################### A few things to try###################################################

#####DAY 1#####

## Hours in a year. How many hours are in a year?
print("Hours in a year", 24*365)
# Hours in a year 8760

## Minutes in a decade. How many minutes are in a decade?
print("Minutes in a decade", 10*365*24*60)
# Minutes in a decade 5256000

## Your age in seconds. How many seconds old are you?
print("My age in seconds", 23*365*24*60*60)
# My age in seconds 725328000

## Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print("Her age:", 48618000/(60*60*24*365))
# Her age: 1.54166
#Strange :o

## How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
print("Days does it take for a 32-bit system to timeout, if it has a bug with integer overflow:", ((2**32)/1000/60/60/24))
#Days does it take for a 32-bit system to timeout, if it has a bug with integer overflow: 49.710269629629636

## How about a 64-bit system?
print("Days does it take for a 64-bit system to timeout, if it has a bug with integer overflow:", ((2**64)/1000/60/60/24))
#Days does it take for a 64-bit system to timeout, if it has a bug with integer overflow: 213503982334.60132

## Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - 
## you will need Python modules
from datetime import datetime
print("Age based on birthday:", datetime.today()-datetime.strptime("22/4/1995 12:00", '%d/%m/%Y %H:%M'))
#Age based on birthday: 8526 days, 7:47:55.427735

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#####DAY 2#####

##Escape characters must always escape themselves. Why?
print("Escape characters such as backslash need to be escaped. \\ It is because, if we type any letter in front of a single backslash, It might become another escape character. Like \n new line")
#Escape characters such as backslash need to be escaped. \ It is because, if we type any letter in front of a single backslash, It might become another escape character. Like 
# new line

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#####DAY 3#####

##Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. 
##Finally, it should greet the person using their full name.
first_name = input("What is your first name? \n")
middle_name = input("What is your middle name? \n")
last_name = input("What is your last name? \n")
print("Hello " + first_name + " " + middle_name + " " + last_name + "!")
# What is your first name? 
# Sameeksha
# What is your middle name? 
# S
# What is your last name? 
# M
# Hello Sameeksha S M!

##Bigger, better favorite number. Write a program that asks for a person’s favorite number. 
##Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. 
##(Do be tactful about it, though.)
input_number = input("What is your favorite number? \n")
input_number = int(input_number)
print("You might like "+str(input_number+1) + ". It is a bigger and a better number than " + str(input_number) + ".")
# What is your favorite number? 
# 22
# You might like 23. It is a bigger and a better number than 22.

##Angry boss. Write an angry boss program that rudely asks what you want. 
##Whatever you answer, the angry boss should yell it back to you and then fire you. 
##For example, if you type in I want a raise, it should yell back like this: WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
ask = input("WHAT DO YOU WANT??! \n")
print("WHADDAYA MEAN " + "\"" + ask.upper() + "\"" + "?!? YOU'RE FIRED!!")
WHAT DO YOU WANT??! 
# i want raise
# WHADDAYA MEAN "I WANT RAISE"?!? YOU'RE FIRED!!

##Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: 
## write a program that will display a table of contents so that it looks like this: 
## Table of Contents Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13
print("Table of Contents".center(100))
print("Chapter 1: Getting Started".ljust(5) + " page1".rjust(72))
print("Chapter 2: Numbers".ljust(5) + " page9".rjust(80))
print("Chapter 3: Letters".ljust(5) + " page13".rjust(81))
#                                          Table of Contents                                          
# Chapter 1: Getting Started                                                                   page1
# Chapter 2: Numbers                                                                           page9
# Chapter 3: Letters                                                                           page13

##pow(base, power) 365%7 abs(-7)
pow(2,4)
#16
365%7
#1
abs(-7)
#7

##Research how to generate a random number with Python. 
##Then try to generate your random Civilization III world by generating a land 'X' tile or a water 'o' tile randomly:
#	oooXXXoo
#	oooXoXoo
#	XXXooXoo
import random
i=0
civilization = ""
while i <8:
    civilization = civilization + random.choice('Xo')
    i = i+1
print(civilization)
#XXooXooX

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#####DAY 4#####

##“99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
for i in range(0, 99):
	print("\n" + str(99-i) + " bottles of beer on the wall, " + str(99-i) + " bottles of beer.")
	if 99-(i+1) == 0:
		print("Take one down and pass it around, no more bottles of beer on the wall.")
	else:
		print("Take one down and pass it around, ", str(99-(i+1)) + " bottles of beer on the wall.")
print("\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")

##Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL!
##unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:NO, NOT SINCE 1938!
