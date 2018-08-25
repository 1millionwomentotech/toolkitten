# 2.5 A Few Things to Try

#Write a program that tells you the following:

#- Hours in a year. How many hours are in a year?
print(24*365)

# #- Minutes in a decade. How many minutes are in a decade?
print("There are",( 60*24*365*10 ) , + 2, "minutes in a decade")
# #- Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
# # 1min=60sec, 1hr=60min=3600sec, 1day =24 hrs=(24*60)min=(60*60*24)sec, 
print  ("I am",  (34*365*24*60*60), "seconds years old")
# #- Andreea Visanoiu?: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print ( "Andrea is",  ( 48618000/(60*60*24*365)),  "year's old")

#day 3
#### A Few Things to Try

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name. 
print("What is your full name?")
name = "Nadia Ardon"
print("Did you know that there are ", len(name), "characters", "in your name,", name, "?")

## Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.) 
num = input("What is your favorite number: ")
print("This number is bigger and your new favorite number: ", str(int(num) + 1))


#If you want a raise what will your angry boss say
print("WHADDAYA MEAN ","I WANT A RAISE?", "YOU'RE FIRED!!")

##Table of Contents
title = "Table of Contents".center(50)
chap_1 = "Chapter 1: Getting Started".ljust(30) + "page 1".rjust(20)
chap_2 = "Chapter 2: Getting Started".ljust(30) + "page 9".rjust(20)
chap_3 = "Chapter 1: Getting Started".ljust(30) + "page 13".rjust(21)
print(title)
print()
print(chap_1)
print(chap_2)
print(chap_3)
