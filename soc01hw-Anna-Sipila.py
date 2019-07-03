# Day 1

#hours in a year
print(24*365)

#minutes in a decade
print(60*24*365*10)

#Your age in seconds (not considering leap years or exact time of birth... I'm 37 years old.)
print(37*365*24*60*60)

#Andreea's age (There must be an error in the number? She can't be a toddler!)
print(48618000/(60*60*24*365))

# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow? The system uses milliseconds.
print(2**32/1000/60/60/24)
# 64 bits
print(2**64/1000/60/60/24)

# Day 3

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. 
# Finally, it should greet the person using their full name.

first_name = input('First name: ')
middle_name = input('Middle name: ')
last_name = input('Last name: ')

print('Hello, ' + first_name + ' ' + middle_name + ' ' + last_name + ', nice to meet you!')

# # Bigger, better favorite number. Write a program that asks for a person’s favorite number. 
# # Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. 
# # (Do be tactful about it, though.)

fav_num = input('What\'s your favorite number? Please write with numbers, not letters. ')

print(str(int(fav_num) + 1) + ' would be a bigger and better favorite number, right?')

# # Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. 

answer = str.upper(input('WHADDAYA WANT??? '))

print('WHADDAYA MEAN "' + answer + '"?!?' + ' YOU\'RE FIRED!')

# Table of Contents (I wasn't sure how the formatting was supposed to look like, so I decided it myself :) )

# Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

header = 'Table of Contents'
str1 = 'Chapter '
str2 = 'Getting Started'
str3 = 'Numbers        '
str4 = 'Letters        '
str5 = 'page '

print()
print(header.center(40, ' '))
print()
print(str1 + '1: ' + str2 + (str5 + '1').rjust(30, ' '))
print(str1 + '2: ' + str3 + (str5 + '9').rjust(30, ' '))
print(str1 + '3: ' + str4 + (str5 + '13').rjust(30, ' '))
print()

# Day 4

# Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”

text1 = ' bottles of beer'
text2 = ' on the wall'
text3 = 'Take one down and pass it around, '
i = 99
while i != 1:
	print(str(i) + text1 + text2 + ', ' + str(i) + text1 + '.' + text3 + str(i-1) + text1 + text2 + '.')
	i = i-1
	
print('1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.')
print('No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.')
	
# Deaf grandma extended. (I know the random year system is not perfect as it won't use all the years between 1930 and 1950... But at least it's something.
# And I'm not sure if I got the BYE 3 times in a row right...)

import random

answer = input('Say something to grandma. ')

while answer != 'BYE'*3:
	while answer != str.upper(answer):
		answer = input('HUH?! SPEAK UP, GIRL! ')
	answer = input('NO, NOT SINCE ' + str(int(random.random()*20 + 1930)) + '! ')
print('BYE, SWEETHEART!')

# Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them 
# (and including them, if they are also leap years).

year1 = input('Insert a starting year, please. ')
year2 = input('Insert an ending year, too, please. ')
for i in range(int(year1), int(year2)+1):
	if ((i % 4 == 0 and i % 100 != 0) or i % 400 == 0):
		print(i)

print('These are the leap years in between the two years you just inserted.')

# Find something today in your life, that is a calculation.
# How many times does my 2-years-old daughter say "I want out of this thing" in a day?
high_chair = int(input('How many meals does your child eat in a day? '))
car_seat = int(input('How many minutes does she travel in a car daily? '))
bicycle = int(input('How many minutes does she travel on the backseat of a bicycle daily? '))
potty = int(input('How many times a day does she sit on a potty? '))
swing = int(input('How many times a day does she sit on a swing? '))

calculation = int(high_chair*5 + car_seat*0.5 + bicycle*0.1 + potty*3 + swing*2)

print('She says "I want out of this thing" approximately ' + str(calculation) + ' times a day!')

 Building and sorting a list. Write the program that asks us to type as many words as we want 
# (one word per line, continuing until we just press Enter on an empty line) and then repeats 
# the words back to us in alphabetical order. 

words = []
word = input('Add a word or see alphabetical order by pressing Enter: ') 

while word != '':
	words.append(word)
	word = input('Add a word or see alphabetical order by pressing Enter: ') 
	# I'm sure there should be a more sophisticated way of doing line 124 as it is exactly the same as line 120, but can't figure it out...

words.sort()
print(words)
