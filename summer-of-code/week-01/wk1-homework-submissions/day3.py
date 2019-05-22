#method that return your full name
def fullname():
	first_name = input("What is your first name? ")
	middle_name = input("What is your middle name? ")
	last_name = input("What is your last name? ")
	name = first_name+' '+middle_name+' '+last_name
	print("Your name is "+name)

#returns a bigger better number
def bigger_better_favourite():
	number = int(input("What is your favourite number?"))
	print(str(number+1)+" is a bigger better number though =D")

def angry_boss():
	wanted = input("WHY ARE YOU HERE??? WHADDAYA WANT?")
	print('WHADDAYA MEAN "'+wanted.upper()+'"?!? YOU\'RE FIRED!!')

def table_of_contents():
	print('Chapter 1: Getting Started'.ljust(30,' ')+'page 1'.rjust(25,' '))
	print('Chapter 2: Number'.ljust(30,' ')+'page 9'.rjust(25,' '))
	print('Chapter 3: Letters'.ljust(30,' ')+'page 13'.rjust(25,' '))

def prompt():
	fullname()
	bigger_better_favourite()
	angry_boss()
	table_of_contents()

prompt()
