#hours in a year
var = 24 * 365
print("Hours in an year: " + str(var))

#minutes in a decade
var1 = var * 10 * 60
print("Minutes in a decade: " + str(var1))

#age in seconds
var2 = var * (2018 - 1999) * 60 * 60
print("Age in seconds: " + str(var2))

#full name
print("First Name: ")
var3 = input()

print("Middle Name: ")
var4 = input()

print("Last Name: ")
var5 = input()

print("Welcome " + var3 + " " + var4 + " " + var5)

#favourite number
print("Type in your Favourite Number: ")
var6 = input()
var6 = int(var6) + 1
print("Better Favourite Number for you is: " + str(var6))

#uppercase
print("Enter the new string: ")
var7 = input()
print(var7.upper())

#grandma listens loud
print("Type something so that Grandma listens.")
var8 = input()
if var8.islower() :
    print("HUH?! SPEAK UP, GIRL!")
else :
	print("NO, NOT SINCE 1938!")

#sorting the lists...
var9 = list()
num = input("Enter the number of elements you want to enter: ")
print("Enter the numbers: ")
for i in range(int(num)):
    n = input("Number: ")
    var9.append(str(n))
print('ARRAY: ', var9)

var9.sort()
print('SORTED ARRAY: ', var9)

#Angry Boss
print("Say something to your boss!!!")
var10 = input()
print('Boss replies: WHADDAYA MEAN "' + var10.upper() + '"?!? YOU\'RE FIRED!!')
