from datetime import datetime

days_in_year = 365
days_in_year_leap = 365.2422

# 60 minutes/hour * 24 hours/day
minutes_in_a_day = 60 * 24

# 60 seconds/minute * 60 minutes/hour * 24 hours/day
seconds_in_a_day = 60*60*24

seconds_in_a_year = seconds_in_a_day * days_in_year
seconds_in_a_year_leap = seconds_in_a_day * days_in_year_leap

seconds_in_milliseconds = 1000

# 1. Hours in a year. How many hours are in a year?
# a day has 24h and a year has 365 days
# therefore
# 1 common year = 365 days = (365 days) times (24 hours/day) = 8760 hours
print
print "Hours in a year:"
print(24 * days_in_year)


# 2. Minutes in a decade. How many minutes are in a decade?
# 60 (minutes in 1 hour) times 24 (hours in a day) times 365 times 10 = 5256000 (Integer)
print
print "Minutes in a decade:"
print(minutes_in_a_day * days_in_year * 10)

# If we want to be more accurate though we should know that
# a year is actually 365.2422 making the calculation = to 5259487.68 (Float)
# source https://en.wikipedia.org/wiki/Year#Variation_in_the_length_of_the_year_and_the_day
print
print "Minutes in a decade considering leaps:"
print(minutes_in_a_day * days_in_year_leap * 10)


# 3. Your age in seconds. How many seconds old are you?
print
print "My age in seconds:"
my_age = 32
print(seconds_in_a_year_leap * my_age)


# 4. Andreea is 48618000 seconds old. Calculate her age
andreea_seconds_old = 48618000
print
print "Andreea's age:"
print(andreea_seconds_old / seconds_in_a_year_leap)

# https://github.com/1millionwomentotech/toolkitten/issues/35
print
print "Andreea's corrected age:"
print(andreea_seconds_old / seconds_in_a_year_leap * 24)

# 5. How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# The Binary Register Width of a processor determines the range of values that can be represented.
# The maximum representable value for a 32-bit system will be 2^32-1
# When an arithmetic operation (in this case the increment of a millisecond in the time)
# produces a result larger than the above we will have an `integer overflow`
# To calculate the days it will take to reach that situation for a 32-bit system
# we need to convert 2^32 milliseconds in days by dividing by 1000s then 60s then 60m 24h
# source https://en.wikipedia.org/wiki/Integer_overflow
print
print "Days it will take for a 32-bit system to timeout"
max_value_32 = pow(2, 32)
print(max_value_32 / seconds_in_milliseconds / seconds_in_a_day)

# 5. How many days does it take for a 64-bit system to timeout, if it has a bug with integer overflow?
# The Binary Register Width of a processor determines the range of values that can be represented.
# The maximum representable value for a 32-bit system will be 2^64-1
# When an arithmetic operation (in this case the increment of a millisecond in the time)
# produces a result larger than the above we will have an `integer overflow`
# To calculate the days it will take to reach that situation for a 64-bit system
# we need to convert 2^64 milliseconds in days by dividing by 1000s then 60s then 60m 24h
# source https://en.wikipedia.org/wiki/Integer_overflow
print
print "Days it will take for a 64-bit system to timeout"
max_value_64 = pow(2, 64)
print(max_value_64 / seconds_in_milliseconds / seconds_in_a_day)

# 7. Calculate your age accurately based on your birthday
# https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
print
delta = datetime.now() - datetime(1986, 12, 8, 18, 45)
print "My age is %d seconds" % delta.total_seconds()