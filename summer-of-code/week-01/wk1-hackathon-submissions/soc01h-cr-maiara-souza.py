

# DEAF GRANDMA
import random 

l = ""

while l!="BYE BYE BYE":
  l = input()

  if (l.isupper() and (l != "BYE BYE BYE")):
    print("´NO, NOT SINCE ", random.randint(1930, 1950), "!")
    
  elif l.islower():
    print("HUH?! SPEAK UP, GIRL!")


# SHOW LEAP YEARS 

startyear = int(input())
lastyear = int(input())

for x in range(startyear, lastyear):
   if ((x % 4 == 0)  or (x % 100== 0) or (x % 400== 0)):
    print(x)


# SORT ARRAYS

letters = []
while True:
  l = input()
  letters.append(l)
  letters.sort()

  if not l:
    break
  print(letters)


# SAY MOO N TIMES
n = int(input())


def say_moo():
  print("moo")

for x in range(n):
  say_moo()

# CONVERT INT TO ROMAN NUMBER
nRoman = [(1000, 'M'), 
       (900, 'CM'),
       (500, 'D'), 
       (400, 'CD'), 
       (100, 'C'), 
       (90, 'XC'),
             (50, 'L'), 
             (40, 'XL'), 
             (10, 'X'), 
             (9, 'IX'), 
             (5, 'V'), 
             (4, 'IV'), 
             (1, 'I')]


def inttoRoman(n):

    roman = ''

    while n > 0:
        for i, r in nRoman:
            while n >= i:
                roman = roman + r
                n = n - i

    return roman


x = int(input())
print(inttoRoman(x))





