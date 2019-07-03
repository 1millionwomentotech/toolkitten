#continent
#week 1 hackathon problem: 11 x 11 grid w/ 1 or 2 continents, find how many squares big the continent you're standing on (from the center) is. Bonus for randomly generated continent(s)

#ideas
#add a counter so that if the tile is land, then for the next 2 or 3 there is a 80%chance it will be land
#make the 6th row very likely to have land


#World generator
import random

world = ["", "", "", "", "", "", "", "", "", "", ""]
currentLine = ""
index = 0

for line in world:
	for i in range(0,11):
		percentage = random.randint(0,100)
		if percentage <= 65:
			tile = ' '
			currentLine = currentLine + tile

		elif percentage > 65:
			tile = "X"
			currentLine = currentLine + tile
	print("Line " + str(index)+ ":" + currentLine)
	world[index] = currentLine
	index += 1
	currentLine = ""
#print("here is the center tile: " + world[5][5])

Line = 5
Tile = 5

#Lists to store coordinates
continentLine = []
continentTile = []

#List to store coordinates of the continent as strings once counted
contList = []
#Counter for number of tiles in center continent
contCount = 0

if world[Line][Tile] == "X":
	#count land around the center and save coordinates:
	for i in range(-1,2):
		for j in range(-1,2):
			if world[Line + i][Tile + j] == "X":
				continentLine.append(Line + i)
				continentTile.append(Tile + j)
				contList.append(str(Line + i)+","+str(Tile + j))
				contCount += 1
				#print("Continent Coordinate: " + str(Line + i) + ", " + str(Tile + j))
	# #since the coordinates lists contain center "5,5" at index 1, pop it off and add 1 to continent count
	# continentLine.pop(1)
	# continentTile.pop(1)	
	# scratch above, if 5,5 is in contlist, remove it:
	#contList.remove("5,5")
	#print("cont count now: " + str(contCount))
	print("contList after first go: " + str(contList))
	#print("length of coords: " + str(len(continentLine)))
	#print("LineCoord: " + str(continentLine))
	#print("TileCoord: " + str(continentTile))








#now need to add those to a count, and then figure out how to do the same thing to the ones in the coordinates list. (to not count the ones we've already counted: if it's an X, but it's also in the continent list, don't count it (don't add to the list))

else:
	print("No land found at center of map")


while len(continentLine) > 0:
#for coordinateIndex in range(len(continentLine)):
	#set the coordinates to be checked around
	Line = continentLine[0]
	Tile = continentTile[0]

	# if (str(Line) + "," + str(Tile)) in contList:
	# 	continentLine.pop(0)
	# 	continentTile.pop(0)

	if Line == 5 and Tile == 5:
		continentLine.pop(0)
		continentTile.pop(0)

	else:

		#print("now checking tile at: " + str(Line)+","+str(Tile))
		# store coordinates as a string in contList and pop these off of continentLine/Tile, and add to count
		#don't pop yet?
		# continentLine.pop(0)
		# continentTile.pop(0)


		
		# if (str(Line) + "," + str(Tile)) not in contList:
		# 	contList.append(str(Line)+","+str(Tile))
		# 	contCount += 1
		#print("contList (continent coordinates to check against): " + str(contList))
		#print("contCount: " + str(contCount))
		# print("length of continentLine: " + str(len(continentLine)))

		for i in range(-1,2):
			if (Line + i > 10) or (Line + i < 0):
				continue
			else:
				for j in range(-1,2):
					if (Line+i == 5 and Tile + j == 5) or (Tile + j > 10) or (Tile + j < 0):
						continue
					elif (world[Line + i][Tile + j] == "X") and (str(Line + i) + "," + str(Tile + j)) not in contList:
						# xTilecoord = str(Line + i) + "," + str(Tile + j)
						# print("xTilecoord:" + xTilecoord)
						# print("isxTilecoord in contList? " + str(xTilecoord in contList))
						# theTruth = xTilecoord in contList
						# if theTruth == True:
						# 	break

						# elif theTruth == False:
						continentLine.append(Line + i)
						continentTile.append(Tile + j)
						contList.append(str(Line + i)+","+str(Tile + j))
						contCount += 1
						#print("New Continent Coordinate: " + str(Line + i) + ", " + str(Tile + j))
						#print("length of continentLine: " + str(len(continentLine)))
						#print("current contCount: " + str(contCount))
					else:
						continue
					
		continentLine.pop(0)
		continentTile.pop(0)

print("final continent count: " + str(contCount))
