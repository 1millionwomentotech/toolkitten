
#######Day1 Homework

# Hours in a year
print(365*24)

# Minutes in a decade
print(10*365*24*60)

# My age in seconds
print(21*365*24*60*60)

# @Andreea Visanoiu's age.
print( 48618000 / (365*24*60*60))

# days 32-bit system to timeout
print((2**31) /1000/24/60/60)


# days 64-bit system to timeout
print((2**63) /1000/24/60/60)

########################################################
#######Day3 Homework
print('Enter Your first name')
n1 =input()
print('Enter Your Middle name')
n2 = input()
print('Enter Your last name')
n3 = input()
print(n1+ ' ' + n2 + ' '+ n3)

###############################
print('Enter your favorite number')
num = input()
result= num+1
print(result + ' ' )
print('Bigger, better favorite number')

###############################
request=input("please input your request here: ")
print("WHADDAYA MEAN \""+request+"\"?!? YOU\'RE FIRED!!")

###############################
title="Table of Contents"
capter="Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13"

print(title.ljust(80))
print(capter.center(85))


###############################
# DAY 4 HOMEWORK
i=1
while i != 100:
    print(str(i)+ ' ' +'99 Bottles of Beer on the Wall.')
    i=i+1

print('come back again')

##############################
import random
input1 = ' '
count=0
while input1 !='BYE' or count!=3:
    input1=input()
    if input1=='BYE':
        count=count+1
    else:
        count =0
        
    if input1.islower() or input1=='BYE':
        print('HUH?! SPEAK UP, GIRL!')
    elif input1.isupper():
        print('NO, NOT SINCE'+ ' ' + str(random.randint(1930,1950)))

         
print('SORRY GRANDMA')
##################################
year1=int(input())
year2=int(input())
arr=[]
for i in range (year1,year2):
    if i%4==0 and i%100==0 and i%400==0:
        arr.append(i)
    elif i%4==0:
        if i%100!=0:
            arr.append(i)
        elif i%400 ==0:
            arr.append(i)


for i in range (0,len(arr)):
    print(arr[i])

####################################
#Building and sorting
word=input('Enter a word')
word_list=[]
while word != '':
    word_list.append(word)
    word=input()

print(word_list.sort())
##################

    
    










