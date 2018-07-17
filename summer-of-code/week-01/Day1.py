# Day1 homework
import time
from datetime import datetime
x=365*24
print ("1 year has %s hours" %x)


x=365*24/2*60
print ("decade has %s minutes" % x)
print("now ", datetime.now())
today=datetime.now()
x=(today-datetime(1987,1,24,16,15)).total_seconds()
print ("I am %s seconds old" % x )
delta=(datetime.now()-datetime(1970,1,1)).total_seconds()-x+300*60 #From my time zone UTC -5
print("My Birthday: ",datetime.fromtimestamp(delta))

#Andreea Birthday
x=48618000
delta=(datetime(2018,7,16,8,23 )-datetime(1970,1,1)).total_seconds()-x+300*60 # From my time zone UTC -5
print("Andreea Birthday: ",datetime.fromtimestamp(delta))
print("Andreea %s years old" % (x/60/60/24/365))