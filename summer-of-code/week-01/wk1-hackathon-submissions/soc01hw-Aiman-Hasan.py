#day1 questions
print('There are ' + str(24*365) + ' hours in a year \n')
print('There are ' + str(24*365*60*10) + ' minutes in a decade')
print('I am ' + str(20*365*24*60*60) + ' seconds old')
print('Andreea Visanoiu\'s age is ' + str(48618000/(60*60*24*365)) + ' years old' )
print('A 32-bit system will take ' + str(int('11111111111111111111111111111111',2)/(60*60*24)) + ' days')
a = '11111111111111111111111111111111'
b = a*2
print ('A 64-bit system will take ' + str(int(b,2)/(60*60*24)) + ' days')

import datetime

current = datetime.datetime.now()
mydate = datetime.datetime(1998,6, 10, 12, 0)
diff = current - mydate

print('I am ' + str(diff.days/365.5) + ' years old')

#day3 questions

##firstname = input("Enter your first name\n")
##middlename = input("Enter your middle name\n")
##lastname = input("Enter your last name\n")
##
##print("Hi, " + firstname + " " + middlename + " " + lastname + "!")
##
##num = input("Enter your favorite number")
##
##print("Okay! But " + str(num+1) + "is more cool :p")

##request = input("What do you want, mister?\n")
##
##print('WHADDAYA MEAN "' +  request.upper() + '"?!? YOU\'RE FIRED!!')

#day4 questions

#99 bottles of bear
str1 = " bottles of beer"
str11 = " bottle of beer"
str2 = " on the wall"
str3 = "Take one down and pass it around, "
for i in range(99,-1,-1):
    strf = str(i) + str1
    strf2 = ""
    strf3 = strf
    if i == 1:
        strf = str(i) + str11
        strf2 = 'no more' + str1
        
    elif i == 0:
        strf = 'No more' + str1
        strf3 = 'no more' + str1
        str3 = 'Go to the store and buy some more, '
        strf2 = '99' + str1
    else:
        strf2 = str(i-1) + str1
        if (i-1) == 1:
            strf2 = str(i-1) + str11
    
    print(strf + str2 + ', ' + strf3 + '.\n' + str3 + strf2 + str2 + '.\n' )


#Write a function that prints out "moo" n times.
n = int(input(("Enter the number of times you want to print moo\n")))
for i in range(n):
    print("moo")

def old_roman_numeral(number):
    i = 0
    v = 0
    x = 0
    l = 0
    c = 0
    d = 0
    m = 0
    if number >= 1000:
        m = number//1000
        number = number % 1000

    if number >= 500:
        d = number//500
        number = number % 500


    if number >= 100:
        c = number//100
        number = number % 100

    if number >= 50:
        l = number//50
        number = number % 50

    if number >= 10:
        x = number//10
        number = number % 10

    if number >= 5:
        v = number//5
        number = number % 5

    if number < 5:
        i = number//1
        number = number % 10

    return (m * "M") + (d * "D") + (c * "C") + ("L" * l) + ("X" * x) + ("V" * v) + ("I" * i)
  
print(old_roman_numeral(9))

set_of_roman_numerals = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)
]


def roman_numeral(number):
    """ Convert an integer to Roman
    >>> print(convert_to_roman(45))
    XLV """
    roman_numerals = []
    for numeral, value in set_of_roman_numerals:
        while value <= number:
            number -= value
            roman_numerals.append(numeral)

    return ''.join(roman_numerals)

print(roman_numeral(90))
