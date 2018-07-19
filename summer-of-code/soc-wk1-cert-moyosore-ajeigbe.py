#This is a program on how to calculate my age in seconds 
hours_in_day=24
days_in_year = 365
hours_in_year= hours_in_day*days_in_year
print ("There are " + str (hours_in_year) + " hours" + " in a year") # number of hours in a year
minutes_in_decade = hours_in_year*10*60
print ("There are " + str (minutes_in_decade) + " minutes" + " in a decade") #number of minutes in a decade 
seconds_in_yr = hours_in_year*360
Age_in_seconds = 23*seconds_in_yr
print ("I am " + str(Age_in_seconds) + " seconds old") #my age in seconds 
A_V_Age_in_seconds = 48618000 #Andreea Visanoiu's age in seconds
A_V_Age= A_V_Age_in_seconds/seconds_in_yr #Andreea's age 
print ("Andreea's age in seconds is " + str(A_V_Age))