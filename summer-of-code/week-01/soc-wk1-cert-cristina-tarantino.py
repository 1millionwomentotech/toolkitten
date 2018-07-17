# 1. Hours in a year. How many hours are in a year?
# a day has 24h and a year has 365 days
# therefore
# 1 common year = 365 days = (365 days) times (24 hours/day) = 8760 hours
print
print "Hours in a year:"
print(24*365)


# 2. Minutes in a decade. How many minutes are in a decade?
# 60 (minutes in 1 hour) times 24 (hours in a day) times 365 times 10 = 5256000 (Integer)
print
print "Minutes in a decade:"
print(60*24*365*10)

# If we want to be more accurate though we should know that
# a year is actually 365.2422 making the calculation = to 5259487.68 (Float)
# source https://en.wikipedia.org/wiki/Year#Variation_in_the_length_of_the_year_and_the_day
print
print "Minutes in a decade considering leaps:"
print(60*24*365.2422*10)


# Seconds in a year
# a year is actually 365.2422 making the calculation = to 31556926.08 (Float)
# source https://en.wikipedia.org/wiki/Year#Variation_in_the_length_of_the_year_and_the_day
print
print "Seconds in a year considering leaps:"
seconds_in_a_year = 60*60*24*365.2422
print(seconds_in_a_year)

# 3. Your age in seconds. How many seconds old are you?
print
print "My age in seconds:"
print(seconds_in_a_year*32)


# 4. Andreea Visanoiu is 48618000 seconds old. Calculate her age
seconds_in_year = 60*60*24*365.2422
andrea_seconds_old = 48618000
print
print "Andreea's age:"
print(andrea_seconds_old/seconds_in_year)
