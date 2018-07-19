# Hours in a year
print("1. How many hours are there in a year?")
diy = 365
hid = 24
hours_in_year = diy * hid
print("Ans. There are",hours_in_year,"hours in a year.")

# Minutes in a decade
print("\n2. How many minutes are in a decade?")
years_in_decade = 10
min_in_hour = 60
min_in_decade = years_in_decade * diy * hid * min_in_hour
print("Ans. There are",min_in_decade,"minutes in a decade.")

# Your age in seconds
print("\n.3. How many seconds old are you?")
import time
import datetime
from datetime import timedelta

curr_date = datetime.datetime.now()

date_entry = input('Enter your date of birth in YYYY-MM-DD format : ')
year,month,day = map(int, date_entry.split('-'))

try:
	time_entry = input('Enter the time of birth as HH:MM:SS format : ')
except KeyboardInterrupt:
	time_entry = "00:00:00"
except EOFError:
	time_entry = "00:00:00"
finally:
	hour, minute, second = map(int, time_entry.split(':'))

full_dob = datetime.datetime(year, month, day, hour, minute, second)
diff = curr_date - full_dob
age = diff.total_seconds()
print("Age in seconds: ",age)

#Andreea Visanoiu'age
print("\n4. I'm 48618000 seconds old. Calculate my age.  - @Andreea Visanoiu")
curr_age_in_sec = 48618000
age_in_yr = curr_age_in_sec/(60 * 60 * 24 * 365)
print("Ans. @Andreea's age is",age_in_yr)