from random import choice

##soc01h-cc-Jessica-Sanchez.py

##Build the world
#Predefined: 2 continents
world=[0,1,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0,0],[0,0,1,1,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,2,2],[0,0,0,0,2,2,2,2,2,2,0],[0,0,0,0,2,2,2,2,2,2,0],[0,0,0,0,0,0,2,2,2,2,0],[0,0,0,0,0,2,2,0,0,0,0]

#Print the world
def printWorld(world):
	print('\n')
	for x in world:
		print(" ".join(map(str, x)))
	print('\n')
print('\n\nPredefined world with 2 continents, where \'0\' is water and other numbers are continents')
printWorld(world)

##Find a "continent" (which could be a one-tile island... at this point we wouldn’t know).
#get a location from user
def play():
	print('\nWrite the coordinates of your location(x,y), you can choose from 0 to 10:')
	x= int(input('\nX = '))
	while (x<0 or x>10):
		x= int(input('\nWrong input, Enter a value from 0 to 10: '))
	y=int(input('\nY = '))
	while (y<0 or y>10):
		y= int(input('\nWrong input, Enter a value from 0 to 10: '))
	location=[y,x]
	print('Your location is ({},{})'.format(location[1],location[0]))
	## Compute its size.
	continent=0
	continent2=0
	if world[location[0]][location[1]]==0:
		print('You are swimming in the sea... Glu glu glu')
		play()
	else:
		for row in range (0,11):
			for col in range (0,11):
				if world[row][col]==world[location[0]][location[1]]:				
					continent=continent+1
				if world[row][col]>0 and world[row][col]!=world[location[0]][location[1]] :
					continent2=continent2+1
		result=''
		if continent2>continent:
			result='larger'
		else:
			result='smaller'
		##Find another continent (making sure not to count any of them twice but also making sure each gets counted), and repeat the process.
		print('\nYou are standing at Continent {}, which contains {} tiles.'.format(world[location[0]][location[1]],continent))
		##Then find the largest two, and see whether they look like fun to play on.
		print('There is another land, with {} tiles, which is {}'.format(continent2,result))

def bonus():
	print('\n****Bonus***\n')
	print('1. Calculate continent size for all continents in the world')
	cont1=0
	cont2=0
	for row in range (0,11):
		for col in range (0,11):
			if world[row][col]==1:				
				cont1=cont1+1
			if world[row][col]==2:
				cont2=cont2+1
	print('the Continent 1\'s size is {} tiles, and Continent 2 is {} tiles.'.format(cont1,cont2))

	print('\n2.Random world generator and 4. extension of the problem to n x n size world(parcially)')

	n=int(input('Enter the size of your world (n): '))
	def generateLand():
		list1=[]
		for i in range (0,n):
			list1.append(choice(['X','o']))
		return list1

	r_world=[]
	for i in range (0,n):
		r_world.append(generateLand())
	print('\nWorld generated {}x{}.\n\'X\' is Land and \'o\' is water'.format(n,n))
	printWorld(r_world)


play()
bonus()