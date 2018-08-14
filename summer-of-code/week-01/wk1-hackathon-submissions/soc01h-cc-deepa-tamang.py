import random

#Ask for the size of the world
worldsize = int(input('Enter the size of your world (2-100):'))
totalworld = worldsize**2

#Randomly generate the world: 1 for land and 0 for water
world = []
for i in range(0,totalworld):
	x = random.random()
	world.append(int(round(x)))

print(world)

dummy_world = world
dummy_worldsize = worldsize+2
dummy_totalworld = dummy_worldsize**2

for x in range(dummy_worldsize):
	dummy_world.append(0)
	dummy_world.insert(x,0)
for x in range(1,worldsize+1):
	dummy_world.insert(dummy_worldsize*x,0)
	dummy_world.insert(dummy_worldsize*(x+1)-1,0)

print(dummy_world)

continue_to_count = dummy_world.count(1)
continents = list()
while continue_to_count!=0:
	land_location = dummy_world.index(1)
	print("Land:",land_location)
	#A new continent is found, the new continent size is 1, change the found land(1)
	# to water(0) to make sure it is not counted again
	continent_size = 1
	dummy_world[land_location] = 0

	# find all land pieces in the neighborhood and create a list
	# to check neighbors of these land pieces
	neighbor_check_list = [land_location]

	while neighbor_check_list!=[]:
		land_location = neighbor_check_list[0]
		#find neighbors
		neighbors = [land_location-(dummy_worldsize+1),land_location-dummy_worldsize,land_location-(dummy_worldsize-1),land_location-1,land_location+1,land_location+(dummy_worldsize-1),land_location+dummy_worldsize, land_location+(dummy_worldsize+1)]	
		print("Neighbors: ",neighbors)

		#check all neighbors until there are no more land
		for i in neighbors:
			if dummy_world[i]==1:
				continent_size+=1
				dummy_world[i] = 0
				neighbor_check_list.append(i)
		neighbor_check_list.remove(land_location)
	print("Continent Size: ",continent_size)

	# add the size of new continent to the list of the continents
	continents.append(continent_size)

	# if there are still uncounted land pieces continue to check for other continents
	continue_to_count = dummy_world.count(1)

# Give information about all the found continents
if len(continents) == 0:
	print("There are no continents on this world!")
else:
	print("There are",len(continents),"continents in this world.")
	print("The sizes of the continents are ", continents)

	# find the biggest continent
	biggest_continent = continents[0]
	if len(continents)>1:
		for i in range(1, len(continents)):
			if continents[i]>biggest_continent:
				biggest_continent = continents[i]
	print("Biggest continent is :", biggest_continent)