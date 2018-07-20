# Wk 1 Homework
# Upload a single file named as
# soc01hw-firstname-lastname.py
# Include all exercised from A Few Things to Try sections.
# If it says Optional, then the homework is of course optional, it is for those who would like more / or more advanced exercises.

#I have not done any optional exercises.

#Day 1
#1.1. Program to calculate hours in a year
normal_year = 365 #days
leap_year = 366 #days
hours_per_day = 24
print("there are", normal_year*hours_per_day,
	"hours in a standard year and", leap_year*hours_per_day,
	"in a leap year.")

#1.2. Calculate minutes in a decade.
#assuming each decade involves 2 leap years:
minutes_per_hour = 60
minutes_per_decade = (8 * normal_year + 2 * leap_year) * hours_per_day * minutes_per_hour
print("there are", minutes_per_decade, "minutes in a decade.")

#1.3. Calculate age in seconds.
#the date chosen is an example - DOB is personal info :)
#I used the datetime module and followed the tutorial at
#https://pymotw.com/2/datetime/ 
#and answer at
#https://stackoverflow.com/questions/15067710/calculate-the-difference-between-two-times-in-python

import datetime
#note datetime is in year-month-day format

today = datetime.datetime(2018, 8, 20, 12) #y|m|d|hour
birthdate = datetime.datetime(1986, 9, 26, 10, 30)

date_diff = today - birthdate
age_in_seconds = date_diff.total_seconds() #returns a float
print("I am hypothetically", int(age_in_seconds), "seconds old.")

#1.4. Calculate Andrea Visanoiu's age.
#because can't know in advance whether will have sg or plural value for any unit of time:
def sg_or_plural(number, word):
	if int(number) ==1:
		return(word)
	elif int(number) !=1:
		return(word +"s")

#splitting off whole number values thanks to answer here: https://stackoverflow.com/questions/6681743/splitting-a-number-into-the-integer-and-decimal-parts
import math
AV_age_seconds = 48618000 #this really is the number on Github...
whole_min = math.modf(AV_age_seconds/60)[1]
spare_sec = AV_age_seconds%60
#math.modf splits (123.456) into .456 and 123 **in that order**, so whole number value is [1].


whole_hours = math.modf(whole_min/60)[1]
spare_min = whole_min%60

whole_days = math.modf(whole_hours/24)[1]
spare_hours = whole_hours%24

whole_years = math.modf(whole_days/365)[1] #since the total no. on github is so low, no need to worry about leap years
spare_days = whole_days%365


print("Andrea Visanoiu is", int(whole_years), sg_or_plural(whole_years, "year")
	, int(spare_days), sg_or_plural(spare_days, "day"), 
	int(spare_hours), sg_or_plural(spare_hours, "hour"), 
	int(spare_min), sg_or_plural(spare_min, "minute"), "and",
	int(spare_sec), sg_or_plural(spare_sec, "second"), "old.")

#Day 2
#no tasks set

#Day 3
#3.1 Full name greeting
firstname = input("Welcome! Please enter your first name. ")

middle_name = input("Thank you. Now please enter your middle name. ")

last_name = input("Thank you. Finally, please enter your last name. ")

final_message = "Thank you for entering your name, " + firstname + " " + middle_name + " " + last_name + "!"
print(final_message)
#3.2 Bigger, better favourite number
first_no = input("Hello! What is your favourite number? ")
new_no = int(first_no) +1
print("I see your favourite number is " + first_no +". But " + str(new_no) + " is one higher. Can I persuade you that equals one better?")

#3.3 Angry Boss
#Desired output: "WHADDAYA MEAN [uppercase version of input]?!? YOU'RE FIRED!!"
request_in = input("Welcome to your annual performance review! What would you like to ask your boss?")
answer_out = "WHADDAYA MEAN '" + str.upper(request_in) +"'?!? YOU'RE FIRED!"
print(answer_out)

#3.4 Table of contents
#didn't really understand the instructions for this task
header = "Table of Contents"
ch_1 = "Chapter 1: Getting started"
ch_1_page = "page 1"
ch_2 = "Chapter 2: Numbers"
ch_2_page = "page 9"
ch_3 = "Letters"
ch_3_page = "page 13"

print(header.ljust(len(header)), "\n")
print(ch_1.ljust(len(ch_1)), ch_1_page.ljust(len(ch_1_page)),
	ch_2.ljust(len(ch_2)), ch_2_page.ljust(len(ch_2_page)),
	ch_3.ljust(len(ch_3)), ch_3_page.ljust(len(ch_3_page)))

#Wk 4
#4.1 99 bottles of beer
#lyrics from https://en.wikipedia.org/wiki/99_Bottles_of_Beer
for i in reversed(range(0, 100)):
	if i > 0:
		print(str(i) + " bottles of beer on the wall", str(i), "bottles of beer.")
		print("Take one down, pass it around,", str(i-1), "bottles of beer on the wall",
		str(i-1), "bottles of beer.")
	elif i == 0:
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 99 bottles of beer on the wall, 99 bottles of beer.")


#4.2 extended deaf grandma
import random
BYE_counter = 0
response = input("Hello dear! What did you say?")

while BYE_counter <2:
	if not response.isupper():
		BYE_counter = 0
		response = input("HUH?! SPEAK UP, GIRL! ")
	if response.isupper():
		if response != "BYE":
			BYE_counter = 0
			gran_years = random.randrange(1930, 1950, 1)#step is one so don't have numbers less than an integer year
			response = input("NO, NOT SINCE " + str(gran_years) + "!")
		elif response == "BYE":
			print("old counter is", BYE_counter)
			BYE_counter = BYE_counter +1
			print("new counter is", BYE_counter)
			gran_years = random.randrange(1930, 1950, 1)#step is one so don't have numbers less than an integer year
			response = input("NO, NOT SINCE " + str(gran_years) + "!")
