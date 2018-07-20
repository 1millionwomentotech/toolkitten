# Hackathon Week 01 - Continent Counter
# Rocio Pena - rocio-gold#4215

# ===========================================================
# My version of the problem :)

# First execution is a fixed 11 x 11 grid with static values and standing point [5][5]
# Second execution randomly generates the world and standing point

# Continent representation
# @ is the standing point
# ▢ is a standing point that is water - no possible continent
# ╬ is a tile that is part of the continent 
# _ is a water tile
# L is a land tile
# ===========================================================

# My approach to tackle the problem;)
# I drawed a 5x5 matrix with standing point right in the middle position[2,2] = [x,y]
# Then I drawed arrows indicating the directions in which the matrix can be past through
# [x,y] 	 = @ standing point 
# [x, y-1] 	 = ← left tile 
# [x-1,y-1]  = ↖ diag up left
# [x-1, y]   = ↑ up
# [x-1,y+1]  = ↗ diag up right 
# [x, y+1]   = → right
# [x+1, y+1] = ↘ diag down right
# [x+1, y]   = ↓ down 
# [x+1, y-1] = ↙ diag down left

# Then I realised that 
# 	- every time I moved to a different tile I had the exact same original problem
#   - conditions whether counting or not a tile were exactly the same. if land add 1
#	- the breaking condition - no possible movement - will return control to the original point

# How to solve this repeating problem? RECURSION
# Whenever the current tile is not a land ('L') return 0 - base case
# Otherwise mark it as visited with ╬ and do everything again 8 times (1 per each direction) 
# and again 8 times for each new position
# Finally I extended the solution to randomly generate the world and N x N extension
# I have also implemented input validation for dynamic world size

# ====================Functions======================

from random import random

# function to print the world in a neat and visually pleasant way
def pretty_print(world):
	for i in range(len(world)): #11
		temp = ''
		for j in range(len(world[0])): #10
			temp += world[i][j] + " "
		print(temp)

# randomly generate 1 tile to fill in dynamic worlds
def generate_tile():
	# pretty cool terciary operator
	return 'L' if random() * 100 <= 50 else '_'

# randomly generate starting point coordenate
def generate_random(max):
	return int(random() * max)

# capture dynamic world size - user input - with validation > 0 and number
def capture_world_size(message):
	while True:
		try:
			world_size = int(input(message))       
		except ValueError:
			print("Not a number! Please try again.")
			continue
		else:
			if world_size == 0:
				print("Size must be greater than zero! Please try again.")
				continue
			return world_size 
			break 

# generate a dynamic world
def generate_world(world_size):
	dyn_world = []
	for i in range(world_size):
		row = []
		for j in range(world_size):
			row.append(generate_tile())
		dyn_world.append(row)
	return dyn_world

# smooth edges to the dynamic world / issue with index out of range
def edges(world):
	new_world = world
	for i in range(len(world)):
		for j in range(len(world)):
			if (i == 0 or i == len(world)-1 or j == 0 or j == len(world)-1):
				new_world[i][j] = '_'
	return new_world

# ====================The method that does the work======================
# function to calculate continent size
def calculate(world, x, y):

	# recursion base case
	if world[x][y] != 'L': # not land: it's water or has been already visited
		return 0	

	size = 1
	world[x][y] = '\u256c'
	size += calculate(world, x, y-1)   #left
	size += calculate(world, x-1,y-1)  #diag up left
	size += calculate(world, x-1, y)   #up
	size += calculate(world, x-1,y+1)  #diag up right 
	size += calculate(world, x, y+1)   #right
	size += calculate(world, x+1, y+1) #diag down right
	size += calculate(world, x+1, y)   #down 
	size += calculate(world, x+1, y-1) #diag down left

	return size


# ====================Main Program======================

print("******************************************************")
print("*                   Static World                     *")
print("******************************************************")

# output static world
# ******************************************************
# *                   Static World                     *
# ******************************************************
# Continent Size:  25
# _ _ _ _ _ _ _ _ _ _ _
# _ _ _ ╬ _ L _ L _ _ _
# _ L _ ╬ _ _ _ _ L L _
# _ _ _ _ ╬ _ _ _ _ L _
# _ _ ╬ _ ╬ ╬ ╬ _ _ _ _
# _ _ _ ╬ ╬ @ ╬ _ ╬ _ _
# _ _ _ ╬ ╬ ╬ _ ╬ _ ╬ _
# _ L _ _ ╬ ╬ ╬ _ ╬ _ _
# _ _ _ ╬ _ ╬ _ ╬ _ _ _
# _ L _ _ _ _ ╬ _ _ L _
# _ _ _ _ _ _ _ _ _ _ _
# Press enter to continue


