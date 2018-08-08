# ##### Write a program that tells you the following:

# ##### DAY1 #####
# # 1. Hours in a year. How many hours are in a year?
# print(24 * 365)

# # 2. Minutes in a decade. How many minutes are in a decade?
# print((60 * 24) *365* 10)

# # 3. Your age in seconds. How many seconds old are you? 
# print(60*60*(24 * 365 * 21))

# # 4. Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
# print(48618000 / (60*60*24*365) * 10)

# ##### DAY2 ##### NONE

# ##### DAY3 #####
# # 5. Full name greeting. Write a program that asks for a 
# # person’s first name, then middle, and then last. Finally,
# # it should greet the person using their full name.
# first = input("Enter first name: ").lower()
# mid = input("Enter second name: ").lower() + ' '
# last = input("Enter last name: ").lower()
# print("Nice to meet you, " + first.capitalize() + ' ' + mid.capitalize() + last.capitalize())

# # 6. Bigger, better favorite number. Write a program that
# # asks for a person’s favorite number. Have your program 
# # add 1 to the number, and then suggest the result as a 
# # bigger and better favorite number. (Do be tactful 
# # about it, though.)

# asking = True
# while asking:
# 	fav = input("What's your favorite number?")
# 	if fav.isalpha():		
# 		print("That's not a number!")
# 	else:
# 		big = int(fav) + 1
# 		print("A bigger and better number is this: " + str(big))
# 		asking = not asking
# print();

# # 7. Angry boss. Write an angry boss program that rudely 
# # asks what you want. Whatever you answer, the angry boss
# # should yell it back to you and then fire you. For example, 
# # if you type in I want a raise, it should yell back like this:
# # WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
# employee = input("What would you like to ask DA BOSS?")
# print("WHAT DO YOU MEAN '" + employee.upper() + "'?! YOU ARE FIRED!!")
# print()

# # 8. Table of contents. Here’s something for you to do in 
# # order to play around more with center, ljust, and rjust: 
# # write a program that will display a table of contents 
# print("Table of Contents")
# ch1 = "Chapter 1: Getting Started"
# ch2 = "Chapter 2: Numbers"
# ch3 = "Chapter 3: Letters"
# p1 = "page 1"
# p2 = "page 9"
# p3 = "page 13" 
# # Printing the original string
# print ("The original string is : \n", ch1, "\n")
# print ("The original string is : \n", ch2, "\n")
# print ("The original string is : \n", ch3, "\n")
 
# # Printing aligned strings
# print ("The right aligned: ")
# print (ch1 + p1.rjust(40, '.'))
# print (ch2 + p2.rjust(40, '.'))
# print (ch3 + p3.rjust(40, '.'))
# print()
# print ("The left aligned: ")
# print (p1.ljust(40, '.') + ch1)
# print (p2.ljust(40, '.') + ch2)
# print (p3.ljust(40, '.') + ch3)
# print()
# print ("The center aligned: ")
# print ((ch1 + ' - ' + p1).center(40, '.'))
# print ((ch2 + ' - ' + p2).center(40, '.'))
# print ((ch3 + ' - ' +p3).center(40, '.'))
# print()

# ##### DAY4 #####
# # 9. “99 Bottles of Beer on the Wall.” Write a program that
# # prints out the lyrics to that beloved classic, “99 Bottles
# # of Beer on the Wall.”
# print()
# bottles = input("How many bottles are on the wall? ")
# b = 0
# while bottles.isalpha():
# 	bottles = input("How many bottles are on the wall?")
# 	print("Please type a number")
# if not bottles.isalpha() and int(bottles) > 0: 
# 	b = int(bottles)
# for x in range(b, -1, -1):
# 	if x == 0:
# 		print("No more bottles of beer on the wall, no more bottles of beer.")
# 		print("Go to the store and buy some more, " + bottles + " bottles of beer on the wall.")
# 	elif x == 1:
# 		print("1 bottle of beer on the wall, 1 bottle of beer.")
# 		print("Take one down and pass it around, no more bottles of beer on the wall.")
# 	else:
# 		print(str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
# 		print("Take one down and pass it around, " + str(x - 1) + " bottle of beer on the wall.")
# print()

# # 10a. Deaf grandma. Whatever you say to Grandma (whatever you type
# # in), she should respond with this: HUH?! SPEAK UP, GIRL! Unless
# # you shout it (type in all capitals). If you shout, she can
# # hear you (or at least she thinks so) and yells back: 
# # NO, NOT SINCE 1938! To make your program really believable,
# # have Grandma shout a different year each time, maybe any 
# # year at random between 1930 and 1950. You can’t stop 
# # talking to Grandma until you shout BYE.
# import random
# reply = input("What do you want to say to grandma?")
# pw = "BYE" 

# while reply != pw:
# 	if not reply.isupper():
# 		print("HUH?! SPEAK UP, GIRL!")
# 		reply = input("What do you want to say to grandma?")
# 	else:		
# 		y = random.randint(1930,1950)
# 		print("NO, NOT SINCE " + str(y) + ", HONEY!")
# 		reply = input("What do you want to say to grandma?")
# print()


