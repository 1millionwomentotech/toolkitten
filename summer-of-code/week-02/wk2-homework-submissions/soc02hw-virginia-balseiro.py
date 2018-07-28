# DAY 1
# Things to Try
# Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in alice_in_wonderland.txt (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)
# Store the results in a list of lists:
# Hint: use python's lower() method to turn all alphabetic letters into small case and count them (so "A" counts towards "a").
# Hint: Ignore non-alphabetic numbers, you can check with python isalpha() method.

filename = "alice_in_wonderland.txt"

file = open(filename, "r")
raw = file.read()
raw = raw.lower()
text = []
for n in range(len(raw)):
	if raw[n].isalpha():
		text.append(raw[n])
jointtext = ('').join(text)


freq = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
freq_list = []
for i in range(len(alphabet)):
	freq_list.append([alphabet[i] + ': ' + str(raw.count(alphabet[i]))])

print(freq_list)

#Alice in Wonderland letter counter test:

import unittest

from alice_in_wonderland import alice_letter_counter

class TestAlice(unittest.TestCase):

	def test0(self):
		expected = [['a: 9805'], ['b: 1746'], ['c: 3004'], ['d: 5470'], ['e: 15398'], ['f: 2382'], ['g: 2944'], ['h: 7890'], ['i: 8636'], ['j: 235'], ['k: 1290'], ['l: 5211'], ['m: 2467'], ['n: 8053'], ['o: 9478'], ['p: 1968'], ['q: 220'], ['r: 6612'], ['s: 7270'], ['t: 12202'], ['u: 3978'], ['v: 963'], ['w: 2952'], ['x: 176'], ['y: 2584'], ['z: 80']]
		self.assertEqual(alice_letter_counter(), expected) 

unittest.main()

#numbers to letters
# for i in range(1,256):
#     print(i, " stands for ", chr(i))

#fix the above so it prints only A-Z and a-z
# - There is something small that needs fixing. Can you spot it and fix it? (Hint, we only want A-Z and a-z)
# - Make a function that prints A-Z and a-z
# - Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))
# "I LOVE YOU" [ 73, , 76, ...]

#fixed it to print A-Z and a-z and turned it into a function
alpha = []
def alpha_print():
	for i in range(1,123):
		if (chr(i).isalpha()):
			print(str(i) + " stands for " + chr(i))
			#I save the values in a list to make the cypher:
			alpha.append([i, chr(i)])
	#I return it so I can use it in the next function
	return alpha
alpha_print()
#print(alpha)

def secret_message():
	secret = []
	message = input('Write your message here: ')
	for x in range(len(message)):
		for n in range(len(alpha)):
			if message[x] == alpha[n][1]:
				secret.append(alpha[n][0])
	print(secret)
	return secret

secret_message()

#DAY 2
# Write out Continent counter.

M = 'land'
o = 'water'

world = [
  [o, o, o, o, M, M, M, M, M, M, M],
  [o, o, o, o, M, M, M, M, M, M, M],
  [o, o, o, o, M, M, M, M, o, o, o],
  [o, o, o, o, M, M, M, o, o, o, o],
  [o, o, o, o, o, M, M, M, o, o, o],
  [o, o, o, o, o, M, o, o, o, o, o],
  [o, o, o, o, o, o, o, o, o, o, o],
  [o, o, o, o, o, o, o, o, o, o, o],
  [o, o, o, o, o, M, o, o, o, o, o],
  [o, o, o, o, o, o, o, o, o, o, o],
  [o, o, o, o, o, o, o, o, o, o, o]
]

# These are just to make the map easier for us to read.​

# - Write a function that prints out all elements of the above board, starting from the first element of the first line, till the end. Each line should be read from beginning to end.


def print_world_items():
	print("Print board:")
	for i in range(len(world)):
		for n in range (len(world[i])):
			print(world[i][n])

print_world_items()

# - Now write a function that prints out all elements in reverse.

def print_world_items_reverse():
	print("Print reversed board:")
	world.reverse()
	for i in range(len(world)):
		for n in range (len(world[i])):
			print(world[i][n])

print_world_items_reverse()

def continent_counter(world, x, y):
  
    if world[y][x] != 'land':
        return 0

    size = 1
    world[y][x] = 'counted land'
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    # row above
    if x == len(world) -1:
      return 1
    if y == len(world) -1:
      return 1
    if x == 0:
      return 1
    if y == 0:
      return 1
    else:
      size = size + continent_counter(world, x-1, y-1)
      #print('first recursion size: ' , size)
      size = size + continent_counter(world, x  , y-1)
      size = size + continent_counter(world, x+1, y-1)

      # same row
      size = size + continent_counter(world, x-1, y  )
      size = size + continent_counter(world, x+1, y  )

      # row below
      size = size + continent_counter(world, x-1, y+1)
      size = size + continent_counter(world, x  , y+1)
      size = size + continent_counter(world, x+1, y+1)
      return size

