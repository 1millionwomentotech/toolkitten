# # Summer of Code - Week 1
# # Day 1
# ###### https://github.com/mswann11/toolkitten/blob/master/summer-of-code/week-01/day1.md
# ### Numbers

import math
import string
import os
import datetime
import random

# Hours in a year. How many hours are in a year?
print(365*24)


# Minutes in a decade. How many minutes are in a decade?
print(10*365*24*60)


# Your age in seconds. How many seconds old are you? 
print(((37*365)+(28-11)+31+30+31+30+20)*24*60*60)


# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
print(math.ceil(((((2**32)/1000)/60)/60)/24))


# How about a 64-bit system?
print(math.ceil(((((2**64)/1000)/60)/60)/24))


# Calculate your age accurately based on your birthday 
# (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday)
# You will need Python modules.
x = datetime.datetime.now()
print("Now: " + str(x))
y = datetime.datetime(1981, 2, 11, 6, 30)
print("Birthday: " + str(y))
z = x-y
seconds = z.days*24*60*60 + z.seconds
years = seconds/60/60/24/365
print("You are " + str(round(years,2)) + " years old!")
days = z.days
print("You are " + str(days) + " days old!")
hours = z.days*24
print("You are " + str(hours) + " hours old!")
minutes = z.days*24*60
print("You are " + str(minutes) + " minutes old!")
seconds = z.days*24*60*60 + z.seconds
print("You are " + str(seconds) + " seconds old!")


# # Day 2
# ###### https://github.com/mswann11/toolkitten/blob/master/summer-of-code/week-01/day2.md
# ### Letters, Variables
# No exercises assigned.


# # Day 3
# ###### https://github.com/mswann11/toolkitten/blob/master/summer-of-code/week-01/day3.md
# ### Love Affair between Numbers and Letters

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. 
# Finally, it should greet the person using their full name.
firstName = input("Please enter your first name: ")
middleName = input("Please enter your middle name: ")
lastName = input("Please enter your last name: ")
print("Hello, " + firstName + " " + middleName + " " + lastName + "! " + "It's very nice to meet you!")


# Bigger, better favorite number. Write a program that asks for a person’s favorite number. 
# Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number.
favoriteNumber = int(input("What is your favorite number? "))
favoritePlusOne = favoriteNumber + 1
print(str(favoriteNumber) + " is a good number, but don't you think " + str(favoritePlusOne) + " is better?")


# Angry boss. Write an angry boss program that rudely asks what you want. 
# Whatever you answer, the angry boss should yell it back to you and then fire you. 
# For example, if you type in I want a raise, it should yell back like this:
# WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
answer = input("WHAT DO YOU WANT?!? ")
print("WHADDAYA MEAN \""+ answer.upper() + "\"?!? YOU'RE FIRED!!")


# Table of contents. Here’s something for you to do in order to play around more with center, 
# ljust, and rjust: write a program that will display a table of contents so that it looks like this:
# Table of Contents
# Chapter 1: Getting Started      page 1 
# Chapter 2: Numbers              page 9 
# Chapter 3: Letters              page 13
title = "Table of Contents"
chapterNames = ["Getting Started", "Numbers", "Letters"]
pageNumbers = ["page 1", "page 9", "page 13"]
for x in range (1,4):
    chapter = "Chapter " + str(x) + ":"
    print(chapter.ljust(12, " ") + chapterNames[x-1].ljust(30," ") + pageNumbers[x-1].ljust(10, " "))


# # Day 4
# ###### https://github.com/mswann11/toolkitten/blob/master/summer-of-code/week-01/day4.md
# ### Looping

# Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
title = "99 Bottles of Beer on the Wall\n"
lyricLineOne = " bottles of beer on the wall, "
lyricLineTwo = " bottles of beer! "
lyricLineThree = "Take one down, pass it around, "
lyricLineFour = " bottles of beer on the wall!"
print(title.center(100, " "))
for x in range(99,90,-1):
    print(str(x) + lyricLineOne + str(x) + lyricLineTwo + lyricLineThree + str(x-1) + lyricLineFour)


# Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: 
#   HUH?! SPEAK UP, GIRL!,
# unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:
#   NO, NOT SINCE 1938!
# To make your program really believable, have Grandma shout a different year each time, 
# maybe any year at random between 1930 and 1950. 
# You can’t stop talking to Grandma until you shout BYE.
answer = input("What do you have to say? ")
while answer != "BYE":
    if answer.isupper():
        print("NO, NOT SINCE "+ str(random.randint(1938,1950)) + "!")
        answer = input("What else do you have to say? ")
    else:
        answer = input("HUH?! SPEAK UP, GIRL! ")
print("OH OKAY, BYE-BYE HONEY!")


# Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. 
# Change your previous program so that you have to shout BYE three times in a row. 
# Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.
answer = input("What do you have to say? ")
byeCount = 0
while byeCount != 2:
    if (answer == "BYE"):
        byeCount += 1
        answer = input("")
    elif answer.isupper():
        byeCount = 0
        print("NO, NOT SINCE "+ str(random.randint(1938,1950)) + "!")
        answer = input("What else do you have to say? ")
    else:
        byeCount = 0
        answer = input("HUH?! SPEAK UP, GIRL! ")
print("OH OKAY, BYE-BYE HONEY!")


# Leap years. Write a program that asks for a starting year and an ending year and then puts 
# all the leap years between them (and including them, if they are also leap years). 
# Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years 
# (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). 
# What a mess!
startingYear = int(input("Enter starting year: "))
endingYear = int(input("Enter ending year: "))
leapYears = "Leap years: "
for y in range(startingYear, endingYear + 1):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                leapYears += str(y) + " "
        else:
            leapYears += str(y) + " "
print(leapYears)


# Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. 
# Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, 
# kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.
# Bookshelf with 6 shelves, each shelf is 3 feet wide, average width of each book is 1.5 inches. 
# How many books can the bookshelf hold?
width = 3*12
totalSpace = width*6
books = int(totalSpace/1.5)
print("The bookshelf can hold " + str(books) + " books.")


# ### Lists

# Building and sorting an array. Write the program that asks us to type as many words as we want 
# (one word per line, continuing until we just press Enter on an empty line) and then repeats the words 
# back to us in alphabetical order. Make sure to test your program thoroughly; for example, 
# does hitting Enter on an empty line always exit your program? Even on the first line? And the second?
words = []
newWord = input("Enter words to add to your word list:\n")
while(newWord != ""):
    words.append(newWord)
    newWord = input()
if len(words) == 0:
    print("Your word list is empty.")
else:
    words.sort()
    wordList = ""
    for w in words:
        wordList += w + " "
    print("Your sorted word list: " + wordList)


# Table of contents. Write a table of contents program here. Start the program with a list holding all 
# of the information for your table of contents (chapter names, page numbers, and so on). 
# Then print out the information from the list in a beautifully formatted table of contents. 
# Use string formatting such as left align, right align, center.
title = "Table of Contents"
chapters = [["Chapter 1:","Getting Started","page 1"],
            ["Chapter 2:","Numbers","page 9"],
            ["Chapter 3:","Letters","page 13"]]
for c in chapters:
    print(c[0].ljust(12, " ") + c[1].ljust(20, " ") + c[2].rjust(20, " "))


# ### Functions

# Write a function that prints out "moo" n times.
def printMoo(n):
    for x in range(n):
        print("moo ")
n = int(input("Pick a number: "))
printMoo(n)


# Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother 
# with any of this new-fangled subtraction “IX” nonsense.
# No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
# Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing 
# the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. 
# Make sure to test your method on a bunch of different numbers.
# Hint: Use the integer division and modulus methods.
# For reference, these are the values of the letters used: 
# I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
number = int(input("Enter a number to convert to Roman numerals: "))

def getThousand(n):
    m = ""
    r = n
    if(n>=1000):
        m_as_int = int(n/1000)
        r = n % 1000
        for j in range(m_as_int):
            m += "M"
    return (m,r)

def getFiveHundred(n):
    d = ""
    r = n
    if(n>=500):
        d_as_int = int(n/500)
        r = n % 500
        for j in range(d_as_int):
            d += "D"
    return (d,r)