# # 10b. Deaf grandma extended. What if Grandma doesn’t want 
# # you to leave? When you shout BYE, she could pretend not to
# # hear you. Change your previous program so that you have to 
# # shout BYE three times in a row. Make sure to test your 
# # program: if you shout BYE three times but not in a row, 
# # you should still be talking to Grandma.
# import random
# reply = input("What do you want to say to grandma?")
# pw = "BYE" 

# while reply != (pw + ' ' + pw + ' ' + pw):
# 	if not reply.isupper():
# 		print("HUH?! SPEAK UP, GIRL!")
# 		reply = input("")
# 	else:		
# 		y = random.randint(1930,1950)
# 		print("NO, NOT SINCE " + str(y) + ", HONEY!")
# 		reply = input("")
# print("BYE,SWEETIE! COME BACK SOON!")
# print()

# # 11. Leap years. Write a program that asks for a starting 
# # year and an ending year and then puts all the leap years
# # between them (and including them, if they are also leap
# # years). Leap years are years divisible by 4 (like 1984 
# # and 2004). However, years divisible by 100 are not leap
# # years (such as 1800 and 1900) unless they are also 
# # divisible by 400 (such as 1600 and 2000, which were 
# # in fact leap years). What a mess!
# print("Calculating Leap Years \n")
# start_str = input("Enter a start year: ")
# end_str = input("Enter an end year: ")
# s = int(start_str)
# e = int(end_str)
# leaps = ''

# for y in range(s,e):
# 	if (y % 100 == 0):
# 		if y % 400 == 0:
# 			leaps += (str(y) + ' ')
# 		else:
# 			pass 
# 	elif (y % 4 == 0):
# 		leaps += (str(y) + ' ')

# if s == e: 
# 	if (s % 100 == 0):
# 		if s % 400 == 0:
# 			leaps += (str(s) + ' ')
# 		else:
# 			pass 
# 	elif (s % 4 == 0):
# 		leaps += (str(s) + ' ')


# print("Here are the leap years: " + leaps)
# print();

# # 12. Find something today in your life, that is a 
# # calculation. Go for a walk, look around the park, try 
# # to count something. Anything! And write a program about
# # it. e.g. number of stairs, steps, windows, leaves 
# # estimated in the park, kids, dogs, estimate your books
# # by bookshelf, toiletries, wardrobe.
# import random

# counting = True
# while counting:
# 	destination = ["the park", "the zoo", "your house"]
# 	num = random.randint(0,len(destination)-1)
# 	place = destination[num]
# 	print("TODAY YOU DECIDED TO COUNT SOME STUFF AT " + place.upper())

# 	stuff = ["bird", "tiger", "book"]
# 	amount = random.randint(1,21)
# 	print("YOU LOOK AROUND AND SEE THERE ARE " + str(amount) +
# 	" " + stuff[num].upper() +"S TO COUNT!")

# 	counter = 0	
# 	variations = ["feathers", "stripes", "chapters"]
# 	total = random.randint(1,21)
# 	print()
# 	print("Press ENTER to find out how many " + variations[num] + " each " +
# 		stuff[num] + " has!")
# 	while counter != total:
# 		to_count = input("")
# 		if not to_count:
# 			counter += 1
# 		else:
# 		    print ("Got start counting all over!")

# 	print("Congrats! You counted " + str(counter) + " " + variations[num] +
# 		" on each " + stuff[num] + " at " + 
# 		destination[num] + " today!")
# 	counting = not counting
# print()

# # 13. Building and sorting a list. Write the program that asks us to type 
# # as many words as we want (one word per line, continuing until we just press
# # Enter on an empty line) and then repeats the words back to us in 
# # alphabetical order. Make sure to test your program thoroughly; for example, 
# # does hitting Enter on an empty line always exit your program? Even on the
# # first line? And the second? Hint: There’s a lovely array method that will
# # give you a sorted version of an array: sorted(). Use it!
#
# writing = True
# final = []
# words = []
# counter = 0

# print("LET'S MAKE A LIST!")
# print("1.WRITE A WORD \n2.PRESS ENTER TO MOVE ON\n3.PRESS ENTER AGAIN TO EXIT\n")

# while writing:
# 	w = input()
# 	if w:
# 		words.append(w)
# 	if not w:
# 		counter += 1
# 	if counter == 1:
# 		writing = not writing

# print("Sorted list of words: ")
# final = [print(w) for w in sorted(words)]
# print()

# # 14. Table of contents. Write a table of contents program here. Start the 
# # program with a list holding all of the information for your table of 
# # contents (chapter names, page numbers, and so on). Then print out the 
# # information from the list in a beautifully formatted table of contents.
# # Use string formatting such as left align, right align, center.
# import random
# organizing = True
# titles = ["Growing Up", "Drowning", "To Enjoy, or Not To Enjoy", "Flourish", "ANTI"]
# pages = [random.randint(0,20), random.randint(21, 40), random.randint(41, 66),
# random.randint(67, 87), random.randint(88,111)]
# # s = [p for p in pages]
# # print(s)
# chaps = ["Chapter 1: ", "Chapter 2: ", "Chapter 3: ", "Chapter 4: ", "Chapter 5: "]

