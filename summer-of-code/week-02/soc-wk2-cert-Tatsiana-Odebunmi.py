#Week 2 Day 1 Homework
import string
#Alice_in_wonderland


def count_letters(file_name):
	text=[]
	with open(file_name, encoding='utf-8') as f:#open and reading from file
		text=f.read().upper()
	letters_list=string.ascii_uppercase
	counted_letters=[]
	for letter in letters_list: # For each letter in the alphabet counting appearence in the text
		num=text.count(letter)
		counted=[letter,num]
		counted_letters.append(counted)
	return counted_letters

#Unittesting:
# functions
def secret_formula(started):
	jelly_beans=started*500
	jars=jelly_beans/1000
	crates=jars/100
	return jelly_beans, jars, crates

def break_words(stuff):
	words=stuff.split(' ')
	return words

def sort_words(words):
	return sorted(words)

def full_name(first_name, second_name):
	full_name=first_name+" "+second_name
	return full_name

def calculator(number1,number2, sign):
	if sign=='+':
		result=number1+number2
	elif sign=='-':
		result=number1-number2
	elif sign=='*':
		result=number1*number2
	elif sign=='/':
		result=number1/number2
	else:
		print("Wrong input!!!")
	return result

# Week2 Day 2 homework

#numbers and letters
def print_a_z():

	for letter in range(65,65+2*26+6):

		if letter<(65+26) or letter>=(65+26+6):
			print(letter,"stands for", chr(letter))

	return

# secret message Will transorm just letters, all other caracters will be egnored
def secret_message():
	message=input("Input your message:\n>").upper()
	secret_message=[]

	for letter in message:
		num=ord(letter)

		if num>=65 and num<(65+26):
			secret_message.append(num)

	print(secret_message)

# Caesar cipher function will transorm just letters, all other caracters will be egnored
def secret_message_by_caesar():
	number=input("Please input key number:\n>")
	message=input("Please input you message:\n>").upper()
	secret_message=''

	for letter in message:
		num=ord(letter)

		if num>=65 and num<(65+26):
			char_num=num-int(number)

			if char_num<65:
				char_num+=26

			secret_message+=chr(char_num)

	print(secret_message)
	return

# World of CivilizationIII 
#Function printing world by the line
def print_by_the_line(world):
	
	# to print each element in the line
	for line in world:

		for elem in line:
			print(' '+elem, end='')

		print()

	return

def print_reverse(world):
	
	# to print each element in the line in reverse starts from the end
	line=len(world)-1
	while True:
		colum=len(world[line])-1
		
		while True:
			print(' '+world[line][colum], end='')
			
			if colum==0:
				break
			colum-=1
		
		if line==0:
			break
		line-=1
		print()	
	return


def continent_counter(world,x,y):
	if x >= 0 and y >= 0 and x < len(world) and y < len(world[x]):
		if world[x][y] != 'land' :
			return 0
		# so first we count this tile...
		size = 1
		world[x][y] = 'counted land'
		#then we count all oh the neighboring
		size = size + continent_counter(world, x-1, y-1)
		size = size + continent_counter(world, x, y-1)
		size = size + continent_counter(world, x+1, y-1)
		size = size + continent_counter(world, x-1, y)
		size = size + continent_counter(world, x+1, y)
		size = size + continent_counter(world, x-1, y+1)
		size = size + continent_counter(world, x, y+1)
		size = size + continent_counter(world, x+1, y+1)
		return size
	return 0

#world generator
import random
def world_generator():

	while True:

		try:
			size=int(input("Input the size of world x*x (1...100): "))
			if size>100:
				raise ValueError
			if size<1:
				raise ValueError
			break

		except ValueError:
			print("No valid symbol! Please try again...")

	#randomly filling the world with numbers 0 & 1
	M = 'land'
	o = 'water'
	world=[]
	for x in range(size):
		world_y=[]
		for y in range(size):
			world_y.append(random.choice([o,M]))
		world.append(world_y)
	print(world)
	return world

