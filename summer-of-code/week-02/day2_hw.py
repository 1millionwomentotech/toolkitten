# Fix the code to print only alphabets a-z and A-Z
import re
for i in range(1,256):
    s = chr(i)
    if re.match('[a-zA-Z]',s):
        print(i, " stands for ", s)

#Make a function to print only a-z and A-Z
def print_alpha():
	for i in range(1, 256):
		s = chr(i)
		if re.match('[a-zA-Z]',s):
			print(i, " stands for ", s)
print_alpha()

#Convert message to list of numbers
msg = input("Enter your message: ")
def gen_list(msg):
	secret_list = list()
	for l in msg:
		if l!=" ":
			secret_list.append(ord(l))
		else:
			secret_list.append(" ")
	return secret_list
print("List of secret message number:")
print(gen_list(msg))

#Caeser cypher
msg = input("Enter your message: ")
key = int(input("Enter the key: "))
def encrypt(msg, k):
	cypher = ""
	for l in msg:
		if l!=" ":
			cypher = cypher + chr(ord(l)+k)
		else:
			cypher+=" "
	return cypher
print("Secret message : ",encrypt(msg, key))

# Printing each elements from first to last from the board

M = 'land'
o = 'water'
world = [
         [o,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,M,o,M,M,o,o,o,o],
         [o,o,o,o,M,M,M,M,o,o,o],
         [o,o,o,M,M,M,M,M,M,M,o],
         [o,o,o,M,M,o,M,M,M,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]
        ]
def show_world(world):
	M = 'land'
	o = 'water'
	i = 0
	for row in world:
		j = 0
		for val in row:
			#print("{0: ^7}".format(val),end="")
			print("(",i,",",j,") = ",val)
			j+=1
		#print("")
		i+=1
show_world(world)

print("\nThe world board in reversed order:\n")
def rev_show_world(world):
	M = 'land'
	o = 'water'
	i = len(world)-1
	for row in world:
		j = len(world)-1
		for val in row:
			print("(",i,",",j,") = ",val)
			j-=1
		i-=1
rev_show_world(world)

# Resolved board bug

M = 'land'
o = 'water'
world = [
         [o,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,M,o,M,M,o,o,o,o],
         [o,o,o,o,M,M,M,M,o,o,o],
         [o,o,o,M,M,M,M,M,M,M,M],
         [o,o,o,M,M,o,M,M,M,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]
        ]
dummy_world = world
world_size = len(world)
dummy_world_size = world_size+2
dummy_total_world = dummy_world_size**2
add_list = [o, o]
for row in dummy_world:
    row.append(o)
    row.insert(0,o)
    add_list.append(o)
dummy_world.insert(0,add_list)
dummy_world.append(add_list)

def continent_counter(dworld, x, y):
    if dworld[y][x] != 'land':
        return 0
    size = 1
    dworld[y][x] = 'counted land'
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    # row above
    size = size + continent_counter(dworld, x-1, y-1)
    #print('first recursion size: ' , size)
    size = size + continent_counter(dworld, x  , y-1)
    size = size + continent_counter(dworld, x+1, y-1)

    # same row
    size = size + continent_counter(dworld, x-1, y  )
    size = size + continent_counter(dworld, x+1, y  )

    # row below
    size = size + continent_counter(dworld, x-1, y+1)
    size = size + continent_counter(dworld, x  , y+1)
    size = size + continent_counter(dworld, x+1, y+1)
    return size

print(continent_counter(dummy_world, 5 + 1, 5 + 1)) # +1 added as the dummy world has more number of rows and columns

# Write a function that generates an n x n sized board with either land or water chosen randomly

# n X n continent board

import random

size = int(input("Enter the size of board"))
world = list()
for i in range(size):
    world.append([])
    for j in range(size):
        world[i].append(random.choice(['W','L']))
print("\nThe n X n board is:\n")
print(world)
dummy_world = world
world_size = len(world)
dummy_world_size = world_size+2
dummy_total_world = dummy_world_size**2
add_list = ['W', 'W']
for row in dummy_world:
    row.append('W')
    row.insert(0,'W')
    add_list.append('W')
dummy_world.insert(0,add_list)
dummy_world.append(add_list)

def continent_counter(dworld, x, y):
    if dworld[x][y] != 'L':
        return 0
    size = 1
    dworld[x][y] = 'CL' # Counted Land
    # row above
    size = size + continent_counter(dworld, x-1, y-1)
    #print('first recursion size: ' , size)
    size = size + continent_counter(dworld, x  , y-1)
    size = size + continent_counter(dworld, x+1, y-1)

    # same row
    size = size + continent_counter(dworld, x-1, y  )
    size = size + continent_counter(dworld, x+1, y  )

    # row below
    size = size + continent_counter(dworld, x-1, y+1)
    size = size + continent_counter(dworld, x  , y+1)
    size = size + continent_counter(dworld, x+1, y+1)
    return size
x_pos = input("Enter the x - position for search:")
y_pos = input("Enter the y - position for search:")
print(continent_counter(dummy_world, int(x_pos) + 1, int(y_pos) + 1)) # +1 added as the dummy world has more number of rows and columns


## As expected with 200 size of board the maximum recursion depth exceeded in comparison