print(continent_counter(world, 5, 5))


# - There is one small bug in the continent counter above. Can you find it and fix it? (Hint: change the world so that the continent borders the edge)

# - Write a function that generates an n x n sized board with either land or water chosen randomly.

import random
def random_world(n, a, b):
  options = [a, b]
  board = []
  for i in range(n):
    board.append([])

  for x in range(len(board)):
    for i in range(n):
      secure_random = random.SystemRandom()
      board[x].append([secure_random.choice(options)])
    print(board[x])

  print(board)

random_world(8, 'M', 'o')

my_dict = {
    "a": 35000,
    "b": 8000,
    "z": 450
}

#DAY 3
# Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.
# I made a function that takes a dictionary, an old key-value pair and a new one as arguments, and "replaces" the old with the new one (it actually just adds the new one and deletes the old one). It is imperfect though, since dictionaries are unordered and I cannot insert the item at the same spot as the replaced key-value pair.

def change_key_value(dictionary, oldkey, newkey):
	copied_value = dictionary[oldkey]
	dictionary[newkey] = copied_value
	del(dictionary[oldkey])
	print(dictionary)

change_key_value(my_dict, "a", "x")


# Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

filename = "alice_in_wonderland.txt"

def alice_letter_counter_dict():
	with open(filename) as file:
		raw = file.read()
		raw = raw.lower()
		text = []
		for n in range(len(raw)):
			if raw[n].isalpha():
				text.append(raw[n])
		jointtext = ('').join(text)


	freq = 0
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	alice_dict = {}
	for i in range(len(alphabet)):
		alice_dict[alphabet[i]] =  str(raw.count(alphabet[i]))
	print(alice_dict)
	return alice_dict

alice_letter_counter_dict()

# test for this version of alice in wonderland in separate files

virginia_balseiro = dict(name = "Virginia Balseiro", discord_id = "yesvirginia [Gold] [Volunteer]", fav_food = "Vegan burger", fav_quote = '"Do or do not - there is no try" - Yoda', quirky_fact = "Im obsessed with means of public transport (trains, buses, planes, etc) except boats because I'm scared of being on a man-made device on a large body of water (not scared of water itself, but being on a ship in it)", dream = "Moving to Europe")

print(virginia_balseiro)
print(virginia_balseiro["dream"])

virginia_balseiro["dream"] = "Moving to Europe and working as a developer in a vegan company"

print(virginia_balseiro["dream"])

#Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.

class Student():
    def __init__(self, name, discord_id, fav_food, dream):
        self.name       = name
        self.discord_id = discord_id
        self.fav_food   = fav_food
        self.dream      = dream

s1 = Student("Virginia Balseiro", "yesvirginia [Gold] [Volunteer]", "pasta", "moving to Europe")

s2 = Student("Deb Cupitt", "deb[Gold]", "chocolate", "gender equity")

s3 = Student("Marta Bodojra", "marta [Gold] [Volunteer]", "dark chocolate", "become a developer and help all of you to do it together!😉")

s4 = Student("Cristina Tarantino", "CristyTarantino[Gold]", "pasta", "being an amazing developer")

s5 = Student("Jessica", "Jessi_RS [Gold]", "pasta", "work as developer by end of the year")

s6 = Student("Bituin Callanta", "bituin [gold]", "sashimi", "lessen the gender wage gap")

s7 = Student("Andreea Visanoiu​", "Andreea[Gold]", "wontonmee", "becoming an University teacher")

print(s2)
print(s2.name)
print(s2.dream)

# Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.
 
class StudentExtended():
	def __init__ (self, firstname, lastname, email, phonenumber, github, linkedin, website, country, genderidentity, pronouns, goals, codinglevel, groups, roles, dream):
		self.firstname = firstname
		self.lastname = lastname
		self.email= email
		self.phonenumber = phonenumber
		self.github = github
		self.linkedin = linkedin
		self.website = website
		self.country = country
		self.genderidentity = genderidentity
		self.pronouns = pronouns
		self.goals= goals
		self.codinglevel = codinglevel
		self.groups = groups
		self.roles = roles
		self.dream = dream

se1 = StudentExtended("Virginia", "Balseiro", "virginiabalseiro@gmail.com", "+59898591906", "https://github.com/VirginiaBalseiro", "https://www.linkedin.com/in/virginia-balseiro/", "https://www.virginiabalseiro.com/", "Uruguay", "woman", "she/her", "Find my next job, Become a freelancer", "Intermediate", "Student, Working, Job seeking, Career changer", "Volunteer", "Moving to Europe and working as a developer at a vegan company")

print(se1)
print(se1.firstname)
print(se1.dream)