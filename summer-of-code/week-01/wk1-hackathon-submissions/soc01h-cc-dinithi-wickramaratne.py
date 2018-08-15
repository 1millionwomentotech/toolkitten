import random
#1 is for land 0 is for water
def createWorld(n):
	world = [[random.randint(0,1) for i in range(0,n)] for j in range(0,n)] 
	return world

#shows the randomly generated world
def showWorld(n,world):
	rownumber = 1
	for i in world:
		string = '[ '
		for j in i:
			string = string + str(j)+' '
		string = string+'] '+str(rownumber)
		print(string)
		rownumber+=1

#calculates the land of the continent you are standing on
def calculateLand(row,column,n,world):
	if(row>=0 and column>=0 and row<n and column<n):
		#print(world[row][column])
		if(world[row][column]==0 or world[row][column]==-1):
			return 0
		else:
			world[row][column] = -1
			return 1 + calculateLand(row-1,column,n,world) +calculateLand(row-1,column+1,n,world) +calculateLand(row,column+1,n,world) +calculateLand(row+1,column+1,n,world) +calculateLand(row+1,column,n,world) +calculateLand(row+1,column-1,n,world) +calculateLand(row,column-1,n,world) +calculateLand(row-1,column-1,n,world)
	else:
		return 0

#method to find the size of all continents available
def allContinents(world,n,land):
    print('Size of continent 1 is '+str(land)) 
    index = 2
    for i in range(0,n):
        for j in range(0,n):
            count = calculateLand(i,j,n,world)
            if(count!=0):
                print('Size of continent ',index,'is '+str(count))
                index+=1

def prompt():
	world_size = int(input("Please enter the size of the world "))
	world = createWorld(world_size)
	print('')
	print('This is the random world generated: Land is shown by 1 and water by 0')
	showWorld(world_size,world)
	print('Please select the land where you want to stand on :p')
	print('Rows and columns are indexed starting from 1')
	row = int(input("Enter the row number"))
	column = int(input("Enter the column number"))
	land = (calculateLand(row-1,column-1,world_size,world))
	print('Size of the continent you are standing on is ',land)
	allContinents(world,world_size,land)

prompt()