#1 hours in a year
print(24 * (28 + (30 * 4) + (31 * 7) ))
#2 Minutes in a decade
print(60 * 60 * 24 *(28 + (30 * 4) + (31 * 7)) * 10 )
#3 My age in seconds
print(14 * (28 + (30 * 4) + (31 * 7)) * 24 * 60 * 60 )
#4 32-bit
print(2147483635)
#5 64-bit
print(2147483635)
#6 my age
from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2004-05-29 11:55:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))

#8 full name greeting
first_name = input("what\‘s your first name?" + " ")
second_name = input("what\‘s your second name?" + " ")
last_name = input("what\‘s your last name?" + " ")

print("Hello Awesome " + first_name + second_name + last_name)

#9 bigger
fav_number = input("what\‘s your favourite number?" + " ")
print(str(fav_number + 1 + "is better and bigger"))

#10 angry boss
text = input() + " "
print(text.upper() + "!!!! " + "YOU\‘R FIRED")

#11 table of contents
print("Chapter 1:" + "     "  + "Getting Started" + "       " "page 1")
print("Chapter 2:"+ "       "  + " Numbers page 9")
print("Chapter 3:"+ "       " +" Letters page 13")




#12 99 bottle of beers on the wall
a = 99
while a != 0:
	print a - 1

#13 Deaf grandma
b = input() 
while b.isupper() == False:
	print("HUH?! SPEAK UP, GIRL!")
print("NO, NOT SINCE 1938!")

#14 moo function
def moo(n):
	while n != 0:
		print "moo"
		n = n - 1

moo(5)
