# soc-wk1-cert-Diana-Ilinca.py

# Day1 homework
#hours in a year:8760
print(365*24)
#minutes in a decade: 5256000
print(60*24*365*10)
#age in seconds:1135296000
print(60*60*24*365*36)
#days 32-bit system to timeout:497
print((2**32-1)/100/60/60/24)
#days 64-bit system to timeout:1067519911673
print((2**63)/100/60/60/24)

Day3 homework
Program that asks for a person's first name, middle and last then greet with full name

firstname = raw_input("What is your first name?")
middlename = raw_input("What is your middle name?")
lastname = raw_input("What is your last name?")
print('Hello there '+firstname+ middlename +lastname+ '!!')

# Program that asks for a person's favourite number, add 1 and suggest the result
fav_number = int(raw_input("What is your favourite number?"))
suggestion = fav_number+1
print('your number is nice. However you might want to consider ' +str(suggestion)+ ' as a new fav. Just a thought..')

#AngryBoss
Boss= raw_input("What do you want this time?!?".upper())
print('SO YOU THINK ' + str(Boss).upper()+' IS A GOOD IDEA??? FIRED!')