static_world = [['_','_','_','_','_','_','_','_','_','_','_'],
				['_','_','_','L','_','L','_','L','_','_','_'],
				['_','L','_','L','_','_','_','_','L','L','_'],
				['_','_','_','_','L','_','_','_','_','L','_'],
				['_','_','L','_','L','L','L','_','_','_','_'],
				['_','_','_','L','L','L','L','_','L','_','_'],
				['_','_','_','L','L','L','_','L','_','L','_'],
				['_','L','_','_','L','L','L','_','L','_','_'],
				['_','_','_','L','_','L','_','L','_','_','_'],
				['_','L','_','_','_','_','L','_','_','L','_'],
				['_','_','_','_','_','_','_','_','_','_','_']]		        

continent_size = calculate(static_world, 5, 5)
print("Continent Size: ", continent_size)
static_world[5][5] = '@' # highlight standing point
pretty_print(static_world)

input("Press enter to continue ")



print("\n\n******************************************************")
print("*                  Dynamic World                     *")
print("******************************************************")	

# user input
dynamic_world_size = capture_world_size("Enter the size of your dynamic world: ")
dynamic_world = generate_world(dynamic_world_size)
dynamic_world_new = edges(dynamic_world) # make all borders water

# generate standing point for the dynamic world
x_standing = generate_random(dynamic_world_size)
y_standing = generate_random(dynamic_world_size)

# standing point is water
if dynamic_world_new[x_standing][y_standing] == '_':
	print("Standing point [" , x_standing , "][" , y_standing , "]  is water. No continent found.")
	dynamic_world_new[x_standing][y_standing] = '\u25A2' # highlight standing point
	pretty_print(dynamic_world_new)
else:
	continent_size = calculate(dynamic_world_new, x_standing, y_standing)
	print("Continent Size: ", continent_size)
	dynamic_world_new[x_standing][y_standing] = '@' # highlight standing point
	pretty_print(dynamic_world_new)

# output dynamic world - just an example - existing continent
# ******************************************************
# *                  Dynamic World                     *
# ******************************************************
# Enter the size of your dynamic world: 16
# Continent Size:  72
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# _ L L L L _ ╬ _ ╬ ╬ ╬ _ _ _ _ _
# _ _ _ _ _ _ ╬ _ _ _ ╬ _ L _ L _
# _ L L _ ╬ ╬ _ _ _ ╬ ╬ _ _ _ L _
# _ _ _ _ _ ╬ ╬ ╬ _ _ ╬ ╬ _ _ _ _
# _ _ ╬ _ _ _ _ ╬ _ _ _ ╬ _ _ L _
# _ ╬ _ _ _ ╬ ╬ ╬ _ _ _ _ ╬ _ _ _
# _ ╬ ╬ _ _ _ _ _ ╬ ╬ _ ╬ _ _ L _
# _ _ _ ╬ ╬ _ _ ╬ ╬ _ _ _ ╬ _ _ _
# _ _ _ ╬ ╬ ╬ _ _ ╬ ╬ _ _ _ ╬ ╬ _
# _ ╬ ╬ _ _ ╬ _ ╬ _ _ _ ╬ ╬ ╬ _ _
# _ ╬ _ _ _ _ ╬ _ _ _ _ ╬ _ _ _ _
# _ ╬ ╬ _ ╬ ╬ ╬ _ _ _ _ _ ╬ _ ╬ _
# _ ╬ _ _ ╬ _ ╬ _ _ _ ╬ _ ╬ @ _ _
# _ ╬ _ ╬ _ ╬ ╬ ╬ ╬ ╬ _ ╬ _ ╬ _ _
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


# output dynamic world - just an example - standing point water - no continent
# ******************************************************
# *                  Dynamic World                     *
# ******************************************************
# Enter the size of your dynamic world: 12
# Standing point [ 4 ][ 5 ]  is water. No continent found.
# _ _ _ _ _ _ _ _ _ _ _ _
# _ L L L L _ _ L _ L _ _
# _ L _ L _ L L _ L L L _
# _ _ L _ L L L _ L _ _ _
# _ _ _ _ _ ▢ L L L L _ _
# _ _ _ L L L L _ L L _ _
# _ L L _ _ _ L L L L _ _
# _ _ L _ L _ _ L L L L _
# _ _ _ L _ L _ _ _ _ _ _
# _ _ L L L _ _ _ L L _ _
# _ _ _ L L L _ _ _ L L _
# _ _ _ _ _ _ _ _ _ _ _ _


# ====================The End of Hackathon Week 01======================




