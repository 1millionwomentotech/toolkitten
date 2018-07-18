#Hours in a year. How many hours are in a year?
print(24 * 365)

#Minutes in a decade. How many minutes are in a decade?
print(10 * 365 * 24 * 60)

#Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
print(32 * 365 * 24 * 60 * 60)

#Andreea Visanoiu​: I'm 486180000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print(486180000 / 60 / 60 / 24 / 365)

######

#Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.
first_name = input('What\'s your first name?')
middle_name = input('What\'s your middle name?')
last_name = input('What\'s your last name?')
print('Hello ' + first_name + ' ' + middle_name + ' ' + last_name + "!")

#Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
number = input('What\'s your favorite number?')
newnumber = int(number) + 1
print('Really? I think that ' + str(newnumber) + ' is a much better favorite number for you.')

#Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
#WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
request = input('What do you want to ask your boss?')
print('WHADDAYA MEAN ' + '\"' + request.upper() + '\"' + '?!? YOU\'RE FIRED!!')

#Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
title = 'Table Of Content'
string1 = 'Chapter 1: Getting Started'
stringA = 'page 1'
string2 = 'Chapter 2: Numbers'
stringB = 'page 9'
string3 = 'Chapter 3: Letters'
stringC = 'page 13'
print(title.center(len(title) *4)) 
print(string1.ljust(len(string1)) + stringA.rjust(45 - len(string1)))
print(string2.ljust(len(string2)) + stringB.rjust(45 - len(string2)))
print(string3.ljust(len(stringB)) + stringC.rjust(46 - len(string3)))