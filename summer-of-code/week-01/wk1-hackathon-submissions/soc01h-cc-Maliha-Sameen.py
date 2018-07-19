# Week 1 Hackathon Challenge: Continent Counter

"""
	* Imported Libraries
"""
import random
from timeit import default_timer as timer

world = []
continent_size_list = []

"""
	* This method generates 0 or 1 randomly and then return 
	* 'o' for water and 'X' for land
"""
def random_tiles():
	tile = random.randint(0,1)
	if tile == 0:
		return 'o'
	else:
		return 'X'

"""
	* This method generates random world of size n x n 
"""
def generate_random_world(n):
	for i in range(0, n):
		list_of_tiles = []
		for j in range(0, n):
			list_of_tiles.append(random_tiles())
		world.append(list_of_tiles)

"""
	* This method prints the randomly generated world of 
	* size n x n
"""
def print_random_world(n):
	for i in range(0, n):
		for j in range(0, n):
			print(world[i][j], end="")
		print()

"""
	* This method determines the continent size of all
	* the continents in the world of size n x n
"""
def determine_continent_size(n):
	for i in range(0, n):
		size = 0
		for j in range(0, n):
			if world[i][j] == 'X':
				size += 1
			elif world[i][j] == 'o' and size is 0:
				size = 0
			elif world[i][j] == 'o' and size is not 0:
				continent_size_list.append(size)
				size = 0
	if size is not 0:
		continent_size_list.append(size)

"""
	* main method from where execution of program starts.
"""
def main():
	n = int(input("Input the size of the world: "))
	
	start = timer()
	generate_random_world(n)
	
	print("Random World is:")
	print_random_world(n)

	if not any('X' in sublist for sublist in world):
		print("Oops! This world has no land")
		return
	
	determine_continent_size(n)

	largest_continent_size = max(continent_size_list)
	print("Largest Continent Size: {}" .format(largest_continent_size))
	
	time = ((timer() - start) * 1000 )/ 1000
	print("Time taken: ", time,"s")

if __name__ == '__main__':
	main()