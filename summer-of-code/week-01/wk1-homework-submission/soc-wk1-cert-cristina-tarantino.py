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
while True:
    try:
        favorite_number = int(input("\n" + name + " could you please type your favourite number? "))
    except ValueError:
        print("That wasn't a number!")
        continue
    else:
        big_favorite_number = str(favorite_number + 1)
        print("I have for you a bigger and better favourite number. What about a nice %s." % big_favorite_number)
        break


# 10. Angry boss. Write an angry boss program that rudely asks what you want.
# Whatever you answer, the angry boss should yell it back to you and then fire you.
answer = input("\n" + name + " what the hell do you want? ")
print(("whaddaya mean \"" + answer + "\"?!? you're fired!!").upper())
