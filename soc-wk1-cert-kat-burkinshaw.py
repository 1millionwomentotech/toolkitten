'''	WEEK ONE CERTIFICATION EXERCISES 1MWTT SOC
	KAT BURKINSHAW
	GITHUB: KMBu
'''

#Hours in a year

year = (365*24)

leap = (366*24)

print ("There are " + str(year) + " hours in a year, or " + str(leap) + " hours in a leap year")




#MINUTES IN A DECADE

minindecade = (10*365*24*60)

print ("There are " + str(minindecade) + " minutes in a decade")




#AGE IN SECONDS

'''Assume time = 3:40pm on 16th July 2018
Birthdate and time approx 10:30am on 29th August 1989'''

seconds = ((365*28) + (1*7) + (31+30+31+30+31+31+28+31+30+31+17)) *24*60*60 + (5*60*60) + (10*60)

print ("I am " + str(seconds) + " seconds old")




#ANDREA IS 48618000 SECONDS OLD

seconds = 48618000
minutes = (seconds // 60)	
seconds = (seconds % 60)
hours = (minutes // 60)
minutes = (minutes % 60)
days = (hours // 24)
hours = (hours % 24)
years = (days // 365)
days = (days % 365)

print (str(years) + " years, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds.")




#32-BIT SYSTEM TIMEOUT (assuming +1 per second)

seconds = (2**31)-1

print ("sec ", seconds)

minutes = (seconds // 60)
seconds = (seconds % 60)
hours = (minutes // 60)
minutes = (minutes % 60)
days = (hours // 24)
hours = (hours % 24)
years = (days // 365)
days = (days % 365)

print (str(years) + " years, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds until timeout in a 32-bit system")




#64-BIT SYSTEM (assuming +1 per second)

seconds = (2**63)-1

print ("sec ", seconds)

minutes = (seconds // 60)
seconds = (seconds % 60)
hours = (minutes // 60)
minutes = (minutes % 60)
days = (hours // 24)
hours = (hours % 24)
years = (days // 365)
days = (days % 365)

print (str(years) + " years, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds until timeout in a 64-bit system.")




#EXACT AGE

import datetime

birthday = datetime.date(1989,8,29)
print ("I was born on ", birthday)
print ("Current date and time is ", datetime.datetime.now())

a = datetime.datetime.now()
b = datetime.datetime(1989, 8, 29, 10, 30, 0)
time_difference = a-b

print ("I am exactly ", time_difference, " seconds old.")




#ASK USER'S NAME

first_name = input("What is your first name?")
middle_name = input("What is your middle name?")
surname = input("What is your surname?")

print ("Hello " + first_name + " " + middle_name + " " + surname + "! How lovely to meet you!")




#ASK SUGGEST FAVOURITE NUMBER

fave_num = input("What is your favourite number?")
better_num = int(fave_num) + 1

print (fave_num)
print (better_num)

print ("Number " + fave_num + "? Really? I have it on good authority that the number " + str(better_num) + " is much luckier...")




#ANGRY BOSS

want = input("WHAT THE HECK DO YOU WANT?!")

print ("WHADDAYA MEAN \"" + want + "\"?! YOU'RE FIRED!")




#TABLE OF CONTENTS (I)

chap_1 = "Chapter 1: Getting Started"
chap_2 = "Chapter 2: Numbers        "
chap_3 = "Chapter 3: Letters        "
pg_1 = "page 1"
pg_2 = "page 9"
pg_3 = "page 13"

print (chap_1.ljust(25), pg_1.rjust(25) 
	+ "\n" 
	+ chap_2.ljust(25), pg_2.rjust(25) 
	+ "\n" 
	+ chap_3.ljust(25), pg_3.rjust(25))




#RANDOM NUMBERS

import random

world1 = [random.randrange(0, 2, 1) for i in range (10)]
world2 = [random.randrange(0, 2, 1) for i in range (10)]
world3 = [random.randrange(0, 2, 1) for i in range (10)]
world4 = [random.randrange(0, 2, 1) for i in range (10)]
world5 = [random.randrange(0, 2, 1) for i in range (10)]
world6 = [random.randrange(0, 2, 1) for i in range (10)]
world7 = [random.randrange(0, 2, 1) for i in range (10)]
world8 = [random.randrange(0, 2, 1) for i in range (10)]
world9 = [random.randrange(0, 2, 1) for i in range (10)]
world10 = [random.randrange(0, 2, 1) for i in range (10)]
world11 = [random.randrange(0, 2, 1) for i in range (10)]

print (world_1)
print (world_2)
print (world_3)
print (world_4)
print (world_5)
print (world_6)
print (world_7)
print (world_8)
print (world_9)
print (world_10)
print (world_11)

# #OR

#use numpy to create matrix 

import numpy as np

full_world = np.column_stack((world1, world2, world3, world4, world5, world6, world7, world8, world9, world10, world11))

print (full_world)

# #OR

# #use both numpy and random simultaneously

world = np.random.random_integers(0, 1, (11, 11))

print (world)




#99 BOTTLES OF BEER

num_bottles = 99

while num_bottles > 2:
	print (str(num_bottles) + " bottles of beer on the wall,")
	print (str(num_bottles) + " bottles of beer,")
	print ("Take one down and pass it around,")
	num_bottles -= 1
	print (str(num_bottles) + " bottles of beer on the wall")

if num_bottles == 1:
	print (str(num_bottles) + " bottle of beer on the wall,")
	print (str(num_bottles) + " bottle of beer,")
	print ("Take one down and pass it around,")
	num_bottles -= 1
	print ("no more bottles of beer on the wall")

if num_bottles == 0:
	print ("No more bottles of beer on the wall")
	print ("No more bottles of beer")
	print ("Go to the store and buy some more")
	print ("99 bottles of beer on the wall")


#DEAF GRANDMA

import random

speak_up = input("WHAT DO YOU WANT? ")

while speak_up != "BYE":
	while speak_up.isupper() != True:
		print ("HUH? SPEAK UP, GIRL!")
		speak_up = input("WHAT DO YOU WANT? ")
	while speak_up.isupper() and speak_up != "BYE":
			break
		print ("NO, NOT SINCE " + str(random.randint(1930, 1951)))
		speak_up = input("WHAT DO YOU WANT? ")
	while speak_up == "BYE":
		print ("HERE, TAKE A TOFFEE.")
		break




#SAY "BYE" THREE TIMES TO LEAVE

bye_count = 0

while bye_count < 3:
    speak_up = input("WHAT DO YOU WANT? ")
    while speak_up.isupper() != True:
        bye_count = 0
        print ("HUH? SPEAK UP, GIRL!")
        break
	while speak_up.isupper() == True and speak_up != "BYE":
    	bye_count = 0
    	print ("NO, NOT SINCE " + str(random.randint(1930, 1951)))
    	break
	while bye_count ==2 and speak_up == "BYE":
    	bye_count += 1
    	break
    while bye_count <= 1 and speak_up == "BYE":
    	bye_count += 1
    	print ("NO NOT SINCE " + str(random.randint(1930, 1951)))
    	break
while bye_count == 3:
    print ("ALRIGHT, ALRIGHT. TAKE A TOFFEE.")
    break




#LEAP YEARS

start_year = int(input("Enter a start year: "))
end_year = int(input("Enter an end year: "))

def leap_year(year):
	if year % 4 == 0 and not year % 100 == 0:
		return True
	elif year % 100 == 0 and year % 400 == 0:
		return True
	else:
		return False

print ("The following are leap years between " + str(start_year) + " and " + str(end_year))

for year in range(start_year, (end_year + 1)):
	if leap_year(year):
		print (year)




#COUNT THINGS
#Estimating books on a bookshelf with n shelves

count_1 = input("Let's count books! Hit enter to count a book. Type 'done' when you finish.")

books_on_shelf = 0

while count_1 != "done":
	if count_1 == "":
		books_on_shelf += 1
		count_1 = input("Keep counting! Type 'done' when you finish. ")
if count_1 == "done":
	n = int(input("How many shelves are there? "))
	est_books = books_on_shelf * n
	print ("You have approx " + str(est_books) + " books on this set of shelves.")




#SORTED WORD ARRAYS

word = input("Enter a word: ")

sort_list = []

while word:
	sort_list.append(word)
	word = input("Enter a word: ")

print (sorted(sort_list))



#TABLE OF CONTENTS II

toc = ['Chapter 1: Getting Started', 'page 1', 'Chapter 2: Numbers', 'page 9', 'Chapter 3: Letters', 'page 13', 'Chapter 4: Variables and Assignment','page 24', 'Chapter 5: Mixing It Up', 'page 35', 'Chapter 6: More About Methods', 'page 60', 'Chapter 7: Flow Control', 'page 72', 'Chapter 8: Arrays and Iterators', 'page 90', 'Chapter 9: Writing Your Own Methods', 'page 102']

#for cosmetic alignment, set string length for justifying
longest_str = 0
for index, item in enumerate(toc):
    if len(item) > longest_str:
        longest_str = len(item)

#to print and justify table of contents
for index, item in enumerate(toc):
    if index % 2 == 0:
        print (item.ljust(longest_str + 2), toc[index+1].rjust(longest_str + 2))





#MOOING

def say_moo(n):
	print ("moo " * n)

say_moo(20)

#WHAT DOES say_moo RETURN

a = say_moo(4)

print (a)






#OLD SCHOOL NUMERAL

def old_school_numeral(x):
    osn_string = ""
    while x >= 1000:
        x -= 1000
        osn_string += "M"
    while x >= 500:
        x -= 500
        osn_string += "D"
    while x >= 100:
        x -= 100
        osn_string += "C"
    while x >= 50:
        x -= 50
        osn_string += "L"
    while x >= 10:
        x -= 10
        osn_string += "X"
    while x >= 5:
        x -= 5
        osn_string += "V"
    while x >= 1:
        x -= 1
        osn_string += "I"
    return osn_string




#NEW SCHOOL NUMERAL

numeral_dict = {
    "1000":"M",
    "900":"CM", 
    "500":"D", 
    "400":"CD", 
    "100":"C",
    "90":"XC", 
    "50":"L", 
    "40":"XL", 
    "10":"X", 
    "9":"IX", 
    "5":"V", 
    "4":"IV", 
    "1":"I"
    }

def find_numeral(num):
    numeral_string = ""
    for n in numeral_dict:
        div = num // int(n)
        mod = num % int(n)
        numeral_string += numeral_dict[n] * div
        num -= int(n) * div
    return numeral_string
            
#I'm 85% sure this can be solved with recursion, but I can't get my head around how...













