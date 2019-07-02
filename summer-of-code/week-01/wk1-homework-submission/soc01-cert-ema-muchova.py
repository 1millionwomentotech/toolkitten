#Hours in a year. How many hours are in a year?

print(365 * 24)

#Minutes in a decade. How many minutes are in a decade?

print(365 * 10 * 24 * 60)

#Your age in seconds. How many seconds old are you?

print(21 * 365 * 24 * 60 * 60)

#Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.

print(48618000 / 60 / 60 / 24 / 365)

#Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

first_name = input("What is your first name? ")
middle_name = input("What is your middle name? ")
last_name = input("What is your last name? ")
print("Hello " + first_name + " " + middle_name + " " + last_name + " !")

#Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number.

number = int(input("What is your favourite number? "))
number = number + 1
print("I think " + str(number) + " is a bigger and better favourite number.")

#Angry boss.

answer = input("What do you want? ")
print("WHADDAYA MEAN " + "\"" + answer + "\"" + "?!?" + " YOU'RE FIRED!!")

#Table of contents.

print("Chapter 1: ".ljust(0) + "Getting Started".ljust(20) + "page 1 ".rjust(0))
print("Chapter 2: ".ljust(0) + "Numbers".ljust(20) + "page 9 ".rjust(0))
print("Chapter 3: ".ljust(0) + "Letters".ljust(20) + "page 13".rjust(0))

#99 Bottles of Beer on the Wall.

