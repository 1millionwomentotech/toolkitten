## Program written for Python 2.7
#  Beth106, 09/08/2018
#
#  Function to count the size of a continent in a 
#  randomly generated world for Civilisation III
#
#  Known issues: Only connects continent if tiles are adjacent, not diagonal
##

import random

def continent_counter(n=11):

	## Generate islands 
	#  (standing somewhere near the middle of the board, marked 'Z')
	stand = int(n*n/2)
	world = ''
	for i in range(0,n*n):
		world= world + random.choice('Xo')
	world = list(world)
	world[stand]='Z'

	print 'X = land, o = water, Z = where you are standing'
	print 'Randomly generated %d by %d world:' % (n,n)
	for i in range(0,n):
		print world[i*n:(i+1)*n]

	## Mark the island I'm standing on, then check neighbours
	def check_land(stand, world):
		if world[stand] == 'X':
			world[stand] = 'Z'
			check_neighbours(stand, world)
		

	## Go to each of the 4 neighbouring squares, if not at edge
	def check_neighbours(stand, world):
		if stand%n != n-1:
			neighbr = stand + 1
			check_land(neighbr, world)

		if stand%n != 0:
			neighbr = stand - 1
			check_land(neighbr, world)

		if stand+n < n*n:
			neighbr = stand + n
			check_land(neighbr, world)

		if stand-n  >= 0:
			neighbr = stand - n
			check_land(neighbr, world)



	## Continent counter program

	check_neighbours(stand,world)

	print 'Your continent is marked with Z:'
	for i in range(0,n):
		print world[i*n:(i+1)*n]
	print 'The continent size is ', world.count('Z')

	return world.count('Z')


## Run the program
continent_counter()