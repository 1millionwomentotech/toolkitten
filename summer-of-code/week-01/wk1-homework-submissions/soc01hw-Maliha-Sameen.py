### Week 1 Day 1 Homework

## Question 1: Hours in year?
print("Hours in Common Year: ", 365 * 24)
print("Hours in Leap Year: ", 366 * 24)

## Question 2: Minutes in decade?
print("Minutes in Decade: ", (8 * 365 + 2 * 366) * 24 * 60)

## Question 3: Age in seconds?
print("My Age in Seconds: ", 19 * 365 * 24 * 60 * 60)

## Question 4: 48618000 seconds to years?
print("Andreea Visanoiu​ age: ", 48618000 /60/60/24/365)

## Question 5: How many days does it take for a 32-bit 
## system to timeout, if it has a bug with integer overflow?
print ("32-bit system timeout days: ", round((2**32)/1000/60/60/24))

## Question 6: 64-bit system?
print ("64-bit system timeout days: ", round((2**64)/1000/60/60/24))

## Question 7: Calculate exact age based on DOB?
import datetime as dt

dob = dt.date(1999,1,23)
year = str(dt.date.today().year - dob.year)
month = str(dt.date.today().month - dob.month)
day = str(dt.date.today().day - dob.day)

print("I'm",year,"years",month, "months", day, "days old.", sep=" ")