#Day 3 home work
#working with dictionaries
def working_with_dictionary():
	my_dict={"a": 3500,
	"b": 8000,
	"z": 450}
	print(my_dict)

	#changing item key
	print("changing key a to c")
	my_dict['c']=my_dict['a']
	del my_dict['a']
	print(my_dict)

	# adding item
	print("Added item a: 3800")
	my_dict['a']=3800
	print(my_dict)

	#looping 
	print("goin through all elemnts of dictionary")
	for item, value in my_dict.items():
		print(item, value)

	#get list of keys
	keys=my_dict.keys()
	print("List of keys")
	print(keys)
	return

# Personal info dictionary
def personal_info():
	my_info={'Fullname':'Tatsiana Odebunmi', 'Dicord id': 'Seglya[Gold]' }
	my_info['GitHub username']='Seglya'
	my_info["Country"]="USA"
	my_info["Favorite food"]="Ice cream"
	print(my_info)
	print("Full name: " + my_info['Fullname']+ " Country: " + my_info['Country'])
	print(my_info.keys())
	print(my_info.values() )

	for item, value in my_info.items():
		print(item +": " + value)

	return

# counting letters in Alice and save it in dictinary
def count_letters_dict(file_name):
	text=[]
	with open(file_name, encoding='utf-8') as f:#open and reading from file
		text=f.read().upper()
	letters_list=string.ascii_uppercase
	counted_letters={letter: text.count(letter)
	for letter in letters_list} # For each letter in the alphabet counting appearence in the text
		
	return counted_letters

#Optional Ex #39 LPHW
#create a mapping of states abbreviation
def states_and_cities():
	states = {
	"Pensilvania": "PA",
	"New York": "NY",
	"New Jersey": "NJ",
	"North Carolina": 'NC'
	}

	#states and cities
	cities = {
	"PA": "Philadelphia",
	"NY": "Albany",
	"NJ": "Atlantic City",
	"NC": "Ocean City",
	"PA": "Allentown"
	}

	#adding more cities
	cities['NY']='New York'
	cities['NJ'] = "Jersey City"

	#Printing out some cities
	print('-'*10)
	print("PA state has: ", cities['PA'])
	print("NJ state has: ", cities['NJ'])

	#printing out some states
	print('-'*10)
	print("North Carolina's abbreviation is: ", states['North Carolina'])
	print("New York's abbreviation is: ", states['New York'])

	# do it by using the state then cities dict
	print('-' * 10)
	print("Pensilvania has: ", cities[states['Pensilvania']])
	print("New York has: ", cities[states['New York']])

	# printing every state abbreviation
	print('-' * 10)
	for state, abbrev in list(states.items()):
		print(f"{state} is abbreviated {abbrev}")

	# printing every city in state
	print('-' * 10)
	for abbrev, city in list(cities.items()):
		print(f"{abbrev} has the city {city}")

	# now doing both at the same time
	print('-' * 10)
	for state, abbrev in states.items():
		print(f"{state} state is abbreviated {abbrev}")
		print(f"and has city {cities[abbrev]}")

	print('-' * 10)
	# safely geting a abbreviation by state that might not be there
	state = states.get("Arizona")
	if not state:
		print("Sorry, no Arizona.")

	# geting a city with a default value
	city = cities.get('AZ', 'Does Not Exist')
	print(f"The city for the state 'AZ' is: {city}")

	return

#Classes
class Student():
	def __init__(self, name, discord_id,fav_food,dream):
		self.name=name
		self.discord_id=discord_id
		self.fav_food=fav_food
		self.dream=dream

	def my_print(self):
		print(self.name+self.email+self.dream)

def adding_students():
	students=[]
	students.append(Student("Virginia Balseiro","yesvirginia [Gold] [Volunteer]","Pasta","Moving to europe and working as a dev in a vegan company!!"))
	students.append(Student("Cristina Tatrantino","CristyTarantino[Gold]","Pasta","Being an amazing developer"))
	students.append(Student("Debb Cupitt","","Chocolate","Gender equity"))
	students.append(Student("Marwa Qabeel​","Marwa Qabeel [Gold]","","Data Analyst"))
	students.append(Student("Sacha Young","sacha[Gold]","French Fries","Return to research"))
	students.append(Student("Jessica","Jessi_RS [Gold]","Pasta","Work as developer by the end of the year 😉"))
	students.append(Student("Andreea Visanoiu","Andreea[Gold]","wontonmee","become an University teacher"))
	students.append(Student("Bituin Callanta","bituin [gold]","Sashimi","Lessen the gender wage gap"))
	students.append(Student("Andreea Visanoiu","","become an University teacher"))

