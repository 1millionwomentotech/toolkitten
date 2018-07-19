## Summer of code - 1 million women to tech
## Anna Laszlo
## Hungary
## July 18, 2018

## Week 1 Homework: **A Few Things to Try** sections

## Full name greeting. Write a program that asks for a person’s first name,
## then middle, and then last. Finally, it should greet the person
## using their full name. 
first = input("What is your first name? ")
middle = input("What is your middle name? ")
last = input("What is your last name? ")
if middle == "":
    print("Welcome " + first + " " + last + "!")
else:
    print("Welcome " + first + " " + middle + " " + last + "!")



## Bigger, better favorite number. Write a program that asks for a
## person’s favorite number. Have your program add 1 to the number,
## and then suggest the result as a bigger and better favorite number.
## (Do be tactful about it, though.) 
fnum = input("What is your favorite number?")
fnum = int(fnum) + 1
print("I would suggest You " + str(fnum) + " as a bigger and better favorite number!")



## Angry boss. Write an angry boss program that rudely asks what you want.
## Whatever you answer, the angry boss should yell it back to you and then
## fire you. For example, if you type in I want a raise, it should yell
## back like this: 
## ```
## WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
## ```
employee_wish = input("What do you want? ")
EW = employee_wish.upper()
print("WHADDAYA MEAN \"" + EW + "\"?!? YOU'RE FIRED!!")



## Table of contents. Here’s something for you to do in order to play
## around more with center, ljust, and rjust: write a program that
## will display a table of contents so that it looks like this: 
## Table of Contents 
##  
## Chapter 1: Getting Started        page 1
## Chapter 2: Numbers                page 9
## Chapter 3: Letters                page 13
ch1_title = "Chapter 1: Getting Started"
ch1_page = "page 1"
ch2_title = "Chapter 2: Numbers"
ch2_page = "page 9"
ch3_title = "Chapter 3: Letters"
ch3_page = "page 13"
print(ch1_title + ch1_page.rjust(15, " "))
print(ch2_title + ch2_page.rjust(23, " "))
print(ch3_title + ch3_page.rjust(24, " "))
