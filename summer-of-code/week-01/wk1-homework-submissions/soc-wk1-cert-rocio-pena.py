#1millionwomentotech Summer of Code
#Rocio Pena / rocio-gold#4215
#Please run with python 3

from datetime import datetime, timedelta, date
from calendar import calendar
from random import random, randint

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
input("\nPlease press enter to continue ")
print("\n============A Few Things to Try - Week01 Day03============")

#Full name greeting. Write a program that asks for a person's first name, then middle, and then last. 
#Finally, it should greet the person using their full name.
first_name = input("Please enter your first name: ")
middle_name = input("Thanks. Now, please enter your middle name: ")
last_name = input("Great. Finally please enter your last name: ")

print("Welcome onboard dear", first_name, middle_name, last_name, "\n")


#Bigger, better favorite number. Write a program that asks for a person's favorite number. 
#Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. 
#(Do be tactful about it, though.)
favourite_number =  input("Please enter your favourite number: ")
print(favourite_number, "is a great number. But what about", int(favourite_number) + 1, ", don't you think it's a better number?\n")

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
input("\nPlease press enter to continue ")
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

input("\nPlease press enter to continue ")
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


#---------------Week01 Day04------------------------------------------------
print("\n============A Few Things to Try - Week01 Day04============")

# "99 Bottles of Beer on the Wall." Write a program that prints out the lyrics to that beloved classic" 
input("Ready for the lyrics of 99 Bottles of Beer on the Wall? Please press enter ")
print("\n")
counter = 99
while (counter > -1):
	if counter > 1:
		print(counter, "bottles of beer on the wall,", counter, "bottles of beer.")	
		print("Take one down and pass it around,", counter - 1, "bottles of beer on the wall.\n")
	elif counter == 1:
		print("1 bottle of beer on the wall, 1 bottle of beer.")
		print("Take one down and pass it around, no more bottles of beer on the wall.\n")
	else:
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 99 bottles of beer on the wall.\n")
	counter -= 1

# Deaf grandma. Whatever you say to Grandma (whatever you type in), 
# she should respond with this: HUH?! SPEAK UP, GIRL!
# unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:
# NO, NOT SINCE 1938! or random year between 1930 and 1950
print("\n=== Talk to your Grandma - Deaf Grandma ===")

message = ''
while True:
	message = input("Please say something to Grandma: ")
	if message == "BYE":
		break
	if message.isupper():
		rand_number = randint(1930, 1950)
		print("NO, NOT SINCE " + str(rand_number) + "!")
	else:
		print("HUH?! SPEAK UP, GIRL!") 

print("OK, Bye for now")


#Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them 
#(and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). 
#However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 
#(such as 1600 and 2000, which were in fact leap years). What a mess!

print("\n=== Leap Years ===")

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

start = 0
end = 0
leap_years = []
while True:
	start = int(input("Please enter starting year: "))
	end = int(input("Please enter ending year: "))
	if end > start:
		break
	else:
		print("End year must be greater than starting year. Please try again: ")

for year in range(start, end):
	if is_leap_year(year):
		leap_years.append(year)

print("\nThese are the leap years between", start, "and", end, ":", leap_years)


# Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. 
# Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, 
# dogs, estimate your books by bookshelf, toiletries, wardrobe. 
# I'll count the amount of hours I'll work in 2018 with the following roster:
# 1) Working days: Monday to Friday, no weekends.
# 2) Working hours: 7.5 hrs every day 
# 3) Exceptions:
#    - the first day of each month an extra 2.5 hrs if it's a weekday
#    - every other Tuesday 3.5hrs training starting 02/Jan, not counted as part of my working hours - no training during vacation
#    - 2 weeks planned vacation from 29 Oct until 09 Nov, not part of my working hours

print("\n=== Personalized Counting - Working hours this year ===") 
print("\n=== 2018 working hours with schedule ===")
start_date = date(2018, 1, 1)
end_date = date(2018, 12, 31)
vac_start = date(2018, 10, 29)
vac_end = date(2018, 11, 9) 
hours = 0.0
tuesday_counter = 0 #variable to check every two Tuesdays, I'll take all odd occurrences

