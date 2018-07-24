### DAY - 1 ###

# Hours in a year
print("1. How many hours are there in a year?")
diy = 365
hid = 24
hours_in_year = diy * hid
print("Ans. There are",hours_in_year,"hours in a year.")

# Minutes in a decade
print("\n2. How many minutes are in a decade?")
years_in_decade = 10
min_in_hour = 60
min_in_decade = years_in_decade * diy * hid * min_in_hour
print("Ans. There are",min_in_decade,"minutes in a decade.")

# Your age in seconds
print("\n.3. How many seconds old are you?")

my_age = 24
age_in_sec = 24*diy*hid*min_in_hour*60
print("Age in seconds: ",age_in_sec)

#Andreea Visanoiu'age
print("\n4. I'm 48618000 seconds old. Calculate my age.  - @Andreea Visanoiu")
curr_age_in_sec = 48618000
age_in_yr = curr_age_in_sec/(60 * 60 * 24 * 365)
print("Ans. @Andreea's age is",age_in_yr)

#TOUGH QUESTIONS

#Timeout calculations
print("\nHow many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?")
totalIntFlow32 = (2**31-1)/(100*60*60*24) #Since it counts the time it has been running  in 1/100 of a second
print("Total days to timeout for 32 bit system: ", totalIntFlow32)
print("\nWhat about a 64 bit system?")
totalIntFlow64 = (2**63-1)/(100*60*60*24)
print("Total days to timeout for 64 bit system: ",totalIntFlow64)



#Calculate your age accurately based on your date of birth
import time
import datetime
from datetime import timedelta

curr_date = datetime.datetime.now()
print("\n6. Calculate your age accurately based on your birthday.")
date_entry = input('\nEnter your date of birth in YYYY-MM-DD format : ')
year,month,day = map(int, date_entry.split('-'))

try:
	time_entry = input('Enter the time of birth as HH:MM:SS format : ')
except KeyboardInterrupt:
	time_entry = "00:00:00"
except EOFError:
	time_entry = "00:00:00"
finally:
	hour, minute, second = map(int, time_entry.split(':'))

full_dob = datetime.datetime(year, month, day, hour, minute, second)
diff = curr_date - full_dob
age_in_sec = diff.total_seconds()
myyear = age_in_sec/(60*60*24*365)
mymonth = (myyear -int(myyear))*12
mydays = (mymonth - int(mymonth))*30
myhr = (mydays - int(mydays))*24
mymin = (myhr - int(myhr))*60
mysec = (mymin - int(mymin))*60
print("\nAns. My accurate age based on my birthday: {0}yrs {1}months {2}days {3}hrs {4}min {5:.2f}sec".format(int(myyear),int(mymonth),int(mydays),int(myhr),int(mymin),round(mysec,2)))

### DAY - 3 ###

#Full name greeting
print("Full name greeting")
fname = input("First name: ")
mname = input("Middle name: ")
lname = input("Last name: ")
full_name = fname + ' ' + mname + ' ' + lname
print("Hello,",full_name)

#Bigger, better favorite number
print("Favorite number")
num = input("Enter your favorite number: ")
bignum = int(num) + 1
print("The bigger better favorite number can be "+ str(bignum))

# Angry Boss
print("Angry boss's reply")
print("\nAngry Boss: What do you want??\n")
answer = input("Your answer: ")
reply = "WHADDAYA MEAN \""+ answer.upper() + "\"?!? YOU'RE FIRED!!"
print("\nAngry Boss replied, "+ reply)

# Random numbers generation

## DAY - 4 ##

#99 Bottles of Beer on the Wall
print("Lyrics of the classic - 99 Bottles of Beer on the Wall")
num = 99
while num != 0:
	print(str(num) + " Bottles of Beer on the Wall.")
	num-=1

# Deaf GrandMa + EXtended Deaf GrandMa Problem

import random
count = 0
while True:
	me = input("You: ")
	if me=='BYE':
		count += 1
		if count == 3: 
			break
	else:
		print("Consecutive BYE's:",count)
		count = 0
	if not me.isupper():
		grandma = "HUH?! SPEAK UP, GIRL!"
		print("GrandMa: " + grandma)
	else:
		year = random.randint(1930,1950)
		grandma = "NO, NOT SINCE "+str(year)+"!"
		print("GrandMa: " + grandma)

# Leap Years

print("Leap Years List")
start = int(input("Enter starting year:"))
end = int(input("Enter ending year:"))
leap = list()
while start<=end:
	if start%4==0:
		if ((start%100==0) and (start%400)!=0):
			start+=1
			continue	
		leap.append(start)
		start+=4
	else:
		start+=1
