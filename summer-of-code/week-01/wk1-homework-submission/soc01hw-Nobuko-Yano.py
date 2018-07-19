#### Day 1 homework
from datetime import datetime,timedelta

# Hours in a year. How many hours are in a year?
print("Hours in a year is:")
print(365*24)

# Minutes in a decade. How many minutes are in a decade?
print("Minutes in a decade is:")
print(10*365*24*60)

# Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
# ignore leap year, focus only years.(igonore less than 1 year)
print("I am "+str(60*60*24*365*38)+" seconds old.")

# Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print("Andreea Visanoiu​ is "+str(48618000/(60*60*24*365))+" years old.")
# she may forgot to mulitiply 24 ?? then she is 37 years old.

# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
base = datetime(1970,1,1,00,00,00,000000)
integer32 = (2**31)-1
limit = base + timedelta(seconds=integer32)
print("32 bit integer becomes overflow at "+str(limit))
print("it takes "+str(integer32/(24*60*60))+" days from 2018.07.19")

# How about a 64-bit system?
integer64 = (2**63)-1
years=int(integer64/(365*24*60*60))+1970
#rest_seconds=integer64 - years*60*60*24*365
#limit = base + timedelta(days=years*365) ==>overflow :/
#limit = base + timedelta(seconds=rest_seconds)
print("64 bit integer becomes overflow "+str(years)+" years later")


# Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.
today = datetime.now()
birthday = datetime(1979,8,31,12,00,00,000000)
age = today - birthday
#print(age) ==>14202 days, 2:40:00.300639
age_in_seconds = age.days*24*60*60+age.seconds 
print("I am "+str(age_in_seconds)+" seconds old")


#### Day 3 homework
# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.
firstname=input("please input your first name:")
lastname=input("please input your last name:")
print("Hello, "+ firstname+" "+lastname+"!!")

# Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
favorite_number=input("please input your favorite number: ")
bigger_number = int(favorite_number)+1
print(str(bigger_number) + " is bigger and better!!")

# Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
# WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
request=input("please input your request here: ")
print("WHADDAYA MEAN \""+request+"\"?!? YOU\'RE FIRED!!")

# Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:

title="Table of Contents"
capter="Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13"

print(title.ljust(80))
print(capter.center(85))
