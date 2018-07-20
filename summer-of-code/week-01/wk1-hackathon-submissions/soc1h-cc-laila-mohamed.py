import random
from collections import deque
from operator import eq

mapSize = random.randint(5, 10)   ## change to make random between the given values
map = []

def main():
	map =  generateMap()

	""" Starting at a random position, (i, j) search 8 directions:
	    1 tile north, 1 tile east, 1 tile south, 1 tile west
	    1 tile northeast, 1 tile southeast, 1 tile southwest, 1 tile northwest
	    by adding/subtracting 1 from `i` and `j`

	               (-1, -1)  (-1, 0)  (-1, +1)
	                      \     |     /
	             (0, -1) --   (i,j)   -- (0, +1)
	                      /     |     \
	               (+1, -1)  (+1, 0)  (+1, +1)
	"""
	neighbors = (-1, 0), (0, +1), (+1, 0), (0, -1), (-1, +1), (+1, +1), (+1, -1), (-1, -1)

	""" similar means that the spot we land on and the neighboring tile are the same: a == b """
	similar = eq

	""" Generate a random position in the map """
	randomPosition = generateRandomPosition()

	""" Make sure that the starting position is a land tile
        If it's not, generate a new starting position and check again
        Continue until we get a land tile """
	if(get_tile(map, randomPosition) == "O"):
		randomPosition = generateRandomPosition()
	else:
		for j in range(0, mapSize):
			print(map[j])

	print("I'm starting at " +
          str(randomPosition) + " "+
          str(get_tile(map, randomPosition)) +
          " and I'm going to explore my continent."
          )
	explore_map(map, neighbors, randomPosition, similar)

""" Generate a random position
    The maximum is mapSize -1, so we don't end up off-world
"""
def generateRandomPosition():
	return random.randint(0, mapSize-1), random.randint(0, mapSize-1)

""" Generate a map using the given values """
def generateMap():
	n = 0
	while n < mapSize:
		row = []
		for i in range(0, mapSize):
			isLand = random.choice([True, False])
			marker = isLand and "X" or "O"

			row.append(marker)
			i += 1
		map.append(row)
		n +=1
	for j in range(0, mapSize):
		print(map[j])
	return map

def explore_map(map, neighbors, randomPosition, similar):
	# start at 1 because we start on a land tile
	continentSize = 1

	# This is the position starting tile on the map
	startingTile = get_tile(map, randomPosition)

	# dictionary of the random starting position and elements that match it (the continent).
	# We put the starting position because it's land
	continent = {randomPosition}

	# double-ended queue: ordered collection that supports removing elements from either end only
	# (https://pymotw.com/2/collections/deque.html)
	visit = deque(continent)

		# popleft: Remove and return the leftmost element/start from the left and remove elements going to the right
	nextTile = deque.popleft

	while visit:    # while on this row
		thisTile = nextTile(visit)     # get the tile to the left
		for neighboringTile in neighbors:   # iterate through the 8 directions/for each of (north, south, ..., etc)
			index = get_next_tile(thisTile, neighboringTile)    # Get the next tile in the given direction
			if index not in continent:   # If the neighboring tile is not one I visited
				continent.add(index)     # Add it to the dictionary of tiles
				if is_valid(map, index):  # If the tile is not out of bounds
					value = get_tile(map, index)   # Get the value of the tile (x or 0/ water or land)
					if similar(value, startingTile):  # If the value of the neighboring tile matches my starting tile (if it is land)
						visit.append(index) # Add the coordinates of this land tile to my list
						continentSize += 1
	print("My continent is comprised of " + str(continentSize) + " tiles!")


def get_tile(map, index):
	""" Get the tile based on the position we're in now
	    Initially, this is the randomPosition generated
	    Subsequently, this is the tile we move to after we've explored around our position
	"""
	row, column = index
	return map[row][column]


def get_next_tile(thisTile, neighboringTile):
	""" Look 1 tile over in the direction specified by the value passed in neighboringTile (north, south, ..., etc.) """
	row, column = thisTile      # thisTile[i, j]
	row_neighboringTile, column_neighboringTile = neighboringTile   # neighborTile[k, l], where [k, l] is the direction we're searching (ex: (-1,0) to go one tile north)

	""" the return value is the end position. This means that I moved in one of the 8 directions from my current tile
        This is called 8 times for each starting position because I want to check all directions around me for a land mass
    """
	return row + row_neighboringTile, column + column_neighboringTile


def is_valid(map, index):
	""" Verify that the index is in range of the map """
	row, column = index
	return 0 <= row < len(map) and 0 <= column < len(map[row])

if __name__ == '__main__':
	main()