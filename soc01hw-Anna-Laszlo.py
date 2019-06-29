## Summer of code - 1 million women to tech
## Anna Laszlo
## Hungary
## July 18, 22, 23 2018

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



## “99 Bottles of Beer on the Wall.” Write a program that prints out the
## lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
for i in reversed(range(100)):
    if i>2:
        print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.")
        print("Take one down and pass it around, " + str(i-1) + " bottles of beer on the wall.")
    elif i==2:
        print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.")
        print("Take one down and pass it around, " + str(i-1) + " bottle of beer on the wall.")
    elif i==1:
        print(str(i) + " bottle of beer on the wall, " + str(i) + " bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")



## Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this:
## HUH?! SPEAK UP, GIRL!
## unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so)
## and yells back:
## NO, NOT SINCE 1938!
## To make your program really believable, have Grandma shout a different year each time,
## maybe any year at random between 1930 and 1950. (This part is optional and would be much easier
## if you read the section on Python’s random number generator under the Math Object.)
## You can’t stop talking to Grandma until you shout BYE.
question = ""
while question != "BYE":
    question = input("Grandchild's question to Grandma is: ")
    if question != "BYE":
        response = print("HUH?! SPEAK UP, GIRL!")
        if question.isupper():
            import random
            year = random.randint(1930, 1950)
            response = print("NO, NOT SINCE " + str(year) + " !")
print("BYE MY DARLING!")

## Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE,
## she could pretend not to hear you. Change your previous program so that you have to shout
## BYE three times in a row. Make sure to test your program:
## if you shout BYE three times but not in a row, you should still be talking to Grandma.
question = ""
while question != "BYE, BYE, BYE":
    question = input("Grandchild's question to Grandma is: ")
    if question != "BYE, BYE, BYE":
        response = print("HUH?! SPEAK UP, GIRL!")
        if question.isupper():
            import random
            year = random.randint(1930, 1950)
            response = print("NO, NOT SINCE " + str(year) + " !")
print("OH, OK! BYE MY DARLING!")




## Leap years. Write a program that asks for a starting year and an ending year and then puts
## all the leap years between them (and including them, if they are also leap years).
## Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100
## are not leap years (such as 1800 and 1900) unless they are also divisible by 400
## (such as 1600 and 2000, which were in fact leap years). What a mess!
start_year = int(input("Please give a starting year: "))
end_year = int(input("Please give and ending year: "))
print("Leap years between the starting and ending year you gave are:")
for i in range(start_year,end_year+1):
    if i%4==0:
        if i%100==0:
            if i%400==0:
                print(str(i))
            else:
                print()
        else:
            print(str(i))




## Find something today in your life, that is a calculation. Go for a walk, look around the park,
## try to count something. Anything! And write a program about it. e.g. number of stairs, steps,
## windows, leaves estimated in the park, kids, dogs, estimate your books by bookshelf,
## toiletries, wardrobe.

## estimate number of book on a bookcase
num_of_shelves = int(input("How many shelves do you have in your bookcase? "))
length_of_shelf = int(input("What is the length of a shelf in cm? "))
percent_used = int(input("About how many percent of the whole bookcase is filled with books? "))
# estimate: approximately 10 books in a 10 cm length of shelf
estimate = round(num_of_shelves * length_of_shelf * percent_used / 100)
print("Approximately you have " + str(estimate) + " number of books on your bookcase.")


## Building and sorting an array. Write the program that asks us to type as many words as we want
## (one word per line, continuing until we just press Enter on an empty line) and then repeats
## the words back to us in alphabetical order. Make sure to test your program thoroughly;
## for example, does hitting Enter on an empty line always exit your program?
## Even on the first line? And the second?
array = []
while word != "":
    word = input("Give one word: ")
    array.append(word)
array_sorted = sorted(array)
print(array_sorted)



## Table of contents. Write a table of contents program here. Start the program with a list holding
## all of the information for your table of contents (chapter names, page numbers, and so on).
## Then print out the information from the list in a beautifully formatted table of contents.
## Use string formatting such as left align, right align, center.
table_of_contents = ["Chapter 1: Getting Started", "1",
                     "Chapter 2: Numbers", "9",
                     "Chapter 3: Letters", "13"
                     ]
for i in range(0, len(table_of_contents), 2):
    print("{0:<35}".format(table_of_contents[i]) +
          "{0:^6}".format("page") +
          "{0:>4}".format(table_of_contents[i+1])
          )




## Write a function that prints out "moo" n times.
#n = input("Please give an integer number between 1 and 10: ")
def print_n_moo(n):
    a = []
    for i in range(0, n):
        a.append("moo")
    print(a)
print_n_moo(4)

## or
def print_n_moo(n):
    for i in range(0, n):
        print("moo")
print_n_moo(6)




## Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any
## of this new-fangled subtraction “IX” nonsense.
## No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
## Write a method that when passed an integer between 1 and 3000 (or so) returns a string
## containing the proper old-school Roman numeral. In other words, old_roman_numeral
## 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers.
## Hint: Use the integer division and modulus methods.
## For reference, these are the values of the letters used: I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
ROMAN = [   (1000, "M"),
            ( 500, "D"),
            ( 100, "C"),
            (  50, "L"),
            (  10, "X"),
            (   5, "V"),
            (   1, "I")
        ]
def old_int_to_roman(n):
    res = ""
    while n > 0:
        for arabic, roman in ROMAN:
            while n >= arabic:
                res += roman
                n -= arabic
    return res

print("-2 = "   + old_int_to_roman(-2))
print("4 = "    + old_int_to_roman(4))
print("23 = "   + old_int_to_roman(23))
print("100 = "  + old_int_to_roman(100))
print("549 = "  + old_int_to_roman(549))
print("1567 = " + old_int_to_roman(1567))
print("3444 = " + old_int_to_roman(3444))



## “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a
## smaller number before a larger one meant you had to subtract the smaller one.
## As a result of this development, you must now suffer.
## Rewrite your previous method to return the new-style Roman numerals so when someone calls
## roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.

ROMAN = [   (1000, "M"),
            ( 900,"CM"),
            ( 500, "D"),
            ( 400,"CD"),
            ( 100, "C"),
            (  90,"XC"),
            (  50, "L"),
            (  40,"XL"),
            (  10, "X"),
            (   9,"IX"),
            (   5, "V"),
            (   4,"IV"),
            (   1, "I")
        ]
def new_int_to_roman(n):
    res = ""
    while n > 0:
        for arabic, roman in ROMAN:
            while n >= arabic:
                res += roman
                n -= arabic
    return res

print("-2 = "   + new_int_to_roman(-2))
print("4 = "    + new_int_to_roman(4))
print("23 = "   + new_int_to_roman(23))
print("90 = "   + new_int_to_roman(90))
print("100 = "  + new_int_to_roman(100))
print("549 = "  + new_int_to_roman(549))
print("1567 = " + new_int_to_roman(1567))
print("3444 = " + new_int_to_roman(3444))
