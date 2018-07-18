import sys, os, datetime
# calculator

def add(num1, num2):
	total = num1 + num2
	return total

def subtract(num1,num2):
	total = num1 - num2
	return total

def multiply(num1,num2):
	total = num1 * num2
	return total

def divide(num1,num2):
	total = num1 / num2
	return total

def hourNyear():
	total = 365.25 * 24
	return total

def minNyear():
	total = 365.25 * 24 * 60
	return total

def minNdecade():
	total = 60 * 24 * 365.25 * 10
	return total

def ageInSeconds(age):
	total = age * 60 * 60 * 24 * 365.25
	return total

# MENU SELECTION
os.system('cls||clear')
print('------- calculator -----')
print('Menu: enter the letters ')
print('      left of the colon ')
print('------------------------')
print('a: add      s: subtract ')
print('m: multiply d: divide   ')
print('hny: hour in a year     ')
print('mnd: minutes in a decade')
print('mny: minute in a year   ')
print('ais: age in seconds     ')
print('x: exit')
print('------------------------')
print('Enter selection:      ')
print('------------------------')

# LOOP THRU USER INPUTS AND SELECTIONS
while True:
	userSelect = input()

	if userSelect == 'a':
		num1= input("Enter first  number: ")
		num2= input("Enter second  number: ")
		print(num1,"+" ,num2,"=" ,add(int(num1),int(num2)))
		print("choose another: ")

	if userSelect == 's':
		num1= input("Enter first larger number: ")
		num2= input("Enter second smaller number: ")
		print(num1,"-" ,num2,"=" ,subtract(int(num1),int(num2)))
		print("choose another: ")	

	if userSelect == 'm':
		num1= input("Enter first  number: ")
		num2= input("Enter second  number: ")
		print(num1,"*" ,num2,"=" ,multiply(int(num1),int(num2)))
		print("choose another: ")

	if userSelect == 'd':
		num1= input("Enter first bigger number: ")
		num2= input("Enter second smaller number: ")
		print(num1,"/" ,num2,"=" ,divide(int(num1),int(num2)))
		print("choose another: ")

	if userSelect == 'mnd':
		print(minNdecade())
		print("choose another: ")

	if userSelect == 'hny':
		print("There are ",hourNyear() ,  "hours in a year")
		print("choose another: ")

	if userSelect == 'mny':
		print("There are ",minNyear()," minutes in a year")
		print("choose another: ")

	if userSelect =='ais':
		num1= input("Enter your Age: ")
		print("You are ", str(ageInSeconds(int(num1))), "seconds old!")
		print("choose another: ")

	if userSelect == 'x':
		sys.exit()
