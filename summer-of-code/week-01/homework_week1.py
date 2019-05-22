#!/usr/bin/env python
"""This is a script containing the homework of week 1."""
# date: 20/08/2018
# author: Roxana Agrigoroaie


######### DAY1: 
# These are the excercises from the class
print(1+2)
# Simple Arithmetic:
print(2*3)
print(5-8)
print(9/2)
print(5* (12-8) + -15)
# There are two other ways of writing the above statement:
# The first one:
print(5 * (12-8) + (-15))
# The second one:
print(5 * (12-8) - 15)

print(98 + (59872 / (13*8)) * -51)
# The above statement should be rewritten as:
print(98 + (59872 / (13*8)) * (-51))
# Modulus
print(10%2)
# Power and bitshift
print(2**8)
print(1<<9)

# A few things to try:
# 1. How many hours are in a year?
# In order to solve this problem we need some variables:
days_in_year = 365
hours_in_day = 24

hours_in_year = hours_in_day * days_in_year
print('There are ' + str(hours_in_year) + ' hours in a year.')

# 2. How many minutes are in a decade?
# For this problem we need some additional information:
years_in_decade = 10
minutes_in_hour = 60
# We already know that there are hours_in_year hours in a year.
# First we find out how many hours are in a decade
hours_in_decade = hours_in_year * years_in_decade
# Next, we can find out how many minutes are in a decade
minutes_in_decade = hours_in_decade * minutes_in_hour

print('There are ' + str(minutes_in_decade) + ' minutes in a decade.')

# 3. How many seconds old are you?
# I was born on the 5th of October, 1990 
# I have 2 decades and 7 years. I have to compute how many minutes are in a
# 7 year

#TODO: add also the months and days.
seconds_in_minute = 60
minutes_in_year = hours_in_year * minutes_in_hour
my_age_in_minutes = 2 * minutes_in_decade + 7 * minutes_in_year
my_age_in_seconds = my_age_in_minutes * seconds_in_minute

print('Being born ')

# 4. Andreea Visanoiu is 48618000 seconds old. Calculate her age.
# She forgot to multiply with 24 for hours in a day. 
# 5. How many days does it take for a 32-bit system to timeout, if it has a 
# bug with integer overflow.

# 6. How about a 64-bit system?

# 7. Calculate your age accurately based on your birthday.
# for this purpose we are going to use the datetime module


####### DAY2
# There was no homework on day 2

####### DAY3


####### DAY4


####### DAY5




