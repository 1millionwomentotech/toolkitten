# Week 1, Day 4 Homework

# 99 Bottles Of Beer

beer_Num = 99

while beer_Num > 2:
    print(str(beer_Num) + " bottles of beer on the wall, " + str(beer_Num) + " bottles of beer!")
    next_beer_Num = beer_Num - 1
    print("Take one down, pass it around, " + str(next_beer_Num) + " bottles of beer on the wall!")
    beer_Num = next_beer_Num

if beer_Num == 2:
    print(str(beer_Num) + " bottles of beer on the wall, " + str(beer_Num) + " bottles of beer!")
    next_beer_Num = beer_Num - 1
    print("Take one down, pass it around, " + str(next_beer_Num) + " bottle of beer on the wall!")
    beer_Num = next_beer_Num

if beer_Num == 1:
    print(str(beer_Num) + " bottle of beer on the wall, " + str(beer_Num) + " bottle of beer!")
    next_beer_Num = beer_Num - 1
    print("Take one down, pass it around, no more bottles of beer on the wall!")
    beer_Num = next_beer_Num

# Deaf Grandma Stage 1

print()
print("Say hello to Deaf Grandma!")

import random

grandkid_Says = input()
all_Caps = grandkid_Says.isupper()
#escape_Clause = str(BYE)
rando_Year = random.randint(1930, 1951)

while grandkid_Says != "BYE":
    if all_Caps == False:
        print("HUH?! SPEAK UP, GIRL!")
    else:
        print("NO, NOT SINCE " + str(random.randint(1930, 1950)))
    print()
    print("Say hello to Deaf Grandma!")
    grandkid_Says = input()
    all_Caps = grandkid_Says.isupper()

print("BYE! SEE YOU SOON!")

# Deaf Grandma Stage 2

print()
print("Say hello to Deaf Grandma Stage 2!")

import random

grandkid_Says = input()
all_Caps = grandkid_Says.isupper()
count = 1

while count < 3:
    if grandkid_Says == "BYE":
        print("NO, NO, STAY!")
        print()
        print("Say hello to Deaf Grandma!")
        grandkid_Says = input()
        all_Caps = grandkid_Says.isupper()
        count = count + 1
    else:
        count = 1
        if all_Caps == False:
            print("HUH?! SPEAK UP, GIRL!")
        else:
            print("NO, NOT SINCE " + str(random.randint(1930, 1950)))
        print()
        print("Say hello to Deaf Grandma!")
        grandkid_Says = input()
        all_Caps = grandkid_Says.isupper()

print("I LOVE *nSYNC! SEE YOU SOON!")

# Leap Year Calculator

print()

ending_Year = 0
starting_Year = 1
leap_Year_Count = 0
sum_Year = 0

while ending_Year < starting_Year:
    starting_Year = int(input("Let's count some leap years! Please enter your starting year: "))
# starting_Year = input()

    ending_Year = int(input("Awesome! Now enter your ending year: "))
# ending_Year = input()

    if starting_Year <= ending_Year:

        # test for starting leap
        if starting_Year % 4 == 0:
            if starting_Year % 100 == 0 and starting_Year % 400 == 0:
                leap_Year_Count = leap_Year_Count + 1
                sum_Year = sum_Year - 1
#            else:
#                leap_Year_Count = leap_Year_Count + 1

        # test for ending leap
        if ending_Year % 4 == 0 and ending_Year != starting_Year:
            if ending_Year % 100 == 0 and ending_Year % 400 == 0:
                leap_Year_Count = leap_Year_Count + 1
                sum_Year = sum_Year - 1
#            else:
#                leap_Year_Count = leap_Year_Count + 1

        sum_Year = sum_Year + int((ending_Year - starting_Year) / 4)
        leap_Year_Count = leap_Year_Count + sum_Year
        print("Total number of leap years is " + str(leap_Year_Count))

    else:
        print("Oops, we're not going back in time! Try again.")

# List Building

# List Building

list_Item = []

print("Let's make a list then sort it alphabetically!")
print("Please enter as many items as you like, then press ENTER to sort:")

word = input()
while word != "":
    list_Item.append(word)
    word = input()

for l in sorted(list_Item):
    print(l)

# Print Moo Function

