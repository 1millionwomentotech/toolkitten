### DAY 1 ###
import random
import datetime

# calculator
# Write a program that tells you the following:
# -Hours in a year. How many hours aare in a year?
# -Minutes in a decade. How many minutes are in a decade?
# -Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
# -Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
# -Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.


# Print solution
def print_solution(num, date_format_1, date_format_2):
    print("There are " + str(num) + " " + date_format_1 + " per " + date_format_2 + ".")


# Hours in a year
def hours_per_year():
        return 24 * 365


# Minutes in a decade
def minutes_per_decade():
    return (hours_per_year() * 60) * 10


# Your age in seconds
def age_in_seconds(age):
    print("You are " + str(((((int(age) * 365) * 24) * 60) * 60)) + " seconds old.")


# Andreea Visanoiu​: 48618000 seconds old. Calculate @Andreea Visanoiu's age.
def year_from_sec(second):
    print(str(((((int(second) / 60) / 60) / 24) / 365)))


def age_from_sec(second):
    years = second // (60 * 60 * 24 * 364) 
    second -= years * (60 * 60 * 24 * 364)
    months = second // (30 * 24 * 60 * 60)
    second -= months * (30 * 24 * 60 * 60)
    days = second // (24 * 60 * 60)
    print("You are " + str(years) + " years " + str(months) + " months " + str(days) + " days old.")


# Calculate your age accurately based on your birthday
def accurate_age(b_year, b_month, b_day):
    actual_year = 2018
    actual_month = 7
    actual_day = 18
    actual_year_to_sec = (actual_year - 1900) * 364 * 24 * 60 * 60
    actual_month_to_sec = (actual_month - 1) * 30 * 24 * 60 * 60
    actual_day_to_sec = (actual_day - 1) * 24 * 60 * 60

    birtday_year_to_sec = (b_year - 1900) * 364 * 24 * 60 * 60
    birtday_month_to_sec = (b_month - 1) * 30 * 24 * 60 * 60
    birthday_day_to_sec = (b_day - 1) * 24 * 60 * 60

    actual_date_after_1900_in_sec = actual_year_to_sec + actual_month_to_sec + actual_day_to_sec
    bday_date_after_1900_in_sec = birtday_year_to_sec + birtday_month_to_sec + birthday_day_to_sec

    actual_age_in_sec = actual_date_after_1900_in_sec - bday_date_after_1900_in_sec

    age_from_sec(actual_age_in_sec)

print_solution(hours_per_year(), "hours", "year")

print_solution(minutes_per_decade(), "minutes", "decade")

age_in_seconds(30)

year_from_sec(48618000)

accurate_age(1988, 7, 19)

print(1+2)
print(3)
print(10 % 2)
print(11 % 2)

############################### DAY 3 #######################################

# 1) Try this to run & see what error messages, behaviour I get

'''
float('15')


float('99.999'​)
int('99.999'​)

int('5 is my favorite number!'​) 
int('Who asked you about 5 or whatever?'​)
float('Your momma did.'​)

str('stringy'​)
int(3)
'''

#### A Few Things to Try

'''
2)
- Full name greeting. Write a program that asks for a person’s first name, 
then middle, and then last. Finally, it should greet the person using their full name. 
3)
- Bigger, better favorite number. Write a program that asks for a person’s 
favorite number. Have your program add 1 to the number, and then suggest the
result as a bigger and better favorite number. (Do be tactful about it, though.)
'''

# Full name greeting

full_name = ""
firts_name = input("Please, enter your first name: ")
full_name += firts_name
middle_name = input("Please, enter your middle name: ")
full_name += " " + middle_name
last_name = input("Please, enter your last name: ")
full_name += " " + last_name
print("Hello, " + full_name)

# Bigger, better favorite number

users_favourite_num = int(input("Please, enter your favourite number: "))
print("I think a bigger and better number will be a better choice for you. " +
"Let's have this: " + str(users_favourite_num + 1))

'''
4) Check out more fancy string methods here: 
https://docs.python.org/3/library/stdtypes.html#str

'''

'''5)
- Angry boss. Write an angry boss program that rudely asks what you want. 
Whatever you answer, the angry boss should yell it back to you and then fire you. 
For example, if you type in I want a raise, it should yell back like this: 

```
WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
```

    6)
- Table of contents. Here’s something for you to do in order to 
play around more with center, ljust, and rjust: write a program 
that will display a table of contents so that it looks like this: 

Table of Contents 
 
Chapter 1: Getting Started        page 1
Chapter 2: Numbers                page 9
Chapter 3: Letters                page 13
'''

# 5 Angry Boss

what_you_want = input("What do you want? ")
print("Whaddaya mean \'" + what_you_want + "\'?!? You are fired!!")

# 6 Table of contents

print("Table of contents \n")
left_string = "Chapter 1"
right_string = "Page 1"
print(left_string.ljust(40, '.') + right_string)
left_string_2 = "Chapter 2"
right_string_2 = "Page 9"
print(left_string_2 + right_string_2.rjust(40, '.'))


'''7)
Problem solving

- Video: https://www.coursera.org/lecture/duke-programming-web/a-seven-step-approach-to-solving-programming-problems-AEy5M
- Book: The Algorithm Design Manual by Steven S Skiena

'''

'''8)
Research how to generate a random number with Python.

   9) Math object
https://docs.python.org/3/library/math.html 

'''
# 8 random num generator

i = 1
counter = 0
while i < 11:
    print(random.randint(1, 101))
    counter += 1
    i += 1
print("Amount of printed nums: " + str(counter))


############################### DAY 4 #######################################

# 1) “99 Bottles of Beer on the Wall.” 
# Write a program that prints out the lyrics to that beloved classic,
# “99 Bottles of Beer on the Wall.” 

i = 99
while i > 0:
    print(str(i) + " bottles of beer on the wall, " + str(i) + 
    " bottles of beer.\nTake one down and pass it around, " + str(i - 1) +
    " bottles of beer on the wall.\n")
    i -= 1
print("""No more bottles of beer on the wall, no more bottles of beer. 
Go to the store and buy some more, 99 bottles of beer on the wall.""")

# 2) Deaf grandma
'''
- Deaf grandma. Whatever you say to Grandma (whatever you type in), 
she should respond with this: HUH?! SPEAK UP, GIRL! unless you shout it 
(type in all capitals). If you shout, she can hear you (or at least she thinks so) 
and yells back:q

NO, NOT SINCE 1938!

To make your program really believable, have Grandma shout a different year each time, 
maybe any year at random between 1930 and 1950. 
(This part is optional and would be much easier if you read the section on Python’s 
random number generator under the Math Object.) You can’t stop talking to Grandma until 
you shout BYE. 

- Hint: Try to think about what parts of your program should happen over and over again. 
All of those should be in your while loop. 

- Hint: People often ask me, “How can I make random give me a number in a range not 
starting at zero?” But you don’t need it to. Is there something you could do to the number random returns to you? 

- Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, 
she could pretend not to hear you. Change your previous program so that you have to 
shout BYE three times in a row. 
Make sure to test your program: if you shout BYE three times but not in a row, 
you should still be talking to Grandma.''' 