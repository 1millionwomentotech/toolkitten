# -*- coding: utf-8 -*-
'''
Homework
Week-01
@Sofia Faria
'''

from datetime import datetime
from datetime import date
import random 


#Day-01

def hoursinyears(years):
	hours = years*365*24
	return hours

def minutesindecades(decades):
	minutes = decades*10*365*24*60
	return minutes

def ageinseconds(age):
	seconds = age*365*24*60*60
	return seconds

def andreea_age(seconds):
	years = seconds/(365*24*60*60)
	return years

def findage(birth):
	today = datetime.now()
	age = today.year - birth.year - ((today.month, today.day, today.hour, today.minute) < (birth.month, birth.day, birth.hour, birth.minute)) # se for true subtrai por 1, se for falso subtrai por 0
	return age
	
# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# How about a 64-bit system?

'''
All the letter after a "%" represent a format for something :

%d is the day number
%m is the month number
%b is the month abbreviation
%y is the year last two digits
%Y is the all year
%H  Hour (24-hour clock) as a decimal number [00,23]    
%I  Hour (12-hour clock) as a decimal number [01,12]
%M  Minute as a decimal number [00,59]   
%p  Locale’s equivalent of either AM or PM

'''
#Day-03

def angry_boss():
	what = input('What do you want?? ')
	return 'WHADDAYA MEAN "' + what+ '"?!? YOU\'RE FIRED!!'

def table_of_contents():
	first_linel= 'Chapter 1: Getting Started'
	first_liner= 'page 1'
	second_linel= 'Chapter 2: Numbers'
	second_liner= 'page 9'
	third_linel= 'Chapter 3: Letters'
	third_liner= 'page 13'
	return first_linel.ljust(30) + first_liner.rjust(30)+ '\n' + second_linel.ljust(30) + second_liner.rjust(30) +'\n'+ third_linel.ljust(30) + third_liner.rjust(30)

#Day-04

def bottles_of_beer(bottles):
	while bottles >= 0:
		if bottles > 0 and bottles-1 >1:
			print( str(bottles) +' bottles of beer on the wall, ' + str(bottles)+' bottles of beer.\n Take one down and pass it around, ' + str(bottles-1) + ' bottles of beer on the wall.')
		elif bottles > 0 and bottles-1 == 1:
			print(str(bottles) +' bottles of beer on the wall, ' + str(bottles)+' bottles of beer.\n Take one down and pass it around, ' + str(bottles-1) + ' bottle of beer on the wall.')
		elif bottles > 0 and bottles-1 == 0:
			print(str(bottles) +' bottle of beer on the wall, ' + str(bottles)+' bottle of beer.\n Take one down and pass it around, no more bottles of beer on the wall.')
		elif bottles == 0:
			print('No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, 99 bottles of beer on the wall.')
		bottles -= 1

def deaf_grandma():
	phrase = input('You: ')
	years = [x for x in range(1930,1951)]
	words = []
	while phrase:
		if phrase.isupper() and phrase != 'BYE':
			year = random.choice(years)
			print('Grandma: NO, NOT SINCE ' + str(year) +'!')
			words.append(phrase)
			phrase = input('You: ')
		elif phrase == 'BYE':
			words.append(phrase)
			if words[-3] == 'BYE' and words[-2]== 'BYE' and words[-1]=='BYE':
				break
			else:  
				print('Grandma: HUH?! SPEAK UP, GIRL!')
				phrase = input('You: ')
		else:
			words.append(phrase)			
			print('Grandma: HUH?! SPEAK UP, GIRL!')
			phrase = input('You: ')


def leap():
	start = int(input('Starting year: '))
	end = int(input('Ending year: '))
	leap = [year for year in range(start, end+1) if year %4==0 or year %400==0]
	return leap


def array():
	word = input('Word: ')
	words = []
	while word:
		words.append(word)
		word= input('Word: ')
	
	sort_words=sorted(words)
	for w in sort_words:
		print(w)

def table2 (information):
	chapters = []
	pages = []
	for i in information:
		if 'Chapter' in i:
			chapters.append(i)
		elif 'page' in i:
			pages.append(i)

	sort_chapters = sorted_with_numbers(chapters)
	sort_pages = sorted_with_numbers(pages)
	if len(sort_chapters) ==  len(sort_pages):
		for i in range(len(sort_chapters)):
			print (sort_chapters[i].ljust(45,'.') + sort_pages[i].rjust(30) + '\n')
	else: print('Number of chapters and pages aren\'t equal.')

