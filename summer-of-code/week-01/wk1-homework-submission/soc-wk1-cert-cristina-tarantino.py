from datetime import datetime
from random import randint


days_in_year = 365

# year leap. Source https://en.wikipedia.org/wiki/Year#Variation_in_the_length_of_the_year_and_the_day
days_in_year_leap = 365.2422

# 60 minutes/hour * 24 hours/day
minutes_in_a_day = 60 * 24

# 60 seconds/minute * 60 minutes/hour * 24 hours/day
seconds_in_a_day = 60 * 60 * 24

seconds_in_a_year = seconds_in_a_day * days_in_year
seconds_in_a_year_leap = seconds_in_a_day * days_in_year_leap

seconds_in_milliseconds = 1000

# 1. Hours in a year. How many hours are in a year?
# a day has 24h and a year has 365 days
# therefore
# 1 common year = 365 days = (365 days) times (24 hours/day) = 8760 hours
print("\nHours in a year: " + str(24 * days_in_year))

# 2. Minutes in a decade. How many minutes are in a decade?
# 60 (minutes in 1 hour) times 24 (hours in a day) times 365 times 10 = 5256000 (Integer)
print("\nMinutes in a decade: " + str(minutes_in_a_day * days_in_year * 10))

# If we want to be more accurate though we should know that
# a year is actually 365.2422 making the calculation = to 5259487.68 (Float)
# source https://en.wikipedia.org/wiki/Year#Variation_in_the_length_of_the_year_and_the_day
print("\nMinutes in a decade considering leaps: " + str(minutes_in_a_day * days_in_year_leap * 10))

# 3. Your age in seconds. How many seconds old are you?
# 60 seconds/minutes * 60 minutes/hours * 24 hours/days * 365.2422 days/year * 32 year
my_age = 32
print("\nMy age in seconds: " + str(seconds_in_a_year_leap * my_age))

# 4. Andreea is 48618000 seconds old. Calculate her age
# example showing use of escape characters
andreea_seconds_old = 48618000
print('\nAndreea\'s age: ' + str(andreea_seconds_old / seconds_in_a_year_leap))

# https://github.com/1millionwomentotech/toolkitten/issues/35
print("\nAndreea's corrected age: " + str(andreea_seconds_old / seconds_in_a_year_leap * 24))

# 5. How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# The Binary Register Width of a processor determines the range of values that can be represented.
# The maximum representable value for a 32-bit system will be 2^32-1
# When an arithmetic operation (in this case the increment of a millisecond in the time)
# produces a result larger than the above we will have an `integer overflow`
# To calculate the days it will take to reach that situation for a 32-bit system
# we need to convert 2^32 milliseconds in days by dividing by 1000s then 60s then 60m 24h
# source https://en.wikipedia.org/wiki/Integer_overflow
max_value_32 = pow(2, 32)
print("\nDays it will take for a 32-bit system to timeout: " + str(
    max_value_32 / seconds_in_milliseconds / seconds_in_a_day))

# 6. How many days does it take for a 64-bit system to timeout, if it has a bug with integer overflow?
# The Binary Register Width of a processor determines the range of values that can be represented.
# The maximum representable value for a 32-bit system will be 2^64-1
# When an arithmetic operation (in this case the increment of a millisecond in the time)
# produces a result larger than the above we will have an `integer overflow`
# To calculate the days it will take to reach that situation for a 64-bit system
# we need to convert 2^64 milliseconds in days by dividing by 1000s then 60s then 60m 24h
# source https://en.wikipedia.org/wiki/Integer_overflow
max_value_64 = pow(2, 64)
print("\nDays it will take for a 64-bit system to timeout: " + str(
    max_value_64 / seconds_in_milliseconds / seconds_in_a_day))

# 7. Calculate your age accurately based on your birthday
# https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
# example showing %s string variable
delta = datetime.now() - datetime(1986, 12, 8, 18, 45)
print("\nMy age is %d seconds" % delta.total_seconds())