# print("WE ARE ALIGNING THE TABLE OF CONTENTS FOR YOUR NEXT BOOK!")
# print("CHOOSE AND CHANGE A PREVIEW OPTION: \n0 - LEFT ALIGNED\n1 - CENTER ALIGNED\n2 - RIGHT ALIGNED\n3 - EXIT")


# while organizing:
# 	o = input()
# 	if o == '0':
# 		for x in range(0, len(chaps)):	
# 			page_str = str(pages[x])	
# 			print (page_str.ljust(40, '.') + chaps[x] + titles[x])
# 	elif o == '1':
# 		for i in range(0, len(chaps)):	
# 			page_str = str(pages[i])	
# 			print((chaps[i] + titles[i]).center(40,'.') + page_str)
# 	elif o == '2':
# 		for j in range(0, len(chaps)):	
# 			page_str = str(pages[j])	
# 			print (chaps[j] + titles[j] + page_str.rjust(40, '.'))
# 	elif o == '3':
# 		organizing = not organizing
# 	else:
# 		print("INVALID: Try again")

# print()


# # 15. Write a function that prints out "moo" n times.
# SIDE EFFECT OF print()
# def cow_noise(n = 1, sound = "moo "):
# 	print(sound * n)

# print("Fiona the baby cow goes: ")
# cow_noise()
# print("Lucy the cow goes: ")
# cow_noise(3)
# print("Daddy bull goes ")
# cow_noise(2, "MOOOO ")
# print()

# CLEANER - using return
# def cow_noise(n = 1, sound = "moo "):
# 	return sound * n

# print("Fiona the baby cow goes: " + cow_noise())
# print("Lucy the cow goes: " + cow_noise(3))
# print("Daddy bull goes: " + cow_noise(2, "MOOOO "))
# print()

# # 16. Old-school Roman numerals. In the early days of Roman numerals, the 
# # Romans didn’t bother with any of this new-fangled subtraction “IX” 
# # nonsense. No, milady, it was straight addition, biggest to littlest — so
# # 9 was written “VIIII,” and so on. Write a method that when passed an 
# # integer between 1 and 3000 (or so) returns a string containing the proper
# # old-school Roman numeral. In other words, old_roman_numeral 4 should 
# # return 'IIII'. Make sure to test your method on a bunch of different numbers.
# # Hint: Use the integer division and modulus methods. For reference, these
# # are the values of the letters used: 
# # I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
# def old_school(n = 1):
# 	rom = ""
# 	left = n
# 	while (not (left == 0)):
# 		if (n >= 1000):
# 			m = n // 1000
# 			left -= (m * 1000)
# 			rom += ("M" * m)
# 		if (left >= 500):
# 			d = left // 500
# 			left -= (d * 500)
# 			rom += ("D" * d)
# 		if (left >= 100):
# 			c = left // 100
# 			left -= (c * 100)
# 			rom += ("C" * c)
# 		if (left >= 50):
# 			l = left // 50
# 			left -= (l * 50)
# 			rom += ("L" * l)
# 		if (left >= 10):
# 			x = left // 10
# 			left -= (x * 10)
# 			rom += ("X" * x)
# 		if (left >= 5):
# 			v = left // 5
# 			left -= (v * 5)
# 			rom += ("V" * v)
# 		if (left >= 1):
# 			i = left // 1
# 			left -= (i * 1)
# 			rom += ("I" * i)

# 	return print(rom)

# old_school(4)
# old_school(9)
# old_school(3000)
# old_school(2999)
# print()

# 17. “Modern” Roman numerals. Eventually, someone thought it would be 
# terribly clever if putting a smaller number before a larger one meant
# you had to subtract the smaller one. As a result of this development,
# you must now suffer. Rewrite your previous method to return the new - 
# style Roman numerals so when someone calls roman_numeral 4, it should 
# return 'IV', 90 should be 'XC' etc.
# solution logic provided by @ Sriharsha Sammeta from geekfoorgeek.org
# Improved by me @ pinedab
import math

def new_school(n = 0):
  while(n > 3000 or n == 0):
  	n = int(input("Enter a number btwn 1 - 3000:"))

  romansDict = \
      {
          1: "I",
          5: "V",
          10: "X",
          50: "L",
          100: "C",
          500: "D",
          1000: "M",
          5000: "G",
          10000: "H"
      }

  div = 1
  while n >= div:
      div *= 10
  
  div //= 10
 
  res = ""

  while n:

      # main significant digit extracted
      # into lastNum 
      lastNum = int(n // div)

      if lastNum <= 3:
          res += (romansDict[div] * lastNum)
      elif lastNum == 4:
          res += (romansDict[div] +
                        romansDict[div * 5])
      elif 5 <= lastNum <= 8:
          res += (romansDict[div * 5] +
          (romansDict[div] * (lastNum - 5)))
      elif lastNum == 9:
          res += (romansDict[div] +
                        romansDict[div * 10])

      n = math.floor(n % div)
      div /= 10
        
  return str(res)

print("Roman Numeral of Integer is: "
		+ new_school())