print("That's nice dear, see you soon.")

#4.3 leap years
print("Hello. I'm going to calculate the leap years between two years you enter.")
start_year = int(input("Please enter a start year."))
end_year = int(input("Please enter an end year."))

while end_year <= start_year:
	end_year = int(input("I'm sorry, the end year has to be above the start year. Please enter a new end year."))

year_diff = end_year - start_year

#calculate leap years
ly_list = []
for i in range(start_year, end_year+1, 1): #increasing by whole integer years
	if i%4 == 0:
		if i%100 == 0:
			if i%400 == 0:
				ly_list.append(i)
		elif i%100 != 0:
			ly_list.append(i)
print("the leap years between the dates you have entered are", ly_list)

#4.4 calculation in daily life
#this is a calculator to estimate the number of stitches in a hand-knitted item.
fo_weight = int(input("Please enter the finished weight of your item."))
print("Now weigh your item at a point, A, and a few rows later at another point, B. There should be no increases or decreases between the two points.")
start_point = int(input("Please enter the weight of your item at point A."))
end_point = int(input("Please enter the weight of your item at point B."))
calc_rounds = int(input("Please enter the number of rows between points A and B."))
calc_sts_per_round = int(input("Please enter the number of sts per row in the section between A and B."))

weight_diff = end_point - start_point
sts_in_section = calc_rounds * calc_sts_per_round
multiplicator = fo_weight/weight_diff

estimated_sts = int(sts_in_section*multiplicator)
print("There are", estimated_sts, "stitches in your item.")	

#4.5 build and sort array
word_list = []
entry = input("Welcome! Enter any word. To exit the program, press Enter.")

while entry != "":
	word_list.append(entry)
	entry = input("Welcome! Enter any word. To exit the program, press Enter.")
if len(word_list) == 0:
	print("you typed no words.")
elif len(word_list) == 1:
	print("the word you entered was", word_list[0], ".")
elif len(word_list) >1:
	sorted_list = sorted((word_list))
	print("in alphabetical order, the words you entered were", sorted_list, ".")

#4.6 table of contents
toc_list = ["Table of Contents", "Chapter 1: The First Chapter", "page 1", "Chapter 2: Return of the Chapter", "page 34", "Chapter 3: Are you still reading this?", "page 464"]
for i in toc_list:
	if i == "Table of Contents":
		print("\n", i.center(len(i)), "\n")
	elif "Chapter" in i:
		print(i.ljust(len(i)))
	elif "page" in i:
		print(i.rjust(50))


#4.7 n times moo
def less_is_moo(number):
	return("moo " *int (number))

#4.8 old-school Roman numerals
def romanumerator(number):
	if 0 < number <3001:
		M_num = number//1000
		M_remainder = number%1000
		D_num = M_remainder//500
		D_remainder = M_remainder%500
		C_num = D_remainder//100
		C_remainder = D_remainder%100
		L_num = C_remainder//50
		L_remainder = C_remainder%50
		X_num = L_remainder//10
		X_remainder = L_remainder%10
		V_num = X_remainder//5
		V_remainder = X_remainder%5
		I_num = V_remainder #no need to div by 1

		oldskool_rom_num = ("M"*M_num + "D"*D_num + "C"*C_num + "L"*L_num
			+ "X"*X_num + "V"*V_num + "I"*I_num)
		print(oldskool_rom_num)
	else:
		print("please enter a number between 1 and 3000. The Romans didn't have 0, and your eyes will die with large numbers.")

romanumerator(999)
romanumerator(523452345134452134)

#4.9 "modern" Roman numerals
def novaroma(number):
	if 0 < number <3001:
		M_num = number//1000
		M_remainder = number%1000
		D_num = M_remainder//500
		D_remainder = M_remainder%500
		C_num = D_remainder//100
		C_remainder = D_remainder%100
		L_num = C_remainder//50
		L_remainder = C_remainder%50
		X_num = L_remainder//10
		X_remainder = L_remainder%10
		V_num = X_remainder//5
		V_remainder = X_remainder%5
		I_num = V_remainder #no need to div by 1

		num_compiler = ""
		hundreds = number%1000
		tens = number%100
		digits = number%10
		#print(hundreds, tens, digits)

		hun_flat = hundreds - tens
		ten_flat = tens - digits

		#add thousands
		num_compiler = "M"*M_num

		#add hundreds
		if hun_flat == 900:
			num_compiler = num_compiler + "CM"
		elif hun_flat == 400:
			num_compiler = num_compiler + "CD"
		else:
			num_compiler = num_compiler + ("D"*D_num + "C"*C_num)

		#add tens
		if ten_flat == 90:
			num_compiler = num_compiler + "XC"
		elif ten_flat == 40:
			num_compiler = num_compiler + "XL"
		else:
			num_compiler = num_compiler + ("L"*L_num + "X"*X_num)
		
		#add single digits
		if digits == 9:
			num_compiler = num_compiler + "IX"
		elif digits == 4:
			num_compiler = num_compiler + "IV"
		else:
			num_compiler = num_compiler + ("V"*V_num + "I"*I_num)

		print(num_compiler)
	else:
		print("please enter a number between 1 and 3000. The Romans didn't have 0, and your eyes will die with large numbers.")

 
novaroma(999)
novaroma(523452345134452134)
novaroma(876)
#end of week 1 exercises. FLD.