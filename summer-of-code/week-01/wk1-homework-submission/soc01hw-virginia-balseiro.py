#Hours in a year. How many hours are in a year?
print(24 * 365)

#Minutes in a decade. How many minutes are in a decade?
print(10 * 365 * 24 * 60)

#Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
print(32 * 365 * 24 * 60 * 60)

#Andreea Visanoiu​: I'm 486180000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print(486180000 / 60 / 60 / 24 / 365)

######

#Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.
first_name = input('What\'s your first name?')
middle_name = input('What\'s your middle name?')
last_name = input('What\'s your last name?')
if middle_name == '':
	print('Hello ' + first_name + ' ' + last_name + '!')
else:
    print('Hello ' + first_name + ' ' + middle_name + ' ' + last_name + '!')

#Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
number = input('What\'s your favorite number?')
newnumber = int(number) + 1
print('Really? I think that ' + str(newnumber) + ' is a much better favorite number for you.')

#Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
#WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
request = input('What do you want to ask your boss?')
print('WHADDAYA MEAN ' + '\"' + request.upper() + '\"' + '?!? YOU\'RE FIRED!!')

#Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
title = 'Table Of Content'
string1 = 'Chapter 1: Getting Started'
stringA = 'page 1'
string2 = 'Chapter 2: Numbers'
stringB = 'page 9'
string3 = 'Chapter 3: Letters'
stringC = 'page 13'
print(title.center(len(title) *4)) 
print(string1.ljust(len(string1)) + stringA.rjust(45 - len(string1)))
print(string2.ljust(len(string2)) + stringB.rjust(45 - len(string2)))
print(string3.ljust(len(stringB)) + stringC.rjust(46 - len(string3)))

#“99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
num = 99
while num > 1:
	print (str(num) + ' bottles of beer on the wall, ' + str(num) + ' bottles of beer, take one down, pass it around, ' + str(num) + ' bottles of beer on the wall!')
	num = num - 1;
	if num == 1:
		print(str(num) + ' bottle of beer on the wall, ' + str(num) + ' bottle of beer, take it down, pass it around, ' + 'no more bottles of beer on the wall!')

#Deaf grandma and Deaf grandma extended:
import random

message = input('Talk to Grandma!')
while message != 'BYE':
	if message != message.upper():
		print('HUH?! SPEAK UP, GIRL!')
	elif message == message.upper() and message != 'BYE':
		print('NO, NOT SINCE 19' + str(random.randint(30, 50)) + '!')
	message = input()
	
if message == 'BYE':
	byecount = 1
	print('HUH?! SPEAK UP, GIRL!')
while byecount < 3:
	message = input()
	byecount = byecount + 1
	print('HUH?! SPEAK UP, GIRL!')
print('Come again soon!')

#Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

start = int(input('Starting year: '))
end = int(input('Ending year: '))
leap_years = [];
for i in range(start, end):
	if (i % 4 == 0) | (i % 4 == 0 and i % 100 == 0 and i % 400 == 0):
		print(i)	

#Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.
#Will your books fit in your new bookcase? find your thickest and your thinnest book, measure their width, measure the width of your shelf, and enter the amount of shelves and see how many books you can fit! Note: width expressed in centimeters!

thinnest_book = float(input('Enter the width in centimeters of your thinnest book: '))
thickest_book = float(input('Enter the width in centimeters of your thickest book: '))
shelf_width = float(input('Enter the width in centimeters of one of your shelves: '))
number_of_shelves = int(input('Enter how many shelves your bookcase has: '))

average_book = (thickest_book + thinnest_book) / 2
breathing_room = average_book * 2
available_width = shelf_width - breathing_room
result = available_width / average_book
print('You can fit ' + str(int(result)) + ' books in your bookcase')


#Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?

word = input('Type a word: ')
words = [word]
while word != '':
	word = input()
	words.append(word)
words.pop()
words.sort()
print(words)

#Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.


info = ['Table Of Content', 'Chapter 1: Getting Started', 'page 1', 'Chapter 2: Numbers', 'page 9', 'Chapter 3: Letters', 'page 13']
print(info[0].center(len(info[0])*4) + '\n' + info[1].ljust(len(info[1])) + info[2].rjust(45 - len(info[1])) + '\n' + info[3].ljust(len(info[3])), info[4].rjust(44 - len(info[3])) + '\n' + info[5].ljust(len(info[5])), info[6].rjust(45 - len(info[5])))

# Write a function that prints out "moo" n times.

def say_moo(times):
	print('moo ' * times)

say_moo(7)

#Take a quick break, and write a program to find out what say_moo returns.
print(say_moo(5))



#Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
#No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
#Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers.
#Hint: Use the integer division and modulus methods.
#For reference, these are the values of the letters used: I = 1 V = 5 X = 10
#L = 50 C = 100 D = 500 M = 1000


def old_roman_numeral(num):
	newnum = []
	decimal = [1000, 500, 100, 50, 10, 5, 1]
	roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	for i in range(len(decimal)):
		while num % decimal[i] < num:
			newnum.append(roman[i])
			num = num - decimal[i]
	print(''.join(newnum))	
	
old_roman_numeral(4673) #should output MMMMDCLXXIII

#“Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc. 
#I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000

def roman_numeral(num):
	newnum = []
	decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	for i in range(len(decimal)):
		while num % decimal[i] < num:
			newnum.append(roman[i])
			num = num - decimal[i]
	print(''.join(newnum))	
	
roman_numeral(4954) #should output MMMMCMLIV