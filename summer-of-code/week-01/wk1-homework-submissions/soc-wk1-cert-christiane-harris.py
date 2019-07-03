'''........................................................................
Week 1 Day 1
32- and 64-bit Timeout
'''

# 32 bits: maximum representable value 2^32 − 1 = 4,294,967,295
# 64 bits: maximum representable value 2^64 − 1 = 18,446,744,073,709,551,615

# Convert 4294967295 seconds to days
print("A 32-bit system will time out in", 4294967295 / 24 / 60 / 60, "days.")

# Convert 18446744073709551615 to days
print ("A 64-bit system will time out in", 18446744073709551615 / 24 / 60 / 60,
       "days.")


'''........................................................................
Week 1 Day 1
Age in Seconds Calculator
'''

# My birth time: sometime in the afternoon. Let's say 2:00pm, or 14:00
# on July 5, 1995.

import time
import datetime

today = datetime.datetime.today()
birthday = datetime.datetime(1995, 7, 5)
answer = (today-birthday).total_seconds()

print("I believe I am", answer, "seconds old.")

# Checking work (roughly)
print("I am", answer / 3600 / 24 / 365, "years old.")



'''........................................................................
Week 1 Day 3
Angry Boss
'''

print("BOSS: Whaddya want? Come on, spit it out!")
response = input("YOU: ")
print('BOSS: WHADDAYA MEAN, "' + response.upper() + "?!? YOU'RE FIRED!!")



'''........................................................................
Week 1 Day 3
Bigger, better favorite number.
'''


fave_num = int(input("What is your favorite number? "))
print("That's a great number, but may I suggest",fave_num+1,"?")

# Question: why does my output have a space between fave_num and the "?"?


'''........................................................................
Week 1 Day 3
Full Name Greeting.
'''

first = input("What is your first name? ")
middle = input("What is your middle name? ")
last = input("What is your last name? ")

print("Hello,", first , middle , last + "!")


'''........................................................................
Week 1 Day 3
Table of Contents
'''

# I'll use 70 characters for the width.
print("Table of Contents".center(70))

print("Chapter 1: Getting Started" + "page 1".rjust(44))
print("Chapter 2: Numbers".ljust(64) + "page 9")
print("Chapter 3: Letters".ljust(63) + "page 13")


'''........................................................................
Week 1 Day 4
99 Bottles of Beer on the Wall
'''

num = 99
while num > 1:
    print(num, "bottles of beer on the wall!")
    print(num, "bottles of beer!")
    print("Take one down, pass it around,")
    print(num - 1, "bottles of beer on the wall!")
    print("")
    num = num - 1

print("1 bottle of beer on the wall!")
print("1 bottle of beer!")
print("Take one down, pass it around,")
print("No bottles of beer on the wall!")


'''........................................................................
Week 1 Day 4
Array
'''

word = input("Type as many words as you want, pressing Enter after each "
             "word. ")
sentence = []

while word != "":
    sentence.append(word)
    word = input()

print("Alphabetized list of your words:", sorted(sentence))
    

'''........................................................................
Week 1 Day 4
Custom Calculation
'''

# Number of Bugs in the Cabin

command = input("How many bugs do you see? Press Enter whenever you see one.\n"
              "If you would like to know how many bugs you've seen so far,\n"
              "type, 'AMOUNT.'\n"
              "If you are sick of counting bugs, type, 'DONE.'\n")
tally = 0

while command != "DONE":
    # Add to tally if user presses Enter key
    if command == "":
        tally += 1
    # Tell user how many bugs they've seen upon request
    elif command == "AMOUNT":
        print("You've seen", tally, "bug(s)!")
    # Catch bad input
    else:
        print("Please press the Enter key, type 'AMOUNT', or type 'DONE.' ")

    command = input()


'''........................................................................
Week 1 Day 4
Deaf Grandma
'''

import random

statement = input("Say something to Grandma. ")
bye_count = 0

while bye_count >= 0:
    # Grandma can't hear the first two "BYE"s...
    if statement == "BYE":
        bye_count += 1
        if bye_count == 3:
            break
        print("HUH?! SPEAK UP, GIRL!")
    # ...but she can hear you if you shout anything else.
    elif statement == statement.upper():
        bye_count = 0
        print("NO, NOT SINCE", random.randint(1930, 1950), "!")
    # Grandma can't hear you at all if you don't shout.
    else:
        bye_count = 0
        print("HUH?! SPEAK UP, GIRL!")

    statement = input("")



'''........................................................................
Week 1 Day 4
Leap Years
'''

start_year = int(input("What year do you want to start with? "))
end_year = int(input("What year do you want to end with? "))

print("Here are all the leap years in between:")

for year in range (start_year, end_year + 1):
    if year % 100 == 0 and not year % 400 == 0:
        pass
    elif year % 4 == 0:
        print(year)


'''........................................................................
Week 1 Day 4
Moo Function
'''

n = int(input("How many times would you like to see the word 'moo'? "))
print("You got it!")
print("moo " * n)


'''........................................................................
Week 1 Day 4
Roman Numerals
'''

                          # " O L D   S C H O O L "
letters = "IVXLCDM"

def old_school_RN(num):
    i = 0
    RN = ""
    # Iterates backward through num as string (starts with one's place)
    for digit in str(num)[::-1]:
        digit_int = int(digit)
        # Adds appropriate letters to front of Roman numeral string (RN)
        if digit_int < 5:
            RN = letters[i] * digit_int + RN
        # Accounts for digits 5 and above (i.e., "VI" instead of "IIIIII")
        else:
            RN = letters[i+1] + letters[i] * (digit_int-5) + RN
        i += 2
    return RN

print("6 is", old_school_RN(6), "in old school Roman numerals.")
print("47 is", old_school_RN(47), "in old school Roman numerals.")
print("980 is", old_school_RN(980), "in old school Roman numerals.")
print("2694 is", old_school_RN(2694), "in old school Roman numerals.")


                                # M O D E R N
def modern_RN(num):
    '''Same as above, except accounts for when digit is a 9.'''
    i = 0
    RN = ""
    for digit in str(num)[::-1]:
        digit_int = int(digit)
        if digit_int < 5:
            RN = letters[i] * digit_int + RN
        elif 5 <= digit_int < 9:
            RN = letters[i+1] + letters[i] * (digit_int-5) + RN
        # Accounts for a 9 digit
        else:
            RN = letters[i] + letters[i+2] + RN
        i += 2
    return RN

print("6 is", modern_RN(6), "in Roman numerals.")
print("47 is", modern_RN(47), "in Roman numerals.")
print("80 is", modern_RN(980), "in Roman numerals.")
print("2694 is", modern_RN(2694), "in Roman numerals.")


'''........................................................................
Week 1 Day 4
Table of Contents II
'''

info = ["Table of Contents",
        ["Chapter 1: Getting Started", "Chapter 2: Numbers", "Chapter 3: Letters"],
        ["page 1", "page 9", "page 13"]]


# I'll use 70 characters for the width.
print(info[0].center(70))

print(info[1][0].ljust(64) + info[2][0])
print(info[1][1].ljust(64) + info[2][1])
print(info[1][2] + info[2][2].rjust(53))
