from datetime import datetime

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
answer = input("\n" + name + " what the hell do you want? ")
print(("whaddaya mean \"" + answer + "\"?!? you're fired!!").upper())

# 11. Table of contents. Here's something for you to do in order to play around more with center, ljust, and rjust:
# write a program that will display a table of contents so that it looks like this:


# 12. Write a program that prints out the lyrics to that beloved classic, "99 Bottles of Beer on the Wall."


# 13. Deaf grandma.
# Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL!
# unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:
# NO, NOT SINCE 1938!
# To make your program really believable, have Grandma shout a different year each time,
# maybe any year at random between 1930 and 1950.
# You can’t stop talking to Grandma until you shout BYE.
# Hint: Try to think about what parts of your program should happen over and over again.
# All of those should be in your while loop.
# Hint: People often ask me, "How can I make random give me a number in a range not starting at zero?"
# But you don’t need it to. Is there something you could do to the number random returns to you?


# 14. Deaf grandma extended. What if Grandma doesn't want you to leave?
# When you shout BYE, she could pretend not to hear you.
# Change your previous program so that you have to shout BYE three times in a row.
# Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.


# 15. Leap years.
# Write a program that asks for a starting year and an ending year and
# then puts all the leap years between them (and including them,
# if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004).
# However, years divisible by 100 are not leap years (such as 1800 and 1900)
# unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!


# 16. Find something today in your life, that is a calculation.
# Go for a walk, look around the park, try to count something.
# Anything! And write a program about it. e.g. number of stairs, steps, windows,
# leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.


# 17. Building and sorting an array. Write the program that asks us to type as many words as we want
# (one word per line, continuing until we just press Enter on an empty line)
# and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example,
# does hitting Enter on an empty line always exit your program? Even on the first line? And the second?
# Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it!


# 18. Table of contents. Write a table of contents program here.
# Start the program with a list holding all of the information for your table of contents
# (chapter names, page numbers, and so on).
# Then print out the information from the list in a beautifully formatted table of contents.
# Use string formatting such as left align, right align, center.

# 19. Old-school Roman numerals. In the early days of Roman numerals,
# the Romans didn't bother with any of this new-fangled subtraction “IX” nonsense.
# No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.

# 20. Write a method that when passed an integer between 1 and 3000 (or so)
# returns a string containing the proper old-school Roman numeral.
# In other words, old_roman_numeral 4 should return 'IIII'.
# Make sure to test your method on a bunch of different numbers.
# Hint: Use the integer division and modulus methods.
# For reference, these are the values of the letters used:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# 21. “Modern” Roman numerals.
# Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you
# had to subtract the smaller one. As a result of this development, you must now suffer.
# Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4,
# it should return 'IV', 90 should be 'XC' etc.
