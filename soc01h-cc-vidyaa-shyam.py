##### Civilisation III 

#### Week 1 Continent Counter Hackathon #####
import numpy as np


# 11*11 static array
counter = 0
# Array to check if the tile is visited or not 
checked = np.zeros((11,11), dtype=bool)

# create a 11*11 static world

multd = [[0,1,1,0,0,0,1,1,0,0,0], 
		[0,0,0,0,0,0,1,1,0,0,0], 
		[0,1,1,1,1,1,1,1,0,0,0],
		[0,0,0,0,0,1,1,0,0,0,0],
		[0,0,0,0,1,0,1,1,0,0,0],
		[0,1,1,1,1,1,1,1,0,0,0],
		[0,0,0,0,1,1,1,1,0,0,0],
		[1,1,0,0,0,1,1,0,0,0,0],
		[0,0,0,0,1,1,0,0,0,0,0],
		[0,0,0,0,0,1,1,1,0,0,0],
		[0,0,1,0,0,0,0,0,0,0,0]]

def traverse(x, y):
    global counter
    if x < 0 or x > 11:
        return
    if y < 0 or y > 11:
        return
    if checked[x][y] == True:
        return
    #print(x,y)
    checked[x][y] = True
    if multd[x][y] == 1:
        #print(counter)
        #print(x,y)
        counter += 1	
        #print(counter)
        traverse(x-1,y)
        traverse(x+1,y)
        traverse(x,y-1)
        traverse(x,y+1)
    return counter

# Starting at the middle of the continent at 5,5
print("Size of the continent from the middle tile:", traverse(5,5))


######   Bonus Extras   ######

# Creating random world


world = np.random.randint(2,size=(11,11))
print("****Random World****")
print (world)

print(world.shape)
count = 0
for i in range(0,len(world)):
	for j in range(0,len(world)):
		if world[i][j] == 1:
			count += 1

print("Size of all continents in the random world:",count)



	