print(leap)

#Find something today in your life, that is a calculation.

import time
import random
import sys
print("Let's go to the zoo with family. It is 9.00am now.")
duration = 0
reply = ['Dad: \"Have patience.\"',
		'Dad: \"No.\"',
		'Dad: \"Not yet.\"',
		'Dad: \"We\'ll reach soon.\"'

]
while duration<=40:
	blah = "..... "
	if duration==0:
		duration +=10
		continue
	for l in blah:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(1)
	print("9:"+str(duration)+"am")
	time.sleep(1)
	print("You: \"Are we there yet?\"")
	time.sleep(2)
	if duration==40:
		print("Dad:\"Yes, I'm looking for a parking space.\"")
		break
	else:
		print(random.choice(reply))
		duration +=10
time.sleep(2)
print("You: \"Yipee!!  we finally got to the zoo.\"")

#Building and sorting an array
print("Building and sorting an array")
words = list()
while True:
	line = input()
	if line!='':
		words.append(line)
		continue
	break
words.sort()
print("After sorting : ")
print(words)

# Table of Content

print("Enter the table of contents")
content = list()
while True:
	chapter = input("Chapter name:")
	page = input("Page number:")
	hr = input("Credit hour:")
	content.append([chapter,int(page),int(hr)])
	choice = input("Is there more?(Y/N)")
	if choice=='N':
		break
print("\nTABLE OF CONTENTS\n")
print("{0:<20} {1:^20} {2:>20}".format("Chapter","Page number","Credit Hour"))
for x in content:
	print("{0:<20} {1:^20} {2:>20}".format(x[0],x[1],x[2]))

# Write a function that prints out "moo" n times. 

print("To print \"moo\" n times")
def say_moo(n):
	for i in range(n):
		print("moo")	
num = input("Enter the number of times \"moo\" is to be printed:")
say_moo(int(num))

# Old school Roman numerals

num_input = input("Enter an integer between 1 and 3000: ")
number = int(num_input)
roman = ""
def Rconvert(letter,value):
	rom = ""
	while value>0:
		rom+=letter
		value-=1
	return rom

while number!=0:
	if number>=1000:
		roman+=Rconvert("M",int(number/1000))
		number = number%1000
	elif number>=500:
		roman+=Rconvert("D",int(number/500))
		number = number%500
	elif number>=100:
		roman+=Rconvert("C",int(number/100))
		number = number%100
	elif number>=50:
		roman+=Rconvert("L",int(number/50))
		number = number%50
	elif number>=10:
		roman+=Rconvert("X",int(number/10))
		number = number%10
	elif number>=5:
		roman+=Rconvert("V",int(number/5))
		number = number%5
	elif number>=1:
		roman+=Rconvert("I",int(number/1))
		number = number%1

print("Old school Roman equivalent of",num_input," = ",roman)

# Modern Roman numerals

num_input = input("Enter an integer between 1 and 3000: ")
number = int(num_input)
roman = ""

def postRoman(letter, value):
	rom = ""
	while value>0:
		rom+=letter
		value-=1
	return rom
def preRoman(letter1, letter2):
	rom = ""
	rom=letter1+letter2
	return rom

while number!=0:
	if number>=1000:
		roman+=postRoman("M",int(number/1000))
		number = number%1000
	elif number>=500:
		if number<900:
			roman+=postRoman("D",int(number/500))
			number = number%500
		else:
			roman+=preRoman("C","M")
			number = number-(1000-100)
	elif number>=100:
		if number<400:
			roman+=postRoman("C",int(number/100))
			number = number%100
		else:
			roman+=preRoman("C","D")
			number = number-(500-100)
	elif number>=50:
		if number<90:
			roman+=postRoman("L",int(number/50))
			number = number%50
		else:
			roman+=preRoman("X","C")
			number = number-(100-10)
	elif number>=10:
		if number<40:
			roman+=postRoman("X",int(number/10))
			number = number%10
		else:
			roman+=preRoman("X","L")
			number = number-(50-10)
	elif number>=5:
		if number<9: 
			roman+=postRoman("V",int(number/5))
			number = number%5
		else:
			roman+=preRoman("I","X")
			number = number-(10-1)
	elif number>=1:
		if number<4:
			roman+=postRoman("I",int(number/1))
			number = number%1
		else:
			roman+=preRoman("I","V")
			number = number-(5-1)
print("Modern Roman equivalent of",num_input," = ",roman)