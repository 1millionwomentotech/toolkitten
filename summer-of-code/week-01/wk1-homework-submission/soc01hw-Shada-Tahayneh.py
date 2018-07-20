import time
import datetime

print("Number of hours in a year:", end=' ')
# calculate number of hours in a year
print(365 * 24)

print("Number of minutes in a decade: ", end=' ')
# calculate number of minutes in a decade
print( 60 * 24 * 365 * 10)

print("My age in seconds: ", end=' ')
# calculate my age in seconds.
print(60 * 60 * 24 * 365 * 28)


print("Andreea Visanoiu age:", end=' ')
# calculate Andreea Visanoiu age #convert second to year
print(48618000/(60*60*24*365))

print("Number of days that 32 bit system will take to timeout:", end=' ')
# calculate number of days that 32 bit system will take to timeout
print(2**32 - 1)

print("Number of days that 32 bit system will take to timeout:", end=' ')
#calculate number of days that 64 bit system will take to timeout
print(2**64 - 1)

print("My age accuratly based on my birthday:", end=' ')
age = datetime.date(1990,2,15)
year = str(datetime.date.today().year - age.year)
month = str(datetime.date.today().month - age.month)
days = str(datetime.date.today().day - age.day)
print("My age is: " + year + " years and " + month + " months and " + days + " days")


# ask user about his name (first, middle, last)
fname = input("Enter your first name: ")
mname = input("Enter your middle name: ")
lname = input("Enter your last name: ")
print("Hi " + fname + " " + mname + " " + lname, " Nice to meet you ")


# ask user about his favorite number
num = input("What is your favorite number: ")
print("This number is bigger and favorite number: " + str(int(num) + 1))

# Angry boss
request = input("What do you want? ")
print("\""+request.upper()+"\"?!? YOU'RE FIRED!!")


#Day 4
for i in range(1,99):
    print(str(i) + "Bottles of Beer on the Wall")

# if I shout I will get my grandma reply
ask = Input("Deaf grandma .....")
count = 0
while ask != "BYE" or count != 3:
    
    if ask == "BYE":
        count = count + 1
    else:
        count = 0
        
    if ask.islower() or ask == "BYE":
        print("HUH?! SPEAK UP, GIRL!")
    elif ask.isupper():
        print("NO, NOT SINCE " + str(random.radint(1930,1950)))
    ask = Input("Deaf grandma .....")

#Leap year

start_year = int(Input("Enter start year"))
last_year = int(Input("Enter last year"))
leap_year_flag = 0
for i in range(start_year,last_year):
    if i%4 == 0:
        if i%100 == 0:
            if i%400 == 0:
                leap_year_flag = 1
            else:
                leap_year_flag = 0
        else:
            leap_year_flag = 1
    else:
        leap_year_flag = 0
    if leap_year_flag:
        print("Leap Year: " str(i))

#Building and sorting

user_word= input("Enter a word : press Enter to stop and get list sorted")
word_list = {}
while user_word != "":
    word_list.append(user_word)
    user_word= input("Enter a word : press Enter to stop and get list sorted")

if word_list.count == 0:
    print("No word in the list")
else:
    word_list_sorted_array = sorted(word_list)
    print(word_list_sorted_array)


            
        
    