x = 99
while x !=0:
    if x != 1:
        print(str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
        x -= 1
        print("Take one down and pass it around, " + str(x) + " bottles of beer on the wall.")
    elif x == 1:
        print(str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
        x -= 1
print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

#Deaf grandma.

from random import randint
me = ""
while me != "BYE":
    me = input()
    if me.isupper() == True:
        print("NO, NOT SINCE " + str(randint(1930, 1950)) +" !")
    else:
        print("HUH?! SPEAK UP, GIRL!")
#Deaf grandma, extended.

from random import randint
me = ""
num = 0
while num != 3:
    me = input()
    if me.isupper() == True:
        print("NO, NOT SINCE " + str(randint(1930, 1950)) +" !")
        if me == "BYE":
            num += 1
        else:
            num = 0
    else:
        print("HUH?! SPEAK UP, GIRL!")
        num = 0

#Building and sorting an array.

x = " "
list = []
while x != "":
    x = input()
    list.append(x)
list.pop()
print(sorted(list))

#Table of contents.

list_2 = ["Chapter 1: ", "Chapter 2: ", "Chapter 3: ", "Getting started", "Numbers", "Letters", "page 1 ", "page 9 ", "page 13"]
print(list_2[0].ljust(0) + list_2[3].ljust(20) + list_2[6].rjust(0))
print(list_2[1].ljust(0) + list_2[4].ljust(20) + list_2[7].rjust(0))
print(list_2[2].ljust(0) + list_2[5].ljust(20) + list_2[8].rjust(0))

#Write a function that prints out "moo" n times.

def moo(n):
    print("moo " * n)

#Old-school Roman numerals.

def number(x):
    num = ""
    if len(str(x)) == 4:
        y = int(str(x)[0])
        num = num + "M" * y
        x = int(str(x)[1:4])
        if int(str(x)[0]) >= 5 and len(str(x)) == 3:
            num = num + "D"
            x = x - 500
            if len(str(x)) == 3:
                y = int(str(x)[0])
                num = num + "C" * y
                x = int(str(x)[1:3])
                if int(str(x)[0]) >= 5 and len(str(x)) == 2:
                    num = num + "L"
                    x = x - 50
                    if len(str(x)) == 2:
                        y = int(str(x)[0])
                        num = num + "X" * y
                        x = int(str(x)[1])
                        if x >= 5:
                            num = num + "V"
                            x = x - 5
                            num = num + "I" * x
                        elif x < 5:
                            num = num + "I" * x
                    elif len(str(x)) == 1:
                        if x >= 5:
                            num = num + "V"
                            x = x - 5
                            num = num + "I" * x
                        elif x < 5:
                            num = num + "I" * x
                elif int(str(x)[0]) < 5 and len(str(x)) == 2:
                    y = int(str(x)[0])
                    num = num + "X" * y
                    x = int(str(x)[1])
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
                elif len(str(x)) == 1:
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
            elif len(str(x)) == 2:
                if int(str(x)[0]) >= 5:
                    num = num + "L"
                    x = x - 50
                    if len(str(x)) == 2:
                        y = int(str(x)[0])
                        num = num + "X" * y
                        x = int(str(x)[1])
                        if x >= 5:
                            num = num + "V"
                            x = x - 5
                            num = num + "I" * x
                        elif x < 5:
                            num = num + "I" * x
                    elif len(str(x)) == 1:
                        if x >= 5:
                            num = num + "V"
                            x = x - 5
                            num = num + "I" * x
                        elif x < 5:
                            num = num + "I" * x
                elif int(str(x)[0]) < 5:
                    y = int(str(x)[0])
                    num = num + "X" * y
                    x = int(str(x)[1])
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
            elif len(str(x)) == 1:
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
        elif int(str(x)[0]) < 5 and len(str(x)) == 3:
            y = int(str(x)[0])
            num = num + "C" * y
            x = int(str(x)[1:3])
            if int(str(x)[0]) >= 5 and len(str(x)) == 2:
                num = num + "L"
                x = x - 50
                if len(str(x)) == 2:
                    y = int(str(x)[0])
                    num = num + "X" * y
                    x = int(str(x)[1])
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
                elif len(str(x)) == 1:
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
            elif int(str(x)[0]) < 5 and len(str(x)) == 2:
                y = int(str(x)[0])
                num = num + "X" * y
                x = int(str(x)[1])
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
            elif len(str(x)) == 1:
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
        elif int(str(x)[0]) >= 5 and len(str(x)) == 2:
            num = num + "L"
            x = x - 50
            if x >= 10:
                y = int(str(x)[0])
                num = num + "X" * y
                x = int(str(x)[1])
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
            elif x < 10:
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
        elif int(str(x)[0]) < 5 and len(str(x)) == 2:
            y = int(str(x)[0])
            num = num + "X" * y
            x = int(str(x)[1])
            if x >= 5:
                num = num + "V"
                x = x - 5
                num = num + "I" * x
            elif x < 5:
                num = num + "I" * x
        elif len(str(x)) == 1:
            if x >= 5:
                num = num + "V"
                x = x - 5
                num = num + "I" * x
            elif x < 5:
                num = num + "I" * x
    elif len(str(x)) == 3:
        if int(str(x)[0]) >= 5:
            num = num + "D"
            x = x - 500
            if len(str(x)) == 3:
                y = int(str(x)[0])
                num = num + "C" * y
                x = int(str(x)[1:3])
                if int(str(x)[0]) >= 5 and len(str(x)) == 2:
                    num = num + "L"
                    x = x - 50
                    if x >= 10:
                        y = int(str(x)[0])
                        num = num + "X" * y
                        x = int(str(x)[1])
                        if x >= 5:
                            num = num + "V"
                            x = x - 5
                            num = num + "I" * x
                        elif x < 5:
                            num = num + "I" * x
                    elif x < 10:
                        if x >= 5:
                            num = num + "V"
                            x = x - 5
                            num = num + "I" * x
                        elif x < 5:
                            num = num + "I" * x
                elif int(str(x)[0]) < 5 and len(str(x)) == 2:
                    y = int(str(x)[0])
                    num = num + "X" * y
                    x = int(str(x)[1])
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
                elif len(str(x)) == 1:
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
            elif len(str(x)) == 2:
                if int(str(x)[0]) >= 5:
                    num = num + "L"
                    x = x - 50
                    if x >= 10:
                        y = int(str(x)[0])
                        num = num + "X" * y
                        x = int(str(x)[1])
                        if x >= 5:
                            num = num + "V"
                            x = x - 5
                            num = num + "I" * x
                        elif x < 5:
                            num = num + "I" * x
                    elif x < 10:
                        if x >= 5:
                            num = num + "V"
                            x = x - 5
                            num = num + "I" * x
                        elif x < 5:
                            num = num + "I" * x
                elif int(str(x)[0]) < 5:
                    y = int(str(x)[0])
                    num = num + "X" * y
                    x = int(str(x)[1])
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
            elif len(str(x)) == 1:
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
        elif int(str(x)[0]) < 5:
            y = int(str(x)[0])
            num = num + "C" * y
            x = int(str(x)[1:3])
            if int(str(x)[0]) >= 5 and len(str(x)) == 2:
                num = num + "L"
                x = x - 50
                if x >= 10:
                    y = int(str(x)[0])
                    num = num + "X" * y
                    x = int(str(x)[1])
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
                elif x < 10:
                    if x >= 5:
                        num = num + "V"
                        x = x - 5
                        num = num + "I" * x
                    elif x < 5:
                        num = num + "I" * x
            elif int(str(x)[0]) < 5 and len(str(x)) == 2:
                y = int(str(x)[0])
                num = num + "X" * y
                x = int(str(x)[1])
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
            elif len(str(x)) == 1:
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x

    elif len(str(x)) == 2:
        if int(str(x)[0]) >= 5:
            num = num + "L"
            x = x - 50
            if x >=  10:
                y = int(str(x)[0])
                num = num + "X" * y
                x = int(str(x)[1])
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
            elif x < 10:
                if x >= 5:
                    num = num + "V"
                    x = x - 5
                    num = num + "I" * x
                elif x < 5:
                    num = num + "I" * x
        elif int(str(x)[0]) < 5:
            y = int(str(x)[0])
            num = num + "X" * y
            x = int(str(x)[1])
            if x >= 5:
                num = num + "V"
                x = x - 5
                num = num + "I" * x
            elif x < 5:
                num = num + "I" * x

    elif len(str(x)) == 1:
        if x >= 5:
            num = num + "V"
            x = x - 5
            num = num + "I" * x
        elif x < 5:
            num = num + "I" * x
    else:
        print("Sorry, no output for this input.")
    print(num)

#“Modern” Roman numerals.

def funkcia(x):
    num = ""
    if x > 3000 or x == 0:
        print("Sorry, no output for this input.")
    elif len(str(x)) == 4:
        num += "M" * int(str(x)[0])
        if int(str(x)[1]) == 0:
            num += ""
        elif int(str(x)[1]) == 1 or int(str(x)[1]) == 2 or int(str(x)[1]) == 3:
            num += "C" * int(str(x)[1])
        elif int(str(x)[1]) == 4:
            num += "CD"
        elif int(str(x)[1]) == 5:
            num += "D"
        elif int(str(x)[1]) == 6 or int(str(x)[1]) == 7  or int(str(x)[1]) == 8:
            num += "D" + "C" * (int(str(x)[1]) - 5)
        elif int(str(x)[1]) == 9:
            num += "CM"
        if int(str(x)[2]) == 0:
            num += ""
        elif int(str(x)[2]) == 1 or int(str(x)[2]) == 2 or int(str(x)[2]) == 3:
            num += "X" * int(str(x)[2])
        elif int(str(x)[2]) == 4:
            num += "XL"
        elif int(str(x)[2]) == 5:
            num += "L"
        elif int(str(x)[2]) == 6 or int(str(x)[2]) == 7  or int(str(x)[2]) == 8:
            num += "L" + "X" * (int(str(x)[2]) - 5)
        elif int(str(x)[2]) == 9:
            num += "XC"
        if int(str(x)[3]) == 0:
            num += ""
        elif int(str(x)[3]) == 1 or int(str(x)[3]) == 2 or int(str(x)[3]) == 3:
            num += "I" * int(str(x)[3])
        elif int(str(x)[3]) == 4:
            num += "IV"
        elif int(str(x)[3]) == 5:
            num += "V"
        elif int(str(x)[3]) == 6 or int(str(x)[3]) == 7  or int(str(x)[3]) == 8:
            num += "V" + "I" * (int(str(x)[3]) - 5)
        elif int(str(x)[3]) == 9:
            num += "IX"
    elif len(str(x)) == 3:
        if int(str(x)[0]) == 1 or int(str(x)[0]) == 2 or int(str(x)[0]) == 3:
            num += "C" * int(str(x)[0])
        elif int(str(x)[0]) == 4:
            num += "CD"
        elif int(str(x)[0]) == 5:
            num += "D"
        elif int(str(x)[0]) == 6 or int(str(x)[0]) == 7  or int(str(x)[0]) == 8:
            num += "D" + "C" * (int(str(x)[0]) - 5)
        elif int(str(x)[0]) == 9:
            num += "CM"
        if int(str(x)[1]) == 0:
            num += ""
        elif int(str(x)[1]) == 1 or int(str(x)[1]) == 2 or int(str(x)[1]) == 3:
            num += "X" * int(str(x)[1])
        elif int(str(x)[1]) == 4:
            num += "XL"
        elif int(str(x)[1]) == 5:
            num += "L"
        elif int(str(x)[1]) == 6 or int(str(x)[1]) == 7  or int(str(x)[1]) == 8:
            num += "L" + "X" * (int(str(x)[1]) - 5)
        elif int(str(x)[1]) == 9:
            num += "XC"
        if int(str(x)[2]) == 0:
            num += ""
        elif int(str(x)[2]) == 1 or int(str(x)[2]) == 2 or int(str(x)[2]) == 3:
            num += "I" * int(str(x)[2])
        elif int(str(x)[2]) == 4:
            num += "IV"
        elif int(str(x)[2]) == 5:
            num += "V"
        elif int(str(x)[2]) == 6 or int(str(x)[2]) == 7  or int(str(x)[2]) == 8:
            num += "V" + "I" * (int(str(x)[2]) - 5)
        elif int(str(x)[2]) == 9:
            num += "IX"
    elif len(str(x)) == 2:
        if int(str(x)[0]) == 1 or int(str(x)[0]) == 2 or int(str(x)[0]) == 3:
            num += "X" * int(str(x)[0])
        elif int(str(x)[0]) == 4:
            num += "XL"
        elif int(str(x)[0]) == 5:
            num += "L"
        elif int(str(x)[0]) == 6 or int(str(x)[0]) == 7  or int(str(x)[0]) == 8:
            num += "L" + "X" * (int(str(x)[0]) - 5)
        elif int(str(x)[0]) == 9:
            num += "XC"
        if int(str(x)[1]) == 0:
            num += ""
        elif int(str(x)[1]) == 1 or int(str(x)[1]) == 2 or int(str(x)[1]) == 3:
            num += "I" * int(str(x)[1])
        elif int(str(x)[1]) == 4:
            num += "IV"
        elif int(str(x)[1]) == 5:
            num += "V"
        elif int(str(x)[1]) == 6 or int(str(x)[1]) == 7  or int(str(x)[1]) == 8:
            num += "V" + "I" * (int(str(x)[1]) - 5)
        elif int(str(x)[1]) == 9:
            num += "IX"
    elif len(str(x)) == 1:
        if int(str(x)[0]) == 1 or int(str(x)[0]) == 2 or int(str(x)[0]) == 3:
            num += "I" * int(str(x)[3])
        elif int(str(x)[0]) == 4:
            num += "IV"
        elif int(str(x)[0]) == 5:
            num += "V"
        elif int(str(x)[0]) == 6 or int(str(x)[0]) == 7  or int(str(x)[0]) == 8:
            num += "V" + "I" * (int(str(x)[0]) - 5)
        elif int(str(x)[0]) == 9:
            num += "IX"
    elif len(str(x)) != 1 or len(str(x)) != 2 or len(str(x)) != 3 or len(str(x)) != 4:
        print("Sorry, no output for this input.")
    print(num)