### imports
from random import randint

### ---------------------- Day 1
# Write a program that tells you the following:
# Hours in a year. How many hours are in a year?
def hoursInYear():
    return(24*36525/100) # use div by 100 to avoid float

print(hoursInYear())
# Minutes in a decade. How many minutes are in a decade?
def minutesInDecade():
    return(60*24*36525*10/100)

print(minutesInDecade())
# Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
def ageInSecondsFromYear(input):
    try:
        age = int(input)
        return(int(60*60*24*36525*age/100))
    except ValueError:
        print("That's not a number!")
    if not 0 < x < 130:
        print("Try a valid human age")

print(ageInSecondsFromYear(39))

# Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.

def ageInYearsFromSeconds(input):
    try:
        seconds = int(input)
        return(int(seconds*100/(60*60*24*36525)))
    except ValueError:
        print("That's not a number!")
    if not x > 0:
        print("Try a valid human age")

print(ageInYearsFromSeconds(48618000))


# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# How about a 64-bit system?
# not sure, from wikipedia - assume these could be seconds??
# 32 bits: maximum representable value 232 − 1 = 4294967295
# 64 bits: maximum representable value 264 − 1 = 18446744073709551615
def calcDaysToTimeout(input):
    try:
        seconds = int(input)
        return(int(seconds/(60*60*24)))
    except ValueError:
        print("something bad happened with this number of seconds")

print(calcDaysToTimeout(4294967295))
print(calcDaysToTimeout(18446744073709551615))
#49710
#213503982334601

# Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.

from datetime import datetime

def calcAccurateSeconds():
    birthdate = input("Enter your bithdate like YYYY-MM-DD: ")
    try:
        bd = datetime.strptime(birthdate, "%Y-%m-%d")
        now = datetime.now()
        print("You are ", abs((now- bd).days)*24*60*60, "seconds old")
    except ValueError:
        print("Try again, remember the format is YYYY-MM-DD")

calcAccurateSeconds()

### ---------------------- Day 2
# no questions

### ---------------------- Day 3

## Input Methods
### Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.
def fullNameGreet():
    first = input("What is your first name? ")
    middle = input("What is your middle name? ")
    last = input("What is your last name? ")
    fullname = str(first) + ' ' + str(middle) + ' ' + str(last)
    print("Hallo, ", fullname.title())

fullNameGreet()
### Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
def betterFavNumber():
    current = input("What is your favorite number? ")
    try:
        x = int(current)
        print("Might I suggest that you try on", x+1, "as your new favorite?")
    except ValueError:
        print("Please try again")

betterFavNumber()

## Fancy String Methods
### Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
### WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!

def angryBoss():
    want = input("WHADDYA WANT NOW? ")
    try:
        print("WHADDAYA MEAN \"{}\"?!? YOU'RE FIRED!!".format(want.upper()))
    except:
        print("COME BACK LATER")
angryBoss()

### Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
#Table of Contents
#
#Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13
## does not look formatted for me. Skipping

### ---------------------- Day 4

## Looping
# “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
def beerOnWall():
    for i in range(100):
        if i == 99:
            print("No more beer")
        else:
            print(99-i, "Bottles of Beer on the Wall")
beerOnWall()

# Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL! unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back: NO, NOT SINCE 1938! To make your program really believable, have Grandma shout a different year each time, maybe any year at random between 1930 and 1950. (This part is optional and would be much easier if you read the section on Python’s random number generator under the Math Object.) You can’t stop talking to Grandma until you shout BYE.

def deafGrandma():
    say = ""
    while say != "BYE BYE BYE":
        say = input("What do you want to say to Grandma?")
        if say.isupper() == 0:
            print('HUH?! SPEAK UP, GIRL!')
        elif say == "BYE BYE BYE":
            print('STAY FOR CAKE? OK BYE, GIRL!')
        else:
            x = randint(0,20)
            print('NO, NOT SINCE ',1930+x,'!')

deafGrandma()

## Lists

# Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second? Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it!
def sortWords():
    words = []
    while True:
        word = input()
        if len(word)>0:
            words.append(word)
        else:
            break
    words = sorted(words)
    print("\n".join(words))

sortWords()

# Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.
def tableOfContents():
    vital = ["Vital", "Not", "Vital", "Not", "Vital", "Vital"]
    chapters = ["Introduction", "Background", "Methods", "Data", "Findings", "Recommendations"]
    pages = ["1", "18", "32", "54", "78", "89"]
    print("Table of Contents".center(32, ' '))
    for i in range(len(vital)):
        print("{:<10}{:<20}{:>2}\n".format(vital[i], chapters[i], pages[i]))

tableOfContents()
## Write Your Own Functions
# Write a function that prints out "moo" n times.

def moo(n):
    for i in range(n):
        print("moo")

moo(10)

## Return Values
# Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense. No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
# Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers. Hint: Use the integer division and modulus methods. For reference, these are the values of the letters used: I = 1 V = 5 X = 10  L = 50 C = 100 D = 500 M = 1000
def oldRoman(input):
    try:
        x = int(input)
        vals = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        romans = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = []
        for i in range(len(vals)):
            count = int(x / vals[i])
            result.append(romans[i] * count)
            x -= vals[i] * count
        print(''.join(result))
        return
    except ValueError:
        print("That's not an int!")
    if not 0 < x < 4000:
        print("number must be between 1 and 3999")


oldRoman(234)
oldRoman(5)

# “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
def newRoman(input):
    try:
        x = int(input)
        vals = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        romans = ('M',  'MC', 'D', 'DC','C', 'XC','L','LX','X','XI','V','VI','I')
        result = []
        for i in range(len(vals)):
            count = int(x / vals[i])
            result.append(romans[i] * count)
            x -= vals[i] * count
        print(''.join(result))
        return
    except ValueError:
        print("That's not an int!")
    if not 0 < x < 4000:
        print("number must be between 1 and 3999")


newRoman(234)
newRoman(5)