# 8. Full name greeting. Write a program that asks for a person's first name, then middle, and then last.
#    Finally, it should greet the person using their full name.
name = input("\nCould you please type your first name: ")
middle_name = input("Could you please type your middle name: ")
last_name = input("Could you please type your last name: ")

print("\nHello %s %s %s! A really warm welcome to you!" % (name, middle_name, last_name))


# 9. Bigger, better favorite number. Write a program that asks for a person's favorite number.
# Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number.
print("\nEXERCISE Bigger, better favorite number")

# infinite loop
while True:
    # try to convert the input in an integer
    try:
        favorite_number = int(input("\n" + name + " could you please type your favourite number? "))
    # if it is not possible acknowledge the user and continue to prompt him to insert a number
    except ValueError:
        print("That wasn't a number!")
        continue
    # else execute the input manipulation and break the infinite loop
    else:
        big_favorite_number = str(favorite_number + 1)
        print("I have for you a bigger and better favourite number. What about a nice %s." % big_favorite_number)
        break


# 10. Angry boss. Write an angry boss program that rudely asks what you want.
# Whatever you answer, the angry boss should yell it back to you and then fire you.
print("\nEXERCISE Angry boss")

answer = input("\n" + name + " what the hell do you want? ")
print(("whaddaya mean \"" + answer + "\"?!? you're fired!!").upper())


# 11. Table of contents. Here's something for you to do in order to play around more with center, ljust, and rjust:
# write a program that will display a table of contents so that it looks like this:
# Table of Contents
#
# Chapter 1: Getting Started        page 1
# Chapter 2: Numbers                page 9
# Chapter 3: Letters                page 13

print("\nEXERCISE Table of contents")

rows = [
        ["\nTable of Contents",           "\n"],
        ["Chapter 1: Getting Started",  "page 1"],
        ["Chapter 2: Numbers",          "page 9"],
        ["Chapter 3: Letters",          "page 13"]
      ]

# get the length of the longest world from each row in rows and for each word in row + some padding
col_width = max(len(r[0]) for r in rows) + 10  # padding
# for every row in rows
for r in rows:
    # print the first word of the row leaving empty spaces to fill up the column width and then print the second element
    print(r[0].ljust(col_width) + r[1])


# 12. Write a program that prints out the lyrics to that beloved classic, "99 Bottles of Beer on the Wall."
# source http://www.99-bottles-of-beer.net/lyrics.html

print("\nEXERCISE \"99 Bottles of Beer on the Wall.\"")

starter_num = 99

# print the lyrics title
print("\n", (" Lyrics of the song %s Bottles of Beer " % starter_num).center(50, "🍺"), "\n")

# print the lyrics in the loop from 99 to 0
print(" ".join(str("\n" + str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer."
      "\nTake one down and pass it around, " + str(i - 1) + " bottles of beer on the wall.\n")
               for i in range(starter_num, 0, -1)))

# print the end of the lyrics
print("No more bottles of beer on the wall, no more bottles of beer. "
      "\nGo to the store and buy some more, " + str(starter_num) + " bottles of beer on the wall.")


# 13. Deaf grandma.
# Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL!
# unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:
# NO, NOT SINCE 1938!
# To make your program really believable, have Grandma shout a different year each time,
# maybe any year at random between 1930 and 1950.
# You can't stop talking to Grandma until you shout BYE.

print("\nEXERCISE Deaf grandma")

tell_grandma = ""

while tell_grandma != "BYE":
    tell_grandma = input("Tell something to Grandma: ")
    # if tell_grandma.isupper() and not tell_grandma.islower():   =>  this would be semantically more correct however
    # I think that the above method will scan the string tell_grandma twice whilst the one below only once
    if tell_grandma == tell_grandma.upper():
        random_year = randint(1930, 1950)
        print("NO, NOT SINCE %s" % random_year)
    else:
        print("HUH?! SPEAK UP, GIRL!")