while start_date <= end_date:
	if start_date >= vac_start and start_date <= vac_end: #on holidays, yay!!!
		start_date = start_date + timedelta(days=1)
		continue
	if start_date.weekday() > 0 and start_date.weekday() < 6: # between Monday and Friday
		hours += 7.5
		if start_date.day == 1:
			hours += 2.5
		if start_date.weekday() == 2: #Tuesday
			tuesday_counter += 1
			if tuesday_counter % 2 != 0: #take this as training day
				hours -= 3.5
	start_date = start_date + timedelta(days=1)

print("My total working hours in 2018 is:", hours)



print("\n=== Talk to your Grandma - Deaf Grandma extended ===")

message = ''
bye_counter = 0
while True:
	if bye_counter == 3:
		break
	message = input("Please say something to Grandma: ")
	if message == "BYE":
		bye_counter += 1
		continue
	if message.isupper():
		rand_number = randint(1930, 1950)
		print("NO, NOT SINCE " + str(rand_number) + "!")
	else:
		print("HUH?! SPEAK UP, GIRL!") 
	bye_counter = 0
print("OK, Bye for now")



print("\n=== Sorting an array ===")
# Building and sorting an array. Write the program that asks us to type as many words as we want 
# (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us 
# in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line 
# always exit your program? Even on the first line? And the second?
# Hint: There's a lovely array method that will give you a sorted version of an array: sorted(). Use it!

print("Please enter as many words as you want, one on each line. To end press enter ")

array_words = []
while True:
	new_word = input()
	if new_word == "": break
	else: array_words.append(new_word)
if len(array_words) > 0: print("This is your ordered array", sorted(array_words))
else: print("Sorry, your array was empty.")



print("\n=== Table of contents ===")
#Table of contents. Write a table of contents program here. Start the program with a list holding all of the information 
#for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a 
#beautifully formatted table of contents. Use string formatting such as left align, right align, center.
content = [["Exercise 0", "The Setup", 7],
		   ["Exercise 1", "A Good First Program", 9],
		   ["Exercise 2", "Comments And Pound Characters", 15],
		   ["Exercise 3", "Numbers And Math", 16],
		   ["Exercise 4", "Variables And Names", 22],
		   ["Exercise 5", "More Variables And Printing", 24],
		   ["Exercise 6", "Strings And Text", 27],
		   ["Exercise 7", "More Printing", 35],
		   ["Exercise 8", "Printing, Printing", 40],
		   ["Exercise 9", "Printing, Printing, Printing", 49],
		   ["Exercise 10", "What Was That?", 55]]

print("\nTable of Contents")
for i in range (len(content)):
	print((content[i][0] + ": " + content[i][1]).ljust(55) + "page " + str(content[i][2]))



print("\n=== Function to print a word x number of times ===")
#Write a function that prints out "moo" n times.
def print_n_times(word, times):
	new_word = ''
	for i in range(times):
		new_word += " " + word
	return new_word
text = input("Please enter the word you want to repeat: ")
times = input("How many times do you want to repeat this word? ")
print(print_n_times(text, int(times)))



print("\n=== Old School Romans ===")

def convert_to_old_roman(value): 
   decimals = (1000, 500, 100 , 50,  10,  5,  1)  #Decimal conversion
   romans =   ('M',  'D', 'C',  'L', 'X','V','I') #Possible symbols
   result = ""
   for i in range(len(decimals)):
      count = int(value / decimals[i]) #How many times I need each of the symbols?
      result += romans[i] * count      #Add the symbol 'count' times
      value -= decimals[i] * count     #Decrease the value to keep adding symbols
   return result

while True:
	value = input("Enter a number to convert to Old Romans (enter to finish): ")
	if value == '':
		break
	else:
		print(convert_to_old_roman(int(value)))



print("\n=== Modern Romans ===")

def convert_to_roman(value): 
   decimals = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)  #Decimal conversion
   romans =   ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I') #Possible symbols
   result = ""
   for i in range(len(decimals)):
      count = int(value / decimals[i]) #How many times I need each of the symbols?
      result += romans[i] * count      #Add the symbol 'count' times
      value -= decimals[i] * count     #Decrease the value to keep adding symbols
   return result

while True:
	value = input("Enter a number to convert to Modern Romans (enter to finish): ")
	if value == '':
		break
	else:
		print(convert_to_roman(int(value)))


print("\n*********** End Exercises Week 01 ***********")



