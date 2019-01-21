################################################     DAY 1    ###############################################################
#shows you the number of hours in a year
def hoursInAYear(year):
    days = 0
    if(year%4==0):
        if(year%100==0 and year%400 ==0):
        	days = 366
    else:
    	days = 365

    if(days is 366):
        hours = 366*24
    else:
        hours = 365*24
    print('The number of hours in the year ',year,' are ',hours)

#method to check whether a particular year is a leap year or not
def isLeapYear(year):
    days = 0
    if(year%4==0):
        if(year%100 ==0 and year%400==0):
            days = 366
    else:
        days = 365
		
    if(days == 366):
        return 1
    else:
        return 0

#method to calculate the number of minutes in a decade
def minutesInADecade():
    year = int(input("Please enter starting year"))
    count = 0
    for x in range(year,year+10):
        temp = isLeapYear(x)
        count+=temp
    leapYears = count
    nonLeapYears = 10-count
    minutes = leapYears*366*24*60+nonLeapYears*365*24*60
    print('Minutes in the decade from ',year,' to ',year+9,' is ',minutes)

#returns your age in seconds
def ageInSeconds():
    age = int(input("Please enter your age in years"))
    seconds = age*365.25*24*60*60
    print('Age in seconds is ',seconds)

def findAndreeasAge():
    seconds = 486180000
    age = (((seconds/60)/60)/24)/365.25
    print("Andreaa's age is ",age)

#############not sure about the timeout 32bit and 64 bit
#Number of days it takes for a 32-bit system to timeout if it has a bug with integer overflow
def timeout32bit():
    total = 2**31
    days = (((total/1000)/60)/60)/24
    print('Number of days it takes for a 32-bit system to timeout if it has a bug with integer overflow is ',days)

#Number of days it takes for a 64-bit system to timeout if it has a bug with integer overflow
def timeout64bit():
    total = 2**63
    days = (((total/1000)/60)/60)/24
    print('Number of days it takes for a 64-bit system to timeout if it has a bug with integer overflow is ',days)

#method to find your actual age
import datetime
def findActualAge():
    myDate = datetime.datetime(1996,12,4,8,48)
    currentYear = datetime.date.today().strftime("%Y")
    currentMonth = datetime.date.today().strftime("%m")
    currentDay = datetime.date.today().strftime("%d")
    currentHour = 12
    currentMinute = 00
    currentDate = datetime.datetime(int(currentYear),int(currentMonth),int(currentDay),currentHour,currentMinute)
    diff = currentDate - myDate
    print('Actual age is ',diff)
    

print('*********** DAY 1 *************')
year = int(input('Please enter a year '))
hoursInAYear(year)
minutesInADecade()
ageInSeconds()
findAndreeasAge()
timeout32bit()
timeout64bit()
findActualAge()

##############################################################  DAY 3   ##############################################################

#method that return your full name
def fullname():
    first_name = input("What is your first name? ")
    middle_name = input("What is your middle name? ")
    last_name = input("What is your last name? ")
    name = first_name+' '+middle_name+' '+last_name
    print("Your name is "+name)

#returns a bigger better number
def bigger_better_favourite():
    number = int(input("What is your favourite number?"))
    print(str(number+1)+" is a bigger better number though =D")

#angry boss program =D
def angry_boss():
    wanted = input("WHY ARE YOU HERE??? WHADDAYA WANT?")
    print('WHADDAYA MEAN "'+wanted.upper()+'"?!? YOU\'RE FIRED!!')

#prints the table of contents in a fine format
def table_of_contents():
    print('Chapter 1: Getting Started'.ljust(30,' ')+'page 1'.rjust(25,' '))
    print('Chapter 2: Number'.ljust(30,' ')+'page 9'.rjust(25,' '))
    print('Chapter 3: Letters'.ljust(30,' ')+'page 13'.rjust(25,' '))

print('*********** DAY 3 *************')
fullname()
bigger_better_favourite()
angry_boss()
table_of_contents()

######################################################   DAY 4   ##########################################################

def bottles_of_beer():
    for i in range(99,0,-1):
        print(str(i)+ 'bottles of beer on the wall, '+str(i)+' bottles of beer.')
        print('Take one down and pass it around, '+str(i-1)+ ' bottles of beer on the wall.')
    print('No more bottles of beer on the wall, no more bottles of beer.') 
    print('Go to the store and buy some more, 99 bottles of beer on the wall.')

import random
def deaf_grandma():
    print('Tell something to Grandma')
    text = ''
    while(text!='BYE'):
        text = input()
        if text.isupper():
            number = random.randint(1930,1950)
            print('NO, NOT SINCE '+str(number)+'!')
        else:
            print('HUH?! SPEAK UP, GIRL!')

def deaf_grandma_extended():
    print('Tell something to Grandma')
    text = ''
    count = 0
    while count<3:
        text = input()
        number = random.randint(1930,1950)
        if text.isupper() and text =='BYE':
            count +=1
            print('NO, NOT SINCE '+str(number)+'!'+str(count))
        elif text.isupper():
            count = 0
            print('NO, NOT SINCE '+str(number)+'!'+'inside elif')
        else:
            count = 0
            print('HUH?! SPEAK UP, GIRL!')

def leap_years():
    year = int(input('Enter a year '))
    if(year%4==0 and year%100 == 0):
        if(year%400!=0):
            print(str(year)+' is not a leap year')
        else:
            print(str(year)+' is a leap year')
    elif(year%4==0):
        print(str(year)+' is a leap year')
    else:
        print(str(year)+' is not a leap year')

def books_by_bookshelf():
    books = int(input('Enter the estimated number of books per unit'))
    units = int(input('Enter the number of units'))
    total = books*units
    print('Estimated number of books in the bookshelf is '+str(total))

def sort_list():
    print('Enter a word')
    words = []
    text = input()
    while text !='':
        words.append(text)
        words_sorted = sorted(words)
        print(words_sorted)
        text = input()
    print('The sorted list is :')
    print(words_sorted)

def table_of_contents():
    chapter_numbers = ['Chaper 1:','Chaper 2:','Chaper 3:','Chaper 4:']
    chapter_names = ['Intro to Python','Basic Syntax Rules','The First Program','More about the First Program']
    page_numbers = ['1','7','12','16']
    for a in range(4):
        print(chapter_numbers[a].ljust(15,' ')+chapter_names[a].center(40,' ')+page_numbers[a].rjust(6,' '))

def moo():
    n = int(input("Enter the number of times you want to moo "))
    print('moo '*n)

def old_school_roman_numerals(num):
    temp = 0
    num_string = ''
    while num>0:
        if num>=1000:
            temp = num//1000
            num_string +='M'*temp
            num = num%1000  
        if num>500:
            temp = num//500
            num_string +='D'*temp
            num = num%500
        if num>100:
            temp = num//100
            num_string +='C'*temp
            num = num%100
        if num>50:
            temp = num//50
            num_string +='L'*temp
            num = num%50
        if num>10:
            temp = num//10
            num_string +='X'*temp
            num = num%10
        if num>5:
            temp = num//5
            num_string +='V'*temp
            num = num%5
        else:
            temp = num
            num_string +='I'*temp
            break
    print(num_string)