def print_Moo(n):
    print("Moo" * n)

print_Moo(int(input('How many times would you like me to say "Moo"? ')))

# Conversion To Old Roman Numerals

ent_Val = int(input("Please enter a number between 1 to 3000: "))
rom_Num = ""

if (1 <= ent_Val <= 3000) == False :
    print("Sorry, please try again.")

else:
    m_Val = int(ent_Val / 1000)
    if m_Val != 0:
        rom_Num = rom_Num + str("M" * m_Val)
    ent_Val = ent_Val - (m_Val * 1000)
    d_Val = int(ent_Val / 500)
    if d_Val != 0:
        rom_Num = rom_Num + str("D" * d_Val)
    ent_Val = ent_Val - (d_Val * 500)
    c_Val = int(ent_Val / 100)
    if c_Val != 0:
        rom_Num = rom_Num + str("C" * c_Val)
    ent_Val = ent_Val - (c_Val * 100)
    l_Val = int(ent_Val / 50)
    if l_Val != 0:
        rom_Num = rom_Num + str("L" * l_Val)
    ent_Val = ent_Val - (l_Val * 50)
    x_Val = int(ent_Val / 10)
    if x_Val != 0:
        rom_Num = rom_Num + str("X" * x_Val)
    ent_Val = ent_Val - (x_Val * 10)
    v_Val = int(ent_Val / 5)
    if v_Val != 0:
        rom_Num = rom_Num + str("V" * v_Val)
    ent_Val = ent_Val - (v_Val * 5)
    i_Val = int(ent_Val / 1)
    if i_Val != 0:
        rom_Num = rom_Num + str("I" * i_Val)

    print(rom_Num)

# Conversion to New Roman Numerals

    ent_Val = int(input("Please enter a number between 1 to 3000: "))
    rom_Num = ""

    if (1 <= ent_Val <= 3000) == False :
        print("Sorry, please try again.")

    else:

        m_Val = int(ent_Val / 1000)
        if m_Val != 0:
            rom_Num = rom_Num + str("M" * m_Val)
        ent_Val = ent_Val - (m_Val * 1000)
        cm_Val = int(ent_Val / 900)
        if cm_Val != 0:
            rom_Num = rom_Num + str("CM")
            ent_Val = ent_Val - 900
        d_Val = int(ent_Val / 500)
        if d_Val != 0:
            rom_Num = rom_Num + str("D" * d_Val)
        ent_Val = ent_Val - (d_Val * 500)
        cd_Val = int(ent_Val / 400)
        if cd_Val != 0:
            rom_Num = rom_Num + str("CD")
            ent_Val = ent_Val - 400
        c_Val = int(ent_Val / 100)
        if c_Val != 0:
            rom_Num = rom_Num + str("C" * c_Val)
        ent_Val = ent_Val - (c_Val * 100)
        xc_Val = int(ent_Val / 90)
        if xc_Val != 0:
            rom_Num = rom_Num + str("XC")
            ent_Val = ent_Val - 90
        l_Val = int(ent_Val / 50)
        if l_Val != 0:
            rom_Num = rom_Num + str("L" * l_Val)
        ent_Val = ent_Val - (l_Val * 50)
        xl_Val = int(ent_Val / 40)
        if xl_Val != 0:
            rom_Num = rom_Num + str("XL")
            ent_Val = ent_Val - 40
        x_Val = int(ent_Val / 10)
        if x_Val != 0:
            rom_Num = rom_Num + str("X" * x_Val)
        ent_Val = ent_Val - (x_Val * 10)
        ix_Val = int(ent_Val / 9)
        if ix_Val != 0:
            rom_Num = rom_Num + str("IX")
            ent_Val = ent_Val - 9
        v_Val = int(ent_Val / 5)
        if v_Val != 0:
            rom_Num = rom_Num + str("V" * v_Val)
        ent_Val = ent_Val - (v_Val * 5)
        iv_Val = int(ent_Val / 4)
        if iv_Val != 0:
            rom_Num = rom_Num + str("IV")
            ent_Val = ent_Val - 4
        i_Val = int(ent_Val / 1)
        if i_Val != 0:
            rom_Num = rom_Num + str("I" * i_Val)

        print(rom_Num)