#Real world 1mwtt class
class Student_1mwtt():
	def __init__(self, first_name, second_name, 
		date_of_birth,country,time_zone, email, 
		phone_number, discord_id,gitHub_id, level):
		self.first_name=first_name
		self.second_name=second_name
		self.date_of_birth=date_of_birth
		self.country=country
		self.time_zone=time_zone
		self.email=email
		self.phone_number=phone_number
		self.discord_id=discord_id
		self.gitHub_id=gitHub_id
		self.membership=""
		self.level=level

	#method to get full name of student
	def full_name(self):
		return self.first_name + " " + self.second_name

	#Method to update membership
	def update_membership(self, membership):
		self.membership=membership

	#method to define how to print object student
	def __repr__(self):
		return ("\nFull name: " + self.full_name() +
		'\nDate of birth: ' + self.date_of_birth +
		'\nCountry: ' + self.country + 
		'\nTime zone: ' + self.time_zone +
		'\nEmail: ' + self.email + '\nPhone: ' + self.phone_number +
		'\nDiscord username: ' + self.discord_id +
		'\nGitHub username: ' + self.gitHub_id + 
		'\nMembership: ' + self.membership + 
		'\nLevel: ' + self.level)

# EX #40 
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
		
def singing():
	happy_bday = Song(["Happy birthday to you",
		"I don't want to get sued",
		"So I'll stop right there"])
	
	bulls_on_parade = Song(["They rally around tha family",
		"With pockets full of shells"])

	witness_lyrics = Song(["If I lost it all today, would you stay?",
	"Could my love be enough to stimulate?",
	"If shit hit the fan, grenades got thrown",
	"Would you still show, oh?"])

	chainsmokers = Song(["I've been reading books of old",
	"The legends and the myths",
	"Achilles and his gold",
	"Hercules and his gifts"])

	stay = ["Waiting for the time to pass you by",
	"Hope the winds of change will change your mind",
	"I could give a thousand reasons why",
	"And I know you, and you've got to"]

	zedd = Song(stay)
	happy_bday.sing_me_a_song()

	bulls_on_parade.sing_me_a_song()

	print()
	witness_lyrics.sing_me_a_song()

	print()
	chainsmokers.sing_me_a_song()

	print()
	zedd.sing_me_a_song()
	return

	#Day 4 homework
	# Check Week 3 day 1

def main():
	print("Day 1 homework")
	file_name="alice_in_wonderland.txt"
	table=count_letters(file_name)
	print(table)

	print("Day 2 homework")

	print_a_z()
	secret_message()
	secret_message_by_caesar()

	M = 'land'
	o = 'water'
	world = [[o,o,o,o,o,o,o,o,o,o,o],
	[o,o,o,o,M,M,o,o,o,o,o],
	[o,o,o,o,o,o,o,o,M,M,o],
	[o,o,o,M,o,o,o,o,o,M,o],
	[o,o,o,M,o,M,M,o,o,o,o],
	[o,o,o,o,M,M,M,M,o,o,o],
	[o,o,o,M,M,M,M,M,M,M,o],
	[o,o,o,M,M,o,M,M,M,o,o],
	[o,o,o,o,o,o,M,M,o,o,o],
	[o,M,o,o,o,M,o,o,o,o,o],
	[o,o,o,o,o,o,o,o,o,o,o]]

	print_by_the_line(world)

	#printing in reverse
	print("printing in reverse")
	print_reverse(world)
	world=world_generator()
	print(continent_counter(world, len(world)//2, len(world)//2))

	print ("Day 3 homework")

	# working with dictionaries
	working_with_dictionary()

	#dictinary with my info
	personal_info()

	#Alice in wonderland
	print(count_letters_dict(file_name))

	#States and cities
	states_and_cities()

	Creating a new object of my class Student_1mwtt
	student=Student_1mwtt("Tatsiana","Odebunmi",
	"24/01/1987", "USA", "EST", "segl.tanya@gmail.com",
	"+1-570-9999999", "Seglya[Gold]", "Seglya", "Intermediate")
	student.update_membership("Gold")
	print(student)

	#Ex 40
	singing()
	return
main()