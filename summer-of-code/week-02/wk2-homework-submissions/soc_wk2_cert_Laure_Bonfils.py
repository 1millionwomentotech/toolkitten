
#### Day 1 ####

## Exercise: Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in alice_in_wonderland.txt (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)

filename = "/Users/Laure/Workspace/SummerOfCode_Python/alice_in_wonderland.txt"
file = open(filename, "r")
raw = file.read()
txtString = raw.lower()

count = {"a" : 0, "b": 0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

with file as f:
    for i in txtString:
        if i in count:
            count[i]+=1
print(count)

#### Day 2 ####

## Exercise:There is something small that needs fixing:
# for i in range(65,65+2*26):
#     print(i, " stands for ", chr(i))
# Can you spot it and fix it? (Hint, we only want A-Z and a-z)

for i in range(65,65+2*26):
    if chr(i).isalpha():
        print(i, " stands for ", chr(i))

## Exercise: Make a function that prints A-Z and a-z

def allLetters():
    for i in range(65,65+2*26):
        if chr(i).isalpha():
            print(chr(i))
allLetters()

## Exercise: Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;)) "I LOVE YOU" [ 73, , 76, ...]

def message():
    code = []
    question = input("Please give me your message!")
    for i in range(0, len(question)):
        if question[i].isalpha():
            num = ord(question[i])
            code.append(str(num))
    print(code)
            
message()

## Exercise - Optional: Write a function that does a ceaser cypher (Google), ask the user a number, and shift their message by that number.

def message2():
    code = []
    question1 = input("Please give me your message!")
    question2 = input("Please give me a number.")
    for i in range(0, len(question1)):
        if question1[i].isalpha():
            num = ord(question1[i]) + int(question2)
            new_message = chr(num)
            code.append(new_message)
            answer = "".join(code)
    print(answer)
            
message2()

## Exercise: Write a function that prints out all elements of the board below, starting from the first element of the first line, till the end. Each line should be read from beginning to end.

# Not sure what I did is what is asked (not sure to understand what is expected)
M = "land"
o = "water"
world = [[o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,M],
 [o,o,o,M,o,o,o,o,o,M,o],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,M],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]]

print(world)
print (world[0][1])

def countElem():
    for i in range(11):
        for j in range (11):
            print(world[i][j])  

countElem()

## Exercise: Now write a function that prints out all elements in reverse.
def countElem2():
    for i in reversed(range(11)):
        for j in reversed(range(11)):
            print(world[i][j])  

countElem2()

## Exercise: There is one small bug in the continent counter below. Can you find it and fix it? (Hint: change the world so that the continent borders the edge)

import itertools
def continent_counter(world,x,y):
    if x not in range(11) or y not in range(11) or world[y][x] != 'land': 
        return 0 
    size = 1
    world[y][x] = 'counted land'
    size = size + continent_counter(world, x, y-1)
    size = size + continent_counter(world, x, y+1)
    size = size + continent_counter(world, x+1, y-1)
    size = size + continent_counter(world, x+1, y)
    size = size + continent_counter(world, x+1, y+1)
    size = size + continent_counter(world, x-1, y-1)
    size = size + continent_counter(world, x-1, y)
    size = size + continent_counter(world, x-1, y+1)
    return size

print(continent_counter(world, 5, 5))

## Exercise: Write a function that generates an n x n sized board with either land or water chosen randomly.

import random

grid = []

def buildBoard(n):
    #  Create empty grid
    for i in range(n):
        grid.append([])
        for j in range(n):
            # Randomly generate land and water 
            grid[i].append(random.choice([o,M]))
    return (grid)

print(buildBoard(20))

## Exercise -Optional, Advanced: Run your continent counter for a 20 x 20 board. How long does it take to run? (If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up in a VERY LOOOONG WAIT) - make sure you know how to break a running program as it may take a long time to complete and you might not have time to wait for it ;)

def continent_counter2(world,x,y,n):
    if x not in range(n) or y not in range(n) or world[y][x] != 'land': 
        return 0 
    size = 1
    world[y][x] = 'counted land'
    size = size + continent_counter2(world, x, y-1, n)
    size = size + continent_counter2(world, x, y+1, n)
    size = size + continent_counter2(world, x+1, y-1, n)
    size = size + continent_counter2(world, x+1, y, n)
    size = size + continent_counter2(world, x+1, y+1, n)
    size = size + continent_counter2(world, x-1, y-1, n)
    size = size + continent_counter2(world, x-1, y, n)
    size = size + continent_counter2(world, x-1, y+1, n)
    return size

def buildBoard2(n):
    #  Create empty grid
    for i in range(n):
        grid.append([])
        for j in range(n):
            # Randomly generate land and water 
            grid[i].append(random.choice([o,M]))
    return (grid)

new_world = buildBoard2(20)
print(new_world)
print(continent_counter2(new_world, 10, 10, 20))

# Exercise -Optional, Advanced: Write test coverage in unittest and/or trace for Continent Counter.

# --> See file "soc_wk2_cert_Laure_Bonfils_testfile.py"
# I can't send this second file via the Kartra tickets, so please see below the content of "soc_wk2_cert_Laure_Bonfils_testfile.py":

# import unittest
# from soc_wk2_cert_Laure_Bonfils import continent_counter, world 
# class TestDay2(unittest.TestCase):
#     def test0(self):
#         self.assertEqual(continent_counter(world, 5, 5),24)
        
