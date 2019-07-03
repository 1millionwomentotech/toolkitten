import random
import math


print("##Week1 day1 general calculations")
print ("Some calculations for day of birth...")
print ("The number of hours in a year: ", 365*24)
print("The number of minutes in a decade: ", 10*365*24*60)
print ("My age (30) in seconds: ", (30*365*24*60*60)/10)
print("Andreea's age is", ((((48618000/365)/24)/60/60)*10))

#I'm not entierly sure how the calculations for age worked but
#I was able to get it based off mine and only when i devided it or multiplied it by 10... seems odd but it worked.
print("")
print("")
print("-----")


print("##Week1 day 2. Strings and Repeating")
print ("hello world")
print("")
print("i like " + 'apple pie')
print ('blink ' *4)
print ('12' + "12" )
print ('25 ' + str( 34))
print ('you\'re swell')
# ^^ this works because the back slash is an excape char used
#to ignore the single char after it.
print("")

myString = "kuu kuu kachu"
print (myString)
myString = "the big old blue"
print (myString)
print("")
name = "DaNeil Claudia Coulthard"
print ('My name is ' +name)
print("")
print("")
print("-----")


print("##Week1 day 3. Numbers and Letters")
result = ""

print ('result: ' +result)

for i in range (0,len(name)):
    if i % 2 == 0:
        print(name[i])
        result = result + name[i]
        print ('result changed to: ' +result)

print ('the final result is: ' +result)

print (name[-8])
print("")
print("")

Fname = input("what is your first name? ")
Mname = input('what is your middle name? ')
Lname = input('what is your last name? ' )
print ("hello " + Fname + " " + Mname+ " " + Lname+ " its nice to meet you")

print("")
print("")

your_number = input("what is your favorite number? ")
your_numbers = int(your_number)
print("though I like your number of " + str(your_numbers) )
better_number = your_numbers + 1
print (" I think " + str(better_number) + " is better")

print("")
print("")

angry_boss = input ("Angry Boss: What do YOU want?!! ")
print ("WHDDAYA MEAN '" + str(angry_boss) + "'?!? YOU'RE FIRED!!!")

print("")
print("")
print("-----")


print("##Week1 day 4. Numbers and Letters")
#A Few Things to Try--
#“99 Bottles of Beer on the Wall.”
#Write a program that prints out the lyrics to that beloved classic,
#“99 Bottles of Beer on the Wall.”

i = 99
while i > 1:
    print (i , " bottles of beer onn the wall" , i , "bottles of beer. take one down. pass it around. ", i , " bottles of beer on the wall.")
    i = i -1 
print("")
print("")

#Deaf grandma. Whatever you say to Grandma (whatever you type in),
#she should respond with this: HUH?! SPEAK UP, GIRL!

text = ""
print ("Hi, there hunny. What's on your mind? ")
while text != "BYE":
    text = input("WHATS THAT YOU SAY GIRL??? CANT HEAR YOU! SPEAK UP! ")
    if text == "BYE":
        print ("NO, NOT SINCE " , random.randint(1930,1950))
        break
    if text == "bye":
        print ("NO, NOT SINCE " , random.randint(1930,1950))
        break
print("")
print("")
#Leap years. Write a program that asks for a starting
#year and an ending year and then puts all the leap years
#between them (and including them, if they are also leap
#years). Leap years are years divisible
#by 4 (like 1984 and 2004). However, years divisible by
#100 are not leap years (such as 1800 and 1900) unless
#they are also divisible by 400 (such as 1600 and 2000,
#which were in fact leap years). What a mess!

year = int(input("Pleat enter a year to check: "))

if (year %400 == 0):
    print (year, "is a lead year")
elif (year %100 ==0):
    print (year , "is NOT a leao year")
elif (year %4 == 0 ):
    print (year, "is a lear year")
else:
    print (year , "if NOT a leap year")

print("")
print("")
print("")

#Optional program about my drive home
print("this will be a program about my drive home. if its super long im going to do something else for a bit.")
drive_time = int(input("How long is the drive today? (in minutes)"))
        
if (drive_time < 35):
    print (drive_time , " minutes??! go straight home! traffic is amazing")
elif (drive_time > 31 or drive_time < 45):
    print (drive_time , " minutes isnt bad but not great... better get going")
elif (drive_time > 46 or drive_time < 60):
    print (drive_time, " minutes is roung.. might consider something else for a bt")
else:
    print ("dont bother. go to the gym. the drive time is to long and annoying")

                 
print("")
print("")
print("-----")

#sorting user input
#created empty list
user_words = []
text = ""

print ("Please give one word... ")
while text != "end" or text == "":
    text = str(input("Please enter another or type 'end' or leave the entry blank and press Enter to quit "))
    user_words.append(text)

    #ends if user enters "end" or leaves input feild blank
    if text == "end" or text == "":
        #print ("ok bye")
        break
print ('user words were: ')
user_words.sort();
print (user_words)


print("")
print("")
print("-----")


#Table of contents.
content_table= [['Chap 1', 10],
                ['Chap 2', 20],
                ['Chap 3', 30],
                ['Chap 4', 40],
                ['Chap 5', 50]]
print ("Table of Contents")
print (": Chapter Title : Page Number :")

for item in content_table:
    print (":", item[0]," "*(12-len(item[0])), ":"," "*(10-len(str(item[1]))), item[1], ":")



print("")
print("")
print("-----")

#Write a function that prints out "moo" n times.

def moo(count):
    i = count
    while i > 0:
        #print ("moo")
        i = i -1
        print ("moo")

moo_count = int(input("How many times should the cow 'moo'?? "))
moo(moo_count)



print("")
print("")
print("-----")

#Old-school Roman numerals.
#I had trouble with this one and spent some time Googling ways that people handled it.
#this video was clean in its explnations as to what he was doing so I used it as a walk through
#https://www.youtube.com/watch?v=rOVmydb5D5I

numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def converter(count):
    #prints out each number and its rNumeral
    #for k,v in numerals.items():
    #    print (k,v)

    if count >1000:
        print ("number entered is too large")
        return 
    
    range_flag = None
    for symbol, integer in numerals.items():
        if integer == count: return symbol
        if count > integer:
            range_flag = symbol #checks if the unput number is 0-1000
    remaining = count - numerals[range_flag]
    
    return range_flag + converter(remaining)#takes remainder and reenters it inot the converter

#gets input from user
number = int(input("Pick a number 1-1000: "))
print (converter(number))



#Modern Roman numerals.
#got this iteration I decided to take a different

def integerToRoman(A):
        #defines roman numeral numers and their value
	romansDict ={ 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 5000: "G", 10000: "H"}

        #function to determine how many 10th are in a given number 
	div = 1
	while A >= div:
		div *= 10

	div /= 10
	res = ""

        #takes the input number and comairs its location to the roman numeral to give an output of the roman numeral
	while A:
                #
		lastNum = int(A / div)

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

		A = math.floor(A % div)
		div /= 10
		
	return res

#gets input from user
number = int(input("Pick a number 1-1000: "))
print (integerToRoman(number))
