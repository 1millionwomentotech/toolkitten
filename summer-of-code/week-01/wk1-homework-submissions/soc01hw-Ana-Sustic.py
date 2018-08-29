#soc01hw

#A Few Things to Try
#1 Write a program that tells you the following:
#How many hours are in a year?
def isleapyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
year =int(input('Enter a year:'))
if isleapyear(year):
    print('There are {} hours in year {}.'.format(366*24, year))
else:
    print('There are {} hours in year {}.'.format(365*24, year))

x=input ("Press any key to next homework")

#- Minutes in a decade. How many minutes are in a decade?
print('There are {} in a decade.'.format(10*365*24*60))

x=input ("Press any key to next homework")
#- Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
#- Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.

# 
# print ("Home work 2 title") 
# 
# #do your home work #2 coding here print("code for home work 2 goes here") 
# x=input ("Press any key to next home work") 
# print ("Home work 3 title") print("code for home work 3 goes here") #do your home work #2 coding here # and so on ... the input () is cool way to make a pause and run