# unittest.main()

#### Day 3 ####

# Exercise: Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.

my_dict = {
    "a": 35000,
    "b": 8000,
    "z": 450
}

del(my_dict["a"])
my_dict["new_a"]=35000
print(my_dict)

## Exercise: Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

# --> That's already what I've done - see corresponding exercise.

## Exercise: Create a dictionary with your own personal details, feel free to be creative and funny so for example, you could include key-value pairs with quirky fact, fav quote, pet. Practice adding, modifying, accesing.

perso_dict = {"name": "Laure", "hobby": "Well coding of course. Rowing otherwise!", "pet": "none"}

del(perso_dict["pet"])
print(perso_dict["hobby"])
perso_dict["dreamyHobby"] = "travelling around the world"
print(perso_dict)

## Exercise: Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.

class Students():
    def __init__(self, name, dream):
        self.name = name
        self.dream = dream
    
    def printAll(self):
        print(self.name + '\'s dream is ' + self.dream)

s1 = Students("Andrea", "teaching_university")
s1.printAll()
print(s1.name)
s2 = Students("Deb","gender equity")
s3 = Students("Marwa", "data analyst")
s4 = Students("Virginia", "moving to europe and working as a dev in a vegan company")
s5 = Students("Renditions​Sacha", "to return to research")
s6 = Students("Jessica", "work as developer by end of the year")
s7 = Students("Cristina", "being an amazing developer") 
s8 = Students("Bituin", "lessen the gender wage gap") 

## Exercise: Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.
# Hint: You can start with the DIY signup form https://memberportal.1millionwomentotech.com/diy but feel free to be creative and add/modify as you see it best! This is the REAL work of a creator to find the meaningful description of reality and translate it for computers.

class Real_student():
    def __init__(self,first_name,last_name,phone_number,email_address,Github,linked_in,facebook,country,city,languages_spoken,programming_goal,code_level,group_subscription,what_role,sign_up_date,current_job,studies_degree,language_you_aim_to_master,allocated_time_to_soc,other_skills, family_situation):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.Github = Github
        self.linked_in = linked_in
        self.facebook = facebook
        self.country = country
        self.city = city
        self.languages_spoken = languages_spoken
        self.programming_goal = programming_goal
        self.code_level = code_level
        self.group_subscription = group_subscription
        self.what_role = what_role
        self.sign_up_date = sign_up_date
        self.current_job = current_job
        self.studies_degree  = studies_degree 
        self.language_you_aim_to_master = language_you_aim_to_master
        self.allocated_time_to_soc = allocated_time_to_soc
        self.other_skills = other_skills
        self.family_situation = family_situation
    
    def contact_details(self):
        contact = [self.email_address, self.phone_number, self.linked_in, self.facebook]
        print(self.first_name + self.last_name + " is from " + self.city + ", " + self.country + " can be contacted via email address, phone number, LinkedIn or Facebook, using the following: \n" + contact[0] + "\n" + contact[1] + "\n" + contact[2] + "\n" + contact[3] )
        return contact
    
    def perso_details(self):
        if self.studies_degree != "":
            print(self.first_name + " " + self.last_name + " is currently working as a " + self.current_job + " after a degree of " + self.studies_degree + ". The student speaks" + self.languages_spoken + " and have the following skills: " + self.other_skills  + ". The student's family situation is " + self.family_situation +".")
        else:
            print(self.first_name + self.last_name + " is currently working as a" + self.current_job + ". The student speaks " + self.languages_spoken + " and have the following skills: " + self.other_skills  + ". The student's family situation is: " + self.family_situation)

    def soc_registration(self):
        print("The student signed up on " + self.sign_up_date + " and will spend " + self.allocated_time_to_soc + " on learning coding via SOC." + " Add the student on the following groups: " + self.group_subscription + ".")
     
    def coding_details(self):
        print("This student wants to prioritise learning " + self.language_you_aim_to_master + " in which the student's level is " + self.code_level + ", aiming to " + self.programming_goal + " .")
        if self.Github != "":
            print("The student's previours coding work can be found there: " + self.Github + ".")

    def volunteering(self):
        if self.code_level == "Advanced" and self.what_role == "Mentor":
            print("This student can also be a mentor.")
        if self.what_role == "Volunteer":
            print("This student is also a volunteer.")
        if self.what_role == "Hire":
            print("Hiring!")

student1 = Real_student("Laure","Bonfils","074246322556","lmdb@google.com","","whateverlinkedIn","whateverfacebook","UK","Oxford","English, French, Spanish","become a software developper","false beginner","Working, Job seeking, Entrepreneur","Volunteer","April 2018","researcher","PhD","Python","full-time","engineering, project management", "single")

student1.perso_details()
student1.contact_details()
student1.coding_details()
student1.soc_registration()
student1.volunteering()


#### Day 4 ####

## Exercise:install pip, NLTK, Anaconda and Jupyter Notebook
# --->Done<---

## Exercise: #5 from http://www.nltk.org/book/ch01.html --> Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?

def lexical_diversity(text):
    return len(set(text)) / len(text) 

lexical_diversity_humor = 0.231 # the number of distinct words is 23% of the total number of words.
lexical_diversity_fiction_romance = 0.121 # the number of distinct words is 12% of the total number of words.

# So the genre humor is more lexically diverse.