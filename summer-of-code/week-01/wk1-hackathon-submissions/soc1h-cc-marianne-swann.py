## Test change.
import random

# Generate world of size n
def generateWorld(n):
	world = [[0 for x in range(n)] for x in range(n)]
	for i in range(0,n):
		for j in range(0,n):
			world[i][j] = random.randint(0,1)
	return world

# Find new continent
def checkForNewContinent(n):
	for i in range(0,n):
		for j in range (0,n):
			if world[i][j] == 1:
				return [i,j]
	return [1000,1000]

# Check for edges to avoid bounds error
def checkEdges(x, y):
	if(x == 0):
		a = 0
	else:
		a = x-1

	if(x == n-1):
		b = x+1
	else:
		b = x+2

	if(y == 0):
		c = 0
	else:
		c = y-1

	if(y == n-1):
		d = y+1
	else:
		d = y+2

	return([a,b,c,d])

# Loop through array around starting coordinates
def checkLandSize(start_x, start_y):
	rangeVar = checkEdges(start_x, start_y)
	a = rangeVar[0]
	b = rangeVar[1]
	c = rangeVar[2]
	d = rangeVar[3]
	landInCoord = 0
	for i in range(a,b):
		for j in range (c,d):
			if(world[i][j] == 1):
				landInCoord += 1
				#print("[" + str(i) + "," + str(j) + "]")
				world[i][j] = 3
				landInCoord += checkLandSize(i, j)
	return landInCoord

def printWorld(world, size):
	for i in range(0,size):
		row = ""
		for j in range(0,size):
			if world[i][j] == 1:
				row += "X"
			else:
				row += '~'
		print(row)

n = int(input('What size world do you choose? '))
world = generateWorld(n)
numOfContinents = 0
startCoordinates = checkForNewContinent(n)
printWorld(world, n)
if(startCoordinates[0] != 1000):
	while(startCoordinates[0] != 1000):
		land = 0
		start_x = startCoordinates[0]
		start_y = startCoordinates[1]
		land += checkLandSize(start_x, start_y)
		numOfContinents += 1
		print("Size of continent #" + str(numOfContinents) + " is " + str(land))
		startCoordinates = checkForNewContinent(n)
else:
	print("There are no continents in this world.")