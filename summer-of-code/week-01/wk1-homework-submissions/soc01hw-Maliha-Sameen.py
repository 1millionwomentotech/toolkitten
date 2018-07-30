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



