import re
def sorted_with_numbers(l):
	# alphanum_key =[]
	# for x in re.split('([0-9]+)', key):
	# 	alphanum_key.append(numeric(x))
    alphanum_key = lambda key: [numeric(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

def numeric(x):
	if x.isdigit(): return int(x)
	else: return x


def old_roman_numerals(): # I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
	number = int(input('Number: '))
	I = 1
	V = 5
	X = 10
	L = 50
	C = 100
	D = 500
	M = 1000
	if number >= 1 and number <= 3000:
		if number == 1:
			return 'I'
		elif number == 5:
			return'V'
		elif number == 10:
			return 'X'
		elif number == 50:
			return 'L'
		elif number == 100:
			return 'C'
		elif number == 500:
			return 'D'
		elif number == 1000:
			return 'M'
		elif number < 5:
			i = int(number/I)
			return 'I'*i 
		elif number < 10:
			i = number - V
			return 'V'+('I'*i)
		elif number < 50:
			x = int(number/X)
			if (number - (X*x)) >= V:  
				i = number - (X*x) - V
				return ('X'*x)+'V'+('I'*i)
			else: 
				i = number - X*x
				return ('X'*x) + ('I'*i)
		elif number < 100:
			rest = number - L
			x = int(rest/X)
			if (number - L- (X*x)) >= V:  
				i = number - L - (X*x) - V
				return ('L')+('X'*x)+'V'+('I'*i)
			else: 
				i = number - L - X*x
				return ('L')+('X'*x) + ('I'*i)
		elif number < 500:
			c = int(number/C)
			rest = int((number - (C*c))/X)
			if rest >= 5:
				x = rest-5
				if (number - (C*c)-L-(X*x)) >= V:  
					i = number - (C*c)- L -(X*x) - V
					return ('C'*c)+ ('L')+('X'*x)+'V'+('I'*i)
				else: 
					i = number - (C*c)- L -(X*x)
					return ('C'*c)+ ('L')+('X'*x)+('I'*i)
			else:
				x = rest
				if (number - (C*c)- (X*x)) >= V:  
					i = number - (C*c)-(X*x) - V
					return ('C'*c)+('X'*x)+'V'+('I'*i)
				else: 
					i = number - (C*c)-(X*x)
					return ('C'*c)+('X'*x)+('I'*i)
		elif number < 1000:
			rest = number - D
			c = int(rest/C)
			if (number - D -(C*c)) >= L:  
				x = int(((number - D -(C*c)) - L)/X)
				if (number - D -(C*c) - L- (X*x)) >= V:
					i = number - D -(C*c)- L - (X*x) - V
					return 'D' + ('C'*c) + 'L' + ('X'*x) + 'V'+('I'*i)
				else: 
					i = number - D -(C*c) -L- (X*x)
					return 'D' + ('C'*c) + 'L' + ('X'*x) + ('I'*i)
			else: # <L
				x = int((number - D -(C*c))/X)
				if (number - D -(C*c) - (X*x)) >= V:
					i = number - D -(C*c) - (X*x) - V
					return 'D' + ('C'*c) + ('X'*x) + 'V'+('I'*i)
				else: 
					i = number - D -(C*c) - (X*x)
					return 'D' + ('C'*c) + ('X'*x) + ('I'*i)	

		elif number > 1000:
			m = int(number/M)
			rest = number - m*M
			if rest >= D:
				rest2 = rest - D
				c = int(rest2/C)
				if (number - (M*m) - D -(C*c)) >= L:  
					x = int((number - (M*m) - D -(C*c) - L)/X)
					if (number - (M*m) - D -(C*c) - L- (X*x)) >= V:
						i = number -(M*m) -D -(C*c)- L - (X*x) - V
						return ('M'*m) +'D' + ('C'*c) + 'L' + ('X'*x) + 'V'+('I'*i)
					else: 
						i = number -(M*m)- D -(C*c) -L- (X*x)
						return ('M'*m) + 'D' + ('C'*c) + 'L' + ('X'*x) + ('I'*i)
				else: # <L
					x = int((number -(M*m)- D -(C*c))/X)
					if (number - (M*m)-D -(C*c) - (X*x)) >= V:
						i = number -(M*m) - D -(C*c) - (X*x) - V
						return ('M'*m) +'D' + ('C'*c) + ('X'*x) + 'V'+('I'*i)
					else: 
						i = number-(M*m) - D -(C*c) - (X*x)
						return ('M'*m) + 'D' + ('C'*c) + ('X'*x) + ('I'*i)	
			else: # < D
				c = int(rest/C)
				if (number - (M*m) -(C*c)) >= L:  
					x = int((number - (M*m) -(C*c)-L)/X)
					if (number - (M*m) -(C*c) - L- (X*x)) >= V:
						i = number -(M*m)-(C*c)- L - (X*x) - V
						return  ('M'*m)+ ('C'*c) + 'L' + ('X'*x) + 'V'+('I'*i)
					else: 
						i = number -(M*m)-(C*c) -L- (X*x)
						return ('M'*m) + ('C'*c) + 'L' + ('X'*x) + ('I'*i)
				else: # <L
					x = int((number -(M*m)-(C*c))/X)
					if (number -(M*m)-(C*c) - (X*x)) >= V:
						i = number - (M*m)-(C*c) - (X*x) - V
						return ('M'*m) + ('C'*c) + ('X'*x) + 'V'+('I'*i)
					else: 
						i = number -(M*m) -(C*c) - (X*x)
						return ('M'*m) + ('C'*c) + ('X'*x) + ('I'*i)	
			
				


#Do the new_roman_numerals

	

if __name__ == '__main__':
	print(hoursinyears(1))
	print(minutesindecades(1))
	print(ageinseconds(21))
	print(andreea_age(48618000))
	datetime_object = datetime.strptime('Oct 1 1996  7:25PM', '%b %d %Y %I:%M%p')   
	print(findage(datetime_object))
	# today = date.today()
	# print(1 - ((today.month, today.day) > (datetime_object.month, datetime_object.day)))
	# print(datetime.now())
	print(angry_boss())				
	print(table_of_contents())
	bottles_of_beer(99)
	deaf_grandma()
	print(leap())
	array()
	table2(['Chapter 1', 'Chapter 2', 'page 1', 'Chapter 3: How to sort arrays', 'page 3', 'page 11'])
	print(old_roman_numerals())

