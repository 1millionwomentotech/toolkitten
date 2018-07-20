#DAY1

#Write a program that tells you the following:


# 1. Hours in a year. How many hours are in a year?
year=365
day=24
print('there are',year*day,' hours in a year')

print('')
# 2. Minutes in a decade. How many minutes are in a decade?
min=60
hr=24
day=365
mins=day*hr*min
print('there are ',mins+2,'-',mins+3,' minutes in a decade, assuming 2-3 leap years')

print('')
# 3. Your age in seconds. How many seconds old are you? 
from datetime import datetime
today=datetime.now()
fakebd=datetime(1999,1,1,12,0,0,0)
diff=today-fakebd
days=diff.days
secs=diff.seconds

print('my made up age in seconds:',days*24*60*60+secs)




#DAY2
print('')
# 1.Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. 
#   Finally, it should greet the person using their full name.
first=input('enter your first name:')
middle=input('enter your middle name:')
last=input('enter your last name:')
print('Hello,',first,middle,last)

print('')
#2.  Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, 
#    and then suggest the result as a bigger and better favorite number. 
favorite=input('enter your favorite number:')
favorite=int(favorite)
favoriteplus=favorite+1
print('A bigger and better favorite number is:',favoriteplus)


#DAY4


#1. 99 Bottles of beer on the wall
print('')
## simple shout to grandma
you='xx'
while(you!='BYE'):
	you=input('shout to granma:')
	uppers = [l for l in you if ord(l) >= 65 and ord(l) <= 90] 

	if (len(uppers)!=len(you)):
		print('HUH?!SPEAK UP, GIRL!')
	else:
		print('NO,NOT SINCE 1938!')

print('')
## extended shout to grandma

you='xx'
count=0
while(you!='BYE' or count<3):

	print('')
	you=input('extended shout to granma:')
	print('')
	uppers = [l for l in you if ord(l) >= 65 and ord(l) <= 90] 

	if (len(uppers)!=len(you)):
		print('deaf grandma: HUH?!SPEAK UP, GIRL!')
	else:
		print('deaf grandma: NO,NOT SINCE 1938!')
	if you=='BYE':
		count+=1
	if you!='BYE':
		count=0


print('')
# leap years
start=int(input('start year: '))
fin=int(input('end year: '))
print('between the years',start,' and ',fin,'the leap years are:')
for i in range (start,fin+1):
	div4=i%4
	div100=i%100
	if (div4==0 and div100!=0):
		print(i)

print('')
#something in life

from decimal import Decimal
vehicle=250
killed=int(vehicle*10**6/5)
print('There are ~',vehicle,' million vehicles in the US')
print('assume every 1 out of 5 vehicle hit an animal on the road per year')
print('there would be','%.E' % Decimal(killed),' roadkills per year in the US')

