I'm so grateful for Your amazing dedication.Thank You so much.

#SOC-week-1/day-1

#A-hours in a year

days = 365
hours = 24
hours_in_year = days * hours
print (hours_in_year)

#B-minutes in a decade

days = 365
hours = 24
minutes = 60
minutes_in_year = days * hours * minutes
minutes_in_decade = 10 * minutes_in_year
print (minutes_in_decade)

#C-my age in seconds

import datetime

my_born_day = datetime.datetime(1964, 9, 17)
actual_day = datetime.datetime(2018, 7, 17)
days_completed = actual_day - my_born_day
my_born_hour = 12
actual_hour = 17
hours_completed = actual_hour - my_born_hour
hours = 24
seconds = 3600
days_completed_in_seconds = 19661 * hours * seconds
age_in_seconds = days_completed_in_seconds + (hours_completed * 3600)
print(age_in_seconds)


"""D-How many days does it take for a 32-bit /64-bit systems to timeout,
if they have a bug with integer overflow?"""


milliseconds = 2 ** 32 - 1
days_32 = milliseconds/1000/60/60/24
print(days_32)

milliseconds = 2**64 - 1
days_64 = milliseconds/1000/60/60/24
print(days_64)


#SOC-week-1 /day-3

#A- Fullname greeting

x = input("Enter, please your firstname below: " )
y = input("Enter now middle name: ")
z = input("Enter lastname, too: ")
print("You are wellcome, " x, y, z + "!")

#B-  Bigger number

x = int(input("Which is your favorite number" + "?"))
better_number = x + 1
print(" I can suggest you a bigger number : " + str(better_number))

#C- Angry boss:))

wish = input("What do you want" + "?")
print(wish +  " " + "You are fired.")

#D- Table of contents

right_one = str("Chapter 1: Getting started")
left_one = str(1)
print(right_one.ljust(70, '-') + left_one.rjust(1))
right_two = str("Chapter 2: Numbers")
left_two = str(9)
print(right_two.ljust(70, '-') + left_two.rjust(1))
right_three = str("Chapter 3: Letters")
left_three = str(13)
print(right_three.ljust(70,'-') + left_three.rjust(1))

#SOC-week-1/day-4

#A-Beatles song:bottles of beer on the wall

num_bottles = list(range(1,100))

for bott in reversed(num_bottles):
	bott_1 = bott - 1
	print "%(bott)d bottles of beer on the wall, %(bott)d bottles of beer.Take one down and pass it round ,%(bott_1)d bottles of beer on the wall." % {"bott" :bott, "bott_1":bott_1}
	if bott == 1:
		print "%(bott)d bottles of beer on the wall, %(bott)d bottles of beer.Take one down and pass it round ,%(bott_1)d bottles of beer on the wall.No more bottles of beer on the wall,no more bottles of beer.Go to the store and buy some more, %(bott)d bottles of beer on the wall." % {"bott" : bott, "bott_1" :bott_1}
	

#SOC-week-1/day-4

#B-Deaf-grandma-started but I didn't know how to finish it.


import random
me = " "
while me != "BYE"*3:
  me = input("I say to grandma : ")
  if me.islower():
    grandma_one = "She responded : huh?!speak up,girl!"
    print(grandma_one.upper())
  elif me == "BYE":
    print("I want still talk.")
  elif me == "BYE" * 3:
    break
  elif me.isupper():
    year = (str(1938))
    print ("NO, NOT SINCE" + " " + str(random.randint(1930,1960)) + "!")
  
  
#C-Leap-years
    
years = [print (year) for year in range(1900,2000) if year % 4 == 0 ]
print(years)

#D- Camellia thea -count the leaves

def count_leaves (shed_leaves):
  if(shed_leaves >= 30):
    print('Camellia thea will have ' + str(shed_leaves) + ' ' + 'shed leaves this spring.')
    return
  print(shed_leaves)
  shed_leaves += 1
count_leaves(800)

#E-input list print in alphabetical order


words = list()
while True:
  word = input('Enter a word in list and hit enter to stop:\n')
  if word ==  "" :
    break
  words.append(word)
print(sorted(words, reverse = False))

#F content book in list, with titles and pages formatted 

chapter = [ 'Numbers ', 'Variables', 'String', 'Reading files', 'Functions', 'What If', 'Elif', 'Loops ', 'While Loops', 'Dictionaries']

pages = [ 42, 46, 52, 80, 100, 136, 138, 146, 150, 170 ]

pages_str = [str(i) for i in pages]
 
for c,p in zip(chapter, pages_str):
   print(c.ljust(30, '-') + p.rjust(1))

#G-make a function to print moo ,n times.

def print_moo(n):
  print("moo" * n)
print_moo(12)

#H-program that shows what say_moo() returns.Result is None.

def say_moo():
  print("moo")
say_moo()
result = say_moo()
print(result)

#I-convert decimal numbers to romans literals.Monicas-MacBook-Pro:Desktop monicaszabo$ python grandma-1.py

roman_list = ['M', 'CM', 'D', 'C', 'CD', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
decimal_list =[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
def get_roman(decimal_num):
  result = ""
  for i in range(len(decimal_list)):
    while decimal_num % decimal_list[i] < decimal_num :
      result += roman_list[i]
      decimal_num = decimal_num % decimal_list[i]
  print(result) 
  return result
  
  
def get_number():
  try:
    decimal_num = int(input("Please, enter a number between 1 and 3000:"))
    if decimal_num > 3000 or decimal_num < 1:
      print("the number entered is not within the range")
      get_number()
  except ValueError:
    print("that's not a valid number")
    get_number()
  else:
    roman_number = get_roman(decimal_num)
    return roman_number

if __name__ == "__main__":roman_number = get_number()





