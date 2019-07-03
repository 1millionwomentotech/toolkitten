#Day 1:

# Hours in a year. How many hours are in a year?

print(365*24)

8760

#Minutes in a decade. How many minutes are in a decade?

print(10*365*24*60)

5256000

# Your age in seconds. How many seconds old are you? (34 y.o.)

print(34*365*24*60*60)

1072224000

# Andrea is 48618000*24 seconds old. Calculate how old she is.

print((48618000*24)/60/60/24/365)

37

#Here are some tougher questions:

# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?

#An unsigned integer of 32 bits would have a range from 0 to 2**32 - 1
#Because python only has signed integers the range of an integer goes from -(2**31) to 2**31 - 1
#This means 2**31 -1 is the maximum value that can be stored in a 32bits int in Python

print (int(round((2**31 -1)/60/60/24/1000)))

# How about a 64-bit system?

print (int(round((2**63-1)/60/60/24/1000)))

106751991167

# Calculate your age accurately based on your birthday (24-02-1984, 14:00)

import datetime
t = datetime.datetime.now()
print(((t-datetime.datetime(1984,2,24)).total_seconds())-(14*60*60))

1085366084.93