# 14. Deaf grandma extended. What if Grandma doesn't want you to leave?
# When you shout BYE, she could pretend not to hear you.
# Change your previous program so that you have to shout BYE three times in a row.
# Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.

print("\nEXERCISE Deaf grandma extended")

tell_grandma = ""
num_bye = 0

while num_bye < 3:
    tell_grandma = input("Tell something to Grandma: ")
    # if tell_grandma.isupper() and not tell_grandma.islower():   =>  this would be semantically more correct however
    # I think that the above method will scan the string tell_grandma twice whilst the one below only once
    if tell_grandma == tell_grandma.upper():
        if tell_grandma == "BYE":
            num_bye = num_bye + 1
        else:
            num_bye = 0
        random_year = randint(1930, 1950)
        print("NO, NOT SINCE %s" % random_year)
    else:
        print("HUH?! SPEAK UP, GIRL!")

if num_bye == 3:
    print("GOODBYE HONEY!!! SEE YOU SOON! I LOVE YOU!")


# 15. Leap years.
# Write a program that asks for a starting year and an ending year and
# then puts all the leap years between them (and including them,
# if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004).
# However, years divisible by 100 are not leap years (such as 1800 and 1900)
# unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

print("\nEXERCISE Leap years ")

print("\nLet's find leap years. Type a range of two years to find all the leap years in the range.")
loop_years = []

# infinite loop
while True:
    # try to convert the input in an integer
    try:
        year_one = int(input("\nPlease type the starting year: "))
        year_two = int(input("\nPlease type the ending year: "))

        # check that year one is minor of year two
        if year_one >= year_two:
            raise ValueError("\nThe starting year must be greater than the ending year!")

    # if it is not possible acknowledge the user and continue to prompt him to insert a number
    except ValueError as error:
        if error:
            print(error)
        else:
            print("\nThat wasn't a valid year!")
        continue

    # else execute the input manipulation and break the infinite loop
    else:
        current_year = year_one
        while current_year <= year_two:
            if current_year % 400 == 0 or (current_year % 4 == 0 and current_year % 100 != 0):
                loop_years.append(current_year)

            current_year += 1

        for y in loop_years:
            print(y)
        break


# 16. Find something today in your life, that is a calculation.
# I had a JavaScript interview today and the question was to perform a left rotation operation on an array.
# For example, if  left rotations are performed on array, then the array would become .
# For example, if 2 left rotations are performed on an array [1, 2, 3, 4, 5],
# then the array would become [3, 4, 5, 1, 2].
# Here is my algorithm:

print("\nEXERCISE FROM YOUR LIFE")


def rot_left(array, rotations_num):
    a_length = len(array)
    new_array = [None]*a_length
    pos_to_left = rotations_num

    i = 0
    while i < a_length:
        pos_to_left = pos_to_left if pos_to_left != 0 else a_length
        to_index = a_length - pos_to_left
        new_array[to_index] = array[i]
        pos_to_left -= 1
        i += 1

    return new_array


print("\nRotate the following array [1, 2, 3, 4, 5] of 2 position to the left")
print(rot_left([1, 2, 3, 4, 5], 2))
print("\nRotate the following array [1, 2, 3, 4, 5] of 4 position to the left")
print(rot_left([1, 2, 3, 4, 5], 4))
print("\nRotate the following array [1, 2, 3, 4, 5] of 5 position to the left")
print(rot_left([1, 2, 3, 4, 5], 5))
print("\nRotate the following array [1, 2, 3, 4, 5] of 6 position to the left")
print(rot_left([1, 2, 3, 4, 5], 6))


# 17. Building and sorting an array. Write the program that asks us to type as many words as we want
# (one word per line, continuing until we just press Enter on an empty line)
# and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example,
# does hitting Enter on an empty line always exit your program? Even on the first line? And the second?
# Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it!

print("\nEXERCISE Building and sorting an array")

word_list = []

