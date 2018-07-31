### Week 1 Day 1 Homework

## Question 1: Hours in year?
print("Hours in Common Year: ", 365 * 24)
print("Hours in Leap Year: ", 366 * 24)

## Question 2: Minutes in decade?
print("Minutes in Decade: ", (8 * 365 + 2 * 366) * 24 * 60)

## Question 3: Age in seconds?
print("My Age in Seconds: ", 19 * 365 * 24 * 60 * 60)

## Question 4: 48618000 seconds to years?
print("Andreea Visanoiu​ age: ", 48618000 /60/60/24/365)

## Question 5: How many days does it take for a 32-bit 
## system to timeout, if it has a bug with integer overflow?
print ("32-bit system timeout days: ", round((2**32)/1000/60/60/24))

## Question 6: 64-bit system?
print ("64-bit system timeout days: ", round((2**64)/1000/60/60/24))

## Question 7: Calculate exact age based on DOB?
import datetime as dt

dob = dt.date(1999,1,23)
year = str(dt.date.today().year - dob.year)
month = str(dt.date.today().month - dob.month)
day = str(dt.date.today().day - dob.day)

print("I'm",year,"years",month, "months", day, "days old.", sep=" ")

### Week 1 Day 3 Homework

## Question 1: Write a program that asks for a person’s first name, 
## then middle, and then last. Finally, it should greet the person 
## using their full name
first_name = input("FirstName: ")
middle_name = input("MiddleName: ")
last_name = input("LastName: ")
print("Hi", first_name, middle_name, last_name, sep=" ")

## Question 2: Write a program that asks for a person’s favorite number. 
## Have your program add 1 to the number, and then suggest the result 
## as a bigger and better favorite number.
try:
	fav_number = int(input("Favourite Number: "))
	print("A better and bigger favourite number can be ",fav_number+1)
except:
	print("Not A Number")

## Question 3: Write an angry boss program that rudely asks what you 
## want. Whatever you answer, the angry boss should yell it back to you 
## and then fire you.
answer = input("What do you want? ")
print("WHADDAYA MEAN \"" + answer.upper() + "\"?!? YOU'RE FIRED!!")

## Question 4: write a program that will display a table of contents.
print("Table of Contents".center(50,'_'),end="\n\n")
chapter = []
page = []
chapter += ["Chapter 1: Getting Started".ljust(25,'.')]
chapter += ['Chapter 2: Numbers'.ljust(25,'.')] 
chapter += ['Chapter 3: Letters'.ljust(25,'.')]
page += ['page 1'.rjust(25,'.')] 
page += ['page 9'.rjust(25,'.')] 
page += ['page 13'.rjust(25,'.')] 

for i in range(3):
	print(chapter[i] + page[i])

### Week 1 Day 4

## Question 1: print lyrics of "99 Bottles of Bear"
n = 99
for i in range(n,-1,-1):
	if i > 1:
		print(i," bottles of beer on the wall, ",i," bottles of beer.")
		print("Take one down and pass it around, ",i-1," bottles of beer on the wall.", end="\n\n")
	elif i > 0:
		print(i," bottles of beer on the wall, ",i," bottles of beer.")
		print("Take one down and pass it around, no more bottles of beer on the wall.", end="\n\n")

	elif i == 0:
		print("No more bottles of beer on the wall, no more bottles of beer.") 
		print("Go to the store and buy some more, ",n," bottles of beer on the wall.")

## Question 2: deaf grandma
import random

count_bye = 0
while True:
	you = input("You: ")
	if you != you.upper():
		print("HUH?! SPEAK UP, GIRL!")
	else:
		if you in 'BYE':
			count_bye += 1
			if (count_bye < 3):
				print("HUH?! SPEAK UP, GIRL!")
			else:
				break
		else:
			print("NO, NOT SINCE", random.randint(1930,1950))
			count_bye = 0

## Question 3: Leap Year
start_year = int(input("Starting Year: "))
end_year = int(input("Ending Year: "))

print("Leap Years in between")

for i in range(start_year, end_year+1):
	if i % 100 == 0 and i % 400 == 0:
		print(i)
	elif i % 4 == 0:
		print(i)

## Question 4: Building and sorting an array. Write the program 
## that asks us to type as many words as we want (one word per line, 
## continuing until we just press Enter on an empty line) and then 
## repeats the words back to us in alphabetical order.
words = []
while True: 
	word = input("Input a word: ")
	if word != "":
		words.append(word)
	else:
		break

print("Sorted Words:")
sorted_words = sorted(words)
for word in sorted_words:
	print(word)

## Question 5: Table of Contents
print("Table Of Contents".center(50,'_'))

chapters = []
pages = []
for i in range(10):
	chapters += [("Chapter " + str(i)).ljust(25,'.')]
	pages += [("page " + str(i)).rjust(25,'.')]

for i in range(10):
	print(chapters[i] + pages[i])

## Question 6: Write a function that prints out "moo" n times.
def moo(n):
	for i in range(n):
		print("moo")
moo(3)

## Question 7: Old School Roman numerals
# I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
def old_roman_numeral(num):
	roman_string = ''
	while num > 0:
		if num >= 1000:
			roman_string += 'M'
			num -= 1000
		elif num >= 500:
			roman_string += 'D'
			num -= 500
		elif num >= 100:
			roman_string += 'C'
			num -= 100
		elif num >= 50:
			roman_string += 'L'
			num -= 50
		elif num > 10:
			roman_string += 'X'
			num -= 10
		elif num >= 5:
			roman_string += 'V'
			num -= 5
		elif num >= 1:
			roman_string += 'I'
			num -= 1
	return roman_string

print(old_roman_numeral(4))

## Question 8: Modern Roman Numeral
def modern_roman_numeral(num):
	numeral_value = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
	numeral_symbol = ('M','CM','D','CD','C','XC','L','XL','X','IX',
		'V','IV','I')
	roman_string = ""
	for i in range(len(numeral_value)):
		count = int(num / numeral_value[i])
		roman_string += numeral_symbol[i] * count
		num -= numeral_value[i] * count

	return roman_string

print(modern_roman_numeral(4))














