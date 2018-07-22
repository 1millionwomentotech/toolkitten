#hours in a year
print(24*365)

#minutes in a decade
print(60*24*365*10)

#age in seconds
print(60*60*24*365*30)

#andreea's age
print(48618000/31536000)

#angry boss

print("What do you want?")
employee_says = input()
print("WHADDAYA MEAN " + employee_says + "?!? YOU'RE FIRED!!")

#bottle of beers on the wall

num_bottles = 99
while num_bottles >0:
	if num_bottles==1:
		print(str(num_bottles) + " bottle of beer on the wall")
	else:
		print(str(num_bottles) + " bottles of beer on wall")
	num_bottles = num_bottles-1
	print(1+2)response = ""

#deaf grandma

import random

granddaughter_Says = input()
all_Caps = granddaughter_Says.isupper()
rando_Year = random.randint(1930, 1951)

while granddaughter_Says != "BYE":
    if all_Caps == False:
        print("HUH?! SPEAK UP, GIRL!")
    else:
        print("NO, NOT SINCE " + str(random.randint(1930, 1950)))
    print()
    print("Say hello to Deaf Grandma!")
    granddaughter_Says = input()
    all_Caps = granddaughter_Says.isupper()

 #sortedlist

word=input("enter a word ")
word_list = []
while word != "":
	word_list.append(word)
	word=input()

word_list.sort()

print(word_list)

#print moo n times

def printMoo(n):
	for x in range(n):
		print("moo")

printMoo(3)

#roman numeral

def old_roman_numeral(number: int):
	roman_numeral = ""
	while number>0:
		if number >= 1000:
			roman_numeral += "M"
			number -= 1000
		elif number >=500:
			roman_numeral += "D"
			number -=500
		elif number >=100:
			roman_numeral += "C"
			number -= 100
		elif number >= 50:
			roman_numeral += "l"
			number-= 50
		elif number >= 10:
			roman_numeral += "X"
			number -= 10
		elif number >= 5:
			roman_numeral += "V"
			number -= 5
		elif number >= 1:
			roman_numeral += "I"
			number -= 1
	return roman_numeral

print(old_roman_numeral(333))