user_word = input("\nPlease type as many words as you want one word per line, "
                  "continuing until you press Enter on an empty line "
                  "and I will repeat them to you in alphabetical order: ")

while user_word != '':
    word_list.append(user_word)
    user_word = input()


print(sorted(word_list))

# 18. Table of contents. Write a table of contents program here.
# Start the program with a list holding all of the information for your table of contents
# (chapter names, page numbers, and so on).
# Then print out the information from the list in a beautifully formatted table of contents.
# Use string formatting such as left align, right align, center.

print("\nEXERCISE Table of contents with function and info array")


def print_contents(contents_list):
    # get the length of the longest world from each row in rows and for each word in row + some padding
    col_width = max(len(r[1]) for r in contents_list) + 10  # padding

    print("\nTable of Contents\n")

    for c in contents_list:
        print("Chapter " + c[0] + ": " + c[1].ljust(col_width) + "page " + c[2])


contents_table = [
    ["1", "Getting Started", "1"],
    ["2", "Numbers", "9"],
    ["3", "Letters", "13"],
]

print_contents(contents_table)


# 19. Write a function that prints out "moo" n times.

print("\nEXERCISE moo")


def moo(n):
    print("\nmoo" * n)


# infinite loop
while True:
    # try to convert the input in an integer
    try:
        moos_num = int(input("\nPlease type how many times you want to 'moo': "))
    # if it is not possible acknowledge the user and continue to prompt him to insert a number
    except ValueError as error:
        print("\nThat wasn't a valid number!")
        continue
    # else execute the input manipulation and break the infinite loop
    else:
        moo(int(moos_num))
        break


# 20. Old-school Roman numerals. In the early days of Roman numerals,
# the Romans didn't bother with any of this new-fangled subtraction “IX” nonsense.
# No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
# Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing
# the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'.
# Make sure to test your method on a bunch of different numbers.
#
# Hint: Use the integer division and modulus methods.
#
# For reference, these are the values of the letters used:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

print("EXERCISE Old-school Roman numerals")


def old_romans(number):
    result = ''
    decimal = [1000, 500, 100, 50, 10, 5, 1]
    roman = ["M", "D", "C", "L", "X", "V", "I"]

    # looping over every element of our arrays
    for i in range(len(decimal)):
        # keep trying the same number until we need to move to a smaller one
        while number%decimal[i] < number:
            # add the matching roman number to our result string
            result += roman[i]
            # subtract the decimal value of the roman number from our number
            number -= decimal[i]

    return result


# infinite loop
while True:
    # try to convert the input in an integer
    try:
        user_number = int(input("\nPlease type a number between 1 and 3000: "))
    # if it is not possible acknowledge the user and continue to prompt him to insert a number
    except ValueError as error:
        print("\nThat wasn't a valid number!")
        continue
    # else execute the input manipulation and break the infinite loop
    else:
        print(str(old_romans(user_number)))
        break


# 21. “Modern” Roman numerals.
# Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you
# had to subtract the smaller one. As a result of this development, you must now suffer.
# Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4,
# it should return 'IV', 90 should be 'XC' etc.

print("EXERCISE “Modern” Roman numerals.")


def modern_romans(number):
    result = ''
    decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    # looping over every element of our arrays
    for i in range(len(decimal)):
        # keep trying the same number until we need to move to a smaller one
        while number%decimal[i] < number:
            # add the matching roman number to our result string
            result += roman[i]
            # subtract the decimal value of the roman number from our number
            number -= decimal[i]

    return result


# infinite loop
while True:
    # try to convert the input in an integer
    try:
        user_number = int(input("\nPlease type a number between 1 and 3000: "))
    # if it is not possible acknowledge the user and continue to prompt him to insert a number
    except ValueError as error:
        print("\nThat wasn't a valid number!")
        continue
    # else execute the input manipulation and break the infinite loop
    else:
        print(str(modern_romans(user_number)))
        break

