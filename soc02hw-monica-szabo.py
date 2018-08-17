#SOC-WEEK-2/DAY-1
#Many thanks for all Yours contribution to join and learn us .
#Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in `alice_in_wonderland.txt` 
path = '/Users/monicaszabo/Desktop/story/alice_in_wonderland.txt'
wonderland = open(path, 'r')
fl = wonderland.read()
words = fl.split()
words = ''.join([ l for l in words if l.isalpha()])
words = words.lower()
letter_list = list(words)
counted_letters = [[letter, letter_list.count(letter)] for letter in set(letter_list)]
sorted_result = sorted(counted_letters)
print(sorted_result)
wonderland.close()

#SOC-WEEK-2/DAY-2
#A-make a function that print A-Z and a-z

def get_letters():
	for i in range(65 , 91):
		capital = (chr(i))
		print(capital)
	for i in range(97 , 123):
		small = (chr(i))
		print(small)
get_letters()

#B-Make a function that asks the user for a message, and turns it into a list of numbers.

def cypher_message():
	message = input("Enter please Your message:")
	print(message)
	code =[ord(letter) for letter in message]
	print(code)
cypher_message()

#C-Make a function that prints out all the elements of the world board,
from start to end and reverse.

o = 'water'
M = 'land'

world = [[o, o, o, o, o, o, o, o, o, o, o],
	 	[o, o, o, o, M, M, o, o, o, o, o],
	 	[o, o, o, o, o, o, o, o, M, M, o],
		[o, o, o, M, o, o, o, o, o, M, o],
	 	[o, o, o, M, o, M, M, o, o, o, o],
	 	[o, o, o, o, M, M, M, M, o, o, o],
 		[o, o, o, M, M, M, M, M, M, M, o],
	 	[o, o, o, M, M, o, M, M, M, o, o],
	 	[o, o, o, o, o, o, M, M, o, o, o],
 		[o, M, o, o, o, M, o, o, o, o, o],
	 	[o, o, o, o, o, o, o, o, o, o, o]]


def get_el(world):
	for row in range(len(world)):
		for item in range(len(world[row])):
			print(world[row][item])
get_el(world)

#reversed elements below
import itertools
chain = list(itertools.chain(*world))
print(*chain, sep="\n")

#D-- Write a function that generates an n x n sized board with either land or water chosen randomly.
import random
def random_board(n):
	tiles = ['water','land']
	board =[]
	for row in range(n):
		board.append([])
		board[row] = [tiles[random.randrange(len(tiles))] for item in range(n)]
		print(board[row], sep ="\n")
random_board(4)	

#WEEK-2/DAY-3

'''A- Modify "a" for another name in my_dict.
 Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.'''

import gc
my_dict = {
	"a" : 35000,
	"b" : 8000,
	"z" : 450
}
my_dict["doing"]  = "wonderful" 
my_dict["a"] = {"doing" : "wonderful"}
del(my_dict["doing"])
print(my_dict)



#B- Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.
path = '/Users/monicaszabo/Desktop/alice-story/alice_in_wonderland.txt'
wonderland = open(path, 'r')
fl = wonderland.read()
words = fl.split()
words = ''.join([ l for l in words if l.isalpha()])
words = words.lower()

from sortedcontainers import SortedDict
def freq_dist(words):
	dict = {}
	for l in words:
		keys = dict.keys()
		if l in keys:
			dict[l] += 1
		else:
			dict[l] = 1
	return SortedDict(dict)
print(freq_dist(words))
wonderland.close()

#C- Create a dictionary with your own personal details.Practice adding, modifying, accesing.

import gc

monica_szabo = dict( fav_quote = "Count everyday like a life.-Seneca", fav_actor = "Anthony Hopkins", hobby = "coding")
monica_szabo["cat"] = "Pofoo"
monica_szabo["fav_color"] = "red"
monica_szabo["fav_orchestra"] = "Andre Rieu orchestra"
print(monica_szabo)
monica_szabo["color"] = "purple"
print(monica_szabo)
print(monica_szabo["fav_quote"])

#-D- Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.
import gc
class Student():
	def __init__(self, name, dream):
		self.name = name
		self.dream = dream

	def dream_print(self):
		print(self.name + " " + self.dream)

	def show_all(self):
		for attr, value in self.__dict__.items():
			print(attr, value)

s1 = Student("Jessica", "work as developer by the end of the year")
s2 = Student("Andreea Visanoiu", "becoming an University teacher")
s3 = Student("Cristina Tarantino", "being an amazing developer")
s4 = Student("Sacha Young", "to return to research")
s5 = Student("Virginia Balseiro", "moving to Europe and working as a developer in a vegan company")
s6 = Student("Marwa Qabeel", "Data Analyst")
s7 = Student("Deb Cupitt", "gender equity")
s8 = Student("Collanta", "lessen the gender wage gap")

for obj in gc.get_objects():
	if isinstance(obj, Student):
		obj.dream_print()

#E- Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.

import gc
class Student_1MWTT():
	def __init__(self, first_name, last_name, email, country_code, phone_number, your_gender, coding_level, your_goal, subscribing_as, like_being, attended_courses):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.country_code = country_code
		self.phone_number = phone_number
		self.your_gender = your_gender
		self.coding_level = coding_level
		self.your_goal = your_goal
		self.subscribing_as = subscribing_as
		self.like_being = like_being
		self.attended_courses = attended_courses

	def women_tech_print(self):
		print(self.first_name + " " + self.last_name + " " + self.email + " " + self.country_code + " " + self.phone_number + " " + self.your_gender + " " + self.coding_level + " " + self.your_goal + " " + self.subscribing_as + " " + self.like_being + " " + self.attended_courses)

	def women_tech_show(self):
		for attr, value in self.__dict__.items():
			print(attr, value)


#WEEK-2/DAY-4
#Exercise 5 from http://www.nltk.org/book/ch01.html _☼ Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?_


import nltk
from nltk.book import *


from nltk.corpus import brown
romance_text = brown.words(categories = "romance")
humor_text = brown.words(categories = "humor")
def lexical_diversity(text):
    return len(set(text))/len(text)
print(lexical_diversity(romance_text))
print(lexical_diversity(humor_text))

#output below
0.12070492131044529
0.23125144042406084
#Means humor is more diverse than romance :))
