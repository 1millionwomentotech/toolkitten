def bottles_of_beer():
	for i in range(99,0,-1):
		print(str(i)+ 'bottles of beer on the wall, '+str(i)+' bottles of beer.')
		print('Take one down and pass it around, '+str(i-1)+ ' bottles of beer on the wall.')
	print('No more bottles of beer on the wall, no more bottles of beer.') 
	print('Go to the store and buy some more, 99 bottles of beer on the wall.')

import random
def deaf_grandma():
	print('Tell something to Grandma')
	text = ''
	while(text!='BYE'):
		text = input()
		if text.isupper():
			number = random.randint(1930,1950)
			print('NO, NOT SINCE '+str(number)+'!')
		else:
			print('HUH?! SPEAK UP, GIRL!')

def deaf_grandma_extended():
	print('Tell something to Grandma')
	text = ''
	count = 0
	while count<3:
		text = input()
		number = random.randint(1930,1950)
		if text.isupper() and text =='BYE':
			count +=1
			print('NO, NOT SINCE '+str(number)+'!'+str(count))
		elif text.isupper():
			count = 0
			print('NO, NOT SINCE '+str(number)+'!'+'inside elif')
		else:
			count = 0
			print('HUH?! SPEAK UP, GIRL!')

def leap_years():
	year = int(input('Enter a year '))
	if(year%4==0 and year%100 == 0):
		if(year%400!=0):
			print(str(year)+' is not a leap year')
		else:
			print(str(year)+' is a leap year')
	elif(year%4==0):
		print(str(year)+' is a leap year')
	else:
		print(str(year)+' is not a leap year')

def books_by_bookshelf():
	books = int(input('Enter the estimated number of books per unit'))
	units = int(input('Enter the number of units'))
	total = books*units
	print('Estimated number of books in the bookshelf is '+str(total))

def sort_list():
	print('Enter a word')
	words = []
	text = input()
	while text !='':
		words.append(text)
		words_sorted = sorted(words)
		print(words_sorted)
		text = input()
	print('The sorted list is :')
	print(words_sorted)

def table_of_contents():
	chapter_numbers = ['Chaper 1:','Chaper 2:','Chaper 3:','Chaper 4:']
	chapter_names = ['Intro to Python','Basic Syntax Rules','The First Program','More about the First Program']
	page_numbers = ['1','7','12','16']
	for a in range(4):
		print(chapter_numbers[a].ljust(15,' ')+chapter_names[a].center(40,' ')+page_numbers[a].rjust(6,' '))

def moo():
	n = int(input("Enter the number of times you want to moo "))
	print('moo '*n)

def old_school_roman_numerals(num):
	temp = 0
	num_string = ''
	while num>0:
		if num>=1000:
			temp = num//1000
			num_string +='M'*temp
			num = num%1000	
		if num>=500:
			temp = num//500
			num_string +='D'*temp
			num = num%500
		if num>=100:
			temp = num//100
			num_string +='C'*temp
			num = num%100
		if num>=50:
			temp = num//50
			num_string +='L'*temp
			num = num%50
		if num>=10:
			temp = num//10
			num_string +='X'*temp
			num = num%10
		if num>=5:
			temp = num//5
			num_string +='V'*temp
			num = num%5
		else:
			temp = num
			num_string +='I'*temp
			break
	print(num_string)

numbers = [1000,500,100,50,10,5,1]
characters = ['M','D','C','L','X','V','I']
#numbers = [1,5,10,50,100,500,1000]
#characters = ['I','V','X','L','C','D','M']

def find_roman_number(index,num_string,divide,num):
	count = 0
	for a in range(index+1,len(numbers)):
		if num== 
		print(a,' a is this value')
		print('in outside loop ',(numbers[index]-numbers[a]))
		if num ==(numbers[index]-numbers[a]):
			print('in here '+str(numbers[index]-numbers[a]))
			num_string = num_string+characters[a]+characters[index]
			count+=1
	if count==0:
		print('inside count == 0')
		temp = num//divide
		num_string +=characters[index]*temp
	print(num_string+ " num_string is this")
	return num_string
	
def modern_roman_numerals(num):
	temp = 0
	num_string = ''
	while num>0:
		if num>=1000:
			num_string = find_roman_number(-1,num_string,1000,num)
			num = num%1000	
		if num>=500:
			num_string = find_roman_number(0,num_string,500,num)
			num = num%500
		if num>=100:
			num_string = find_roman_number(1,num_string,100,num)
			num = num%100
		if num>=50:
			num_string = find_roman_number(2,num_string,50,num)
			num = num%50
		if num>=10:
			num_string = find_roman_number(3,num_string,10,num)
			num = num%10
		if num>=5:
			num_string = find_roman_number(4,num_string,5,num)
			#num = num%5
			break
		else:
			if num == 4:
				num_string+='IV'
			else:
				temp = num
				num_string +='I'*temp
			break	
	print(num_string)

def prompt():
	#bottles_of_beer()
	#deaf_grandma()
	#deaf_grandma_extended()
	#leap_years()
	#sort_list()
	#table_of_contents()
	#moo()
	#old_school_roman_numerals(657)
	modern_roman_numerals(500)

prompt()