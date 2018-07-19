# exercises for week1 day1
print(365*24)	#hours in a year

print(10*365*24*60) 	#minutes in a decade ssimple version
print(28*365*24*60*60)		#my age in secons simple version
print(48618000/60/60/24/365)		#andreas age...

#how many days does it take for a 32 bit system to timeout
milliseconds = 2**32
days = milliseconds/1000/60/60/24
print("days to time out:" + str(days))

#for 64 bit system
milliseconds2 = 2**64
days2 = milliseconds2/1000/60/60/24
print("days to time out:" + str(days2))