def getHundred(n):
    c = ""
    r = n
    if(n>=100):
        c_as_int = int(n/100)
        r = n % 100
        for j in range(c_as_int):
            c += "C"
    return (c,r)

def getFifty(n):
    l = ""
    r = n
    if(n>=50):
        l_as_int = int(n/50)
        r = n % 50
        for j in range(l_as_int):
            l += "L"
    return (l,r)

def getTen(n):
    x = ""
    r = n
    if(n>=10):
        x_as_int = int(n/10)
        r = n % 10
        for j in range(x_as_int):
            x += "X"
    return (x,r)

def getFive(n):
    v = ""
    r = n
    if(n>=5):
        v_as_int = int(n/5)
        r = n % 5
        for j in range(v_as_int):
            v += "V"
    return (v,r)

def getOne(n):
    i = ""
    for j in range(n):
        i += "I"
    return i
        

(thousand,remainderM) = getThousand(number)
(fiveHundred,remainderD) = getFiveHundred(remainderM)
(hundred,remainderC) = getHundred(remainderD)
(fifty,remainderL) = getFifty(remainderC)
(ten,remainderX) = getTen(remainderL)
(five,remainderV) = getFive(remainderX)
one = getOne(remainderV)

roman = thousand + fiveHundred + hundred + fifty + ten + five + one
print("Conversion: " + roman)


# “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting 
# a smaller number before a larger one meant you had to subtract the smaller one. 
# As a result of this development, you must now suffer. 
# Rewrite your previous method to return the new-style Roman numerals
# so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
number = int(input("Enter a number to convert to Roman numerals: "))

def getThousand(n):
    m = ""
    r = n
    c = ""
    if(n>=1000):
        m_as_int = int(n/1000)
        r = n % 1000
        for j in range(m_as_int):
            m += "M"
    if(r>=900):
        c = "CM"
        r = r-900
    return (m,r,c)

def getFiveHundred(n):
    d = ""
    r = n
    c = ""
    if(n>=500):
        d_as_int = int(n/500)
        r = n % 500
        for j in range(d_as_int):
            d += "D"
    if(r>=400):
        c = "CD"
        r = r-400
    return (d,r,c)

def getHundred(n):
    c = ""
    r = n
    x = ""
    if(n>=100):
        c_as_int = int(n/100)
        r = n % 100
        for j in range(c_as_int):
            c += "C"
    if(r>=90):
        x = "XC"
        r = r-90
    return (c,r,x)

def getFifty(n):
    l = ""
    r = n
    x = ""
    if(n>=50):
        l_as_int = int(n/50)
        r = n % 50
        for j in range(l_as_int):
            l += "L"
    if(r>=40):
        x = "XL"
        r = r-40
    return (l,r,x)

def getTen(n):
    x = ""
    r = n
    i = ""
    if(n>=10):
        x_as_int = int(n/10)
        r = n % 10
        for j in range(x_as_int):
            x += "X"
    if(r==9):
        i = "IX"
        r = 0
    return (x,r,i)

def getFive(n):
    v = ""
    r = n
    i = ""
    if(n>=5):
        v_as_int = int(n/5)
        r = n % 5
        for j in range(v_as_int):
            v += "V"
    if(r==4):
        i = "IV"
        r = 0
    return (v,r,i)

def getOne(n):
    i = ""
    for j in range(n):
        i += "I"
    return i

(thousand,remainderM,mNegC) = getThousand(number)
(fiveHundred,remainderD,dNegC) = getFiveHundred(remainderM)
(hundred,remainderC,cNegX) = getHundred(remainderD)
(fifty,remainderL,lNegX) = getFifty(remainderC)
(ten,remainderX,xNegI) = getTen(remainderL)
(five,remainderV,vNegI) = getFive(remainderX)
one = getOne(remainderV)

roman = thousand + mNegC + fiveHundred + dNegC + hundred + cNegX + fifty + lNegX + ten + xNegI + five + vNegI + one
print("Conversion: " + roman)