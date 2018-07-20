#dayWee-01

#Hours in a year. How many hours are in a year?

print(24*365)

#Minutes in a decade. How many minutes are in a decade?

print(10*365*24*60)

#Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
print(21*365*24*60*60)

#andrea's age
a=48618000/31536000
print(int(a))

#Solution: How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
print(2**31-1)

#How about a 64-bit system?
print(2**63-1)

#day-03
#Full name greeting
print('Enter your first name: ')
firstName= input()
print('Enter your second name: ')
secondName= input()
print('Enter your last name: ')
lastName=input()

print('Welcome, '+firstName+' '+secondName+' '+lastName )

#Bigger, better favorite number
print('Enter a numberL: ')
number=int(input())
number= number+1
print('A Bigger and better number: '+str(number))

#Angry boss
print('What do you want: ')
statement= input()
print('WHADDAYA MEAN "'+statement.upper()+'"?!? YOU\'RE FIRED!!')

#Table of Contents
print('Table of Contents\n')
statement='Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13'
print(statement.center(80,' '))

#day-04
#print 'moo' n times
def printMoo(n):
	for x in range(n):
		print('moo')

printMoo(3)
