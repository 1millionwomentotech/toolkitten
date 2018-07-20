
#### Day 1 ####

## Exercise: Write a program that tells you the following:
# Hours in a year. How many hours are in a year?

hoursInYear = 365 * 24
print ("There are " + str(hoursInYear) + " hours in a year")

# Minutes in a decade. How many minutes are in a decade?

minInDec = 10 * 365 * 24 * 60
print("There are " + str(minInDec) + " minutes in a decade")

# Your age in seconds. How many seconds old are you? 

myAgeInSec = 29 * 365 * 24 * 60 * 60
print("My age in seconds is: " + str(myAgeInSec))

# Andreea Visanoiu​: I'm 48618000 seconds old. Calculate @Andreea Visanoiu's age.

andreasAge = 48618000 / (365 * 24 * 60 * 60)
print("Andrea's age is " + str(andreasAge))

## Exercise: How many days does it take for a 32-bit (then 64-bit) system to timeout, if it has a bug with integer overflow.

from datetime import datetime, timedelta, date, time
from dateutil import relativedelta

timeOutInDays1 = (2**31-1) / (60/60/24)
timeOut1 = datetime(1970, 1, 1) + timedelta(seconds=2**31-1)

print(timeOut1)
print("For a 32-bit system to timeout, it takes " + str(timeOutInDays1) + " days. Therefore, it will timeout on " + str(timeOut1) + " if it has a bug with integer overflow.")

timeOutInDays2 = (2**63-1) / (60/60/24)

print("For a 64-bit system to timeout, it takes " + str(timeOutInDays2) + " days.")

## Exercise: Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday)

today = datetime.now()
birthday = datetime(1989, 5, 21, 12)
difference = relativedelta.relativedelta(today, birthday)

years = difference.years
months = difference.months
days = difference.days
hours = difference.hours
minutes = difference.minutes
seconds = difference.seconds

print("My accurate age in years, months, days, hours, minutes and seconds is " + str(years) + ", " + str(months) + ", " + str(days) + ", " + str(hours) + ", " + str(minutes) + ", " + str(seconds) + ", ")


#### Day 2 ####

## No exercises listed (didn't see any)

#### Day 3 ####

## Exercise: Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

firstName = input('Enter your first name: ')
middleName = input('Enter your middle name: ')
lastName = input('Enter your last name: ')
print('Hello', firstName + " " + middleName + " " + lastName)

## Exercise: Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

favNumber = input('What\'s your favorite number?')
print('May I suggest a bigger amd better favorite number:', str(int(favNumber) + 1) + "?")

## Exercise:Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
# WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!

question = input('What do you want?')
print('WHADDAYA MEAN \"' + question.upper() + '?!? YOU\'RE FIRED!!')

## Exercise:Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
# Table of Contents
# Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

print("Table of Contents \n"  
+ "Chapter 1 ".ljust(1) + "Getting Started ".center(80) + "page1 ".rjust(10) + "\n"
+ "Chapter 2 ".ljust(1) + "Numbers".center(72) + "page9".rjust(17) + "\n"
+ "Chapter 3".ljust(1) + "Letters".center(73) + "page13".rjust(18)
)

## Exercise: Research how to generate a random number with Python.

import random
print("Random number: " + str(random.randint(1,101)))

#### Day 4 ####

## Exercise: “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”

x = 99
while x >= 0:
    if x > 1:
        print (str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer. \nTake one down and pass it around, " + str(x-1) + " bottles of beer on the wall.")
    if x == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer. \nTake one down and pass it around, no more bottles of beer on the wall.")
    if x == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.")
    x -= 1

## Exercise: Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL!
# unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back: NO, NOT SINCE 1938!
# Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. Change your previous program so that you have to shout BYE three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.

toGrandMa = input("What do you want to say to Grandma?")

if toGrandMa.islower() or toGrandMa == "BYE":
    print("HUH?! SPEAK UP, GIRL!")
if toGrandMa.isupper() and toGrandMa != "BYE" and toGrandMa != "BYE BYE BYE":
    print("NO, NOT SINCE " + str(random.randint(1930,1950)) + "!")
if toGrandMa == "BYE BYE BYE":
    print("Bye")

## Exercise: Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

startingYear = input("What is the starting year?")
endingYear = input("What is the ending year?")
for x in range (int(startingYear), int(endingYear)):
    if x %4 == 0:
        if x % 100 != 0 or (x % 100 == 0 and x % 400 == 0):
            print(str(x))
    x += 1

## Exercise: Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.

buildingFloorsNum = input("How many floors are there in this building?")
if int(buildingFloorsNum) <= 2 and int(buildingFloorsNum) > 0:
    print("This is a house of " + str(buildingFloorsNum) + " floors!")
if int(buildingFloorsNum) > 2 and int(buildingFloorsNum) <= 8:
    print("This is a medium building of " + str(buildingFloorsNum) + " floors!")
if int(buildingFloorsNum) > 8:
    print("This is a scycraper of " + str(buildingFloorsNum) + " floors!")
if int(buildingFloorsNum) <= 0: 
    print("Give a realistic number!")

## Exercise: Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?
# Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it!

text = ""
textList = []
while text != " ":
  text = input("Write words")
  textList.append(text)
  print(textList)
result = " ".join(sorted(textList))
print(result)

## Exercise: Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.

tableOfContent = ["Table of Contents", "Chapter 1", "Getting Started", "page 1", "Chapter 2", "Numbers", "page 9", "Chapter 3", "Letters", "page 3"]

print(tableOfContent[0] + "\n" + tableOfContent[1].ljust(1) + tableOfContent[2].center(80) + tableOfContent[3].rjust(10) + "\n" + tableOfContent[4].ljust(1) + tableOfContent[5].center(72) + tableOfContent[6].rjust(18) + "\n" + tableOfContent[7].ljust(1) + tableOfContent[8].center(72) + tableOfContent[9].rjust(18))

## Exercise: Write a function that prints out "moo" n times.

def printMoo(n):
    print("moo "*n)

printMoo(n=3)

## Exercise: Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
# Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers.
# Hint: Use the integer division and modulus methods.
# For reference, these are the values of the letters used: I = 1 V = 5 X = 10
# L = 50 C = 100 D = 500 M = 1000

def old_roman_numeral(input):
    ints = (1000,500,100,50,10,5,1)
    nums = ('M','D','C','L','X','V','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

print(old_roman_numeral(input=9))        

## Exercise:“Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.

def roman_numeral(input):
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

print(roman_numeral(input=4)) 