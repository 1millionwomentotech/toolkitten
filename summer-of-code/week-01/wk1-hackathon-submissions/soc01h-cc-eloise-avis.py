#imported secrets module to randomly chose between land (1) and water (0)
import secrets
import math

# Map generator
#Code to randomly generate a map of a selected size

#defining function to create a row
#function takes one input size and outputs a list
def make_row(size):
    #setting up list of variables to chose from
    var = (0, 1)
    #initalise row as empty list
    row = []
    #generates the values in the row
    for x in range(1, size):
        #chose land or water
        value = secrets.choice(var)
        #add to row
        row.append(value)
    #outputs the list row
    return row

#This function generates a map using rows to create a list of lists.
def map_gen(mapsize):
    map = {x: make_row(map_size) for x in range(map_size)}
    print(map)

# This file contains two version of the continent counter.  
# The first works (as far as I have been able to tell) 
# The second is an attempt to refine and improve it

size=0
land_list=[]


def check_row(x,y,map):
	global size
	global land_list
	row = map[y]
	for co in range(x-1,x+2):
		if row[co]=='l':
			pos = str(co)+str(y)
			if pos in land_list:
				pass
			else:
				size = size+1
				land_list=land_list +[pos]
				#global land_list
				#global size
	
def check_tile(x,y,map):
	global size
	global land_list
	for y_co in range(y-1,y+2):
		check_row(x,y_co,map)

def map_to_use():
	row4 = ('w','w','w','w','w')
	row3 = ('w','l','w','w','w')
	row2 = ('w','l','l','l','w')
	row1 = ('w','l','w','w','w')
	row0 = ('w','w','w','w','w')
	map = {0: row0, 1: row1, 2: row2,3: row3,4:row4}
	return map

def find_middle(mapsize):
	#locate middle
	mid_x=int((mapsize)/2)
	return mid_x

#This counter works

def main():
	global size
	global land_list
	map = map_to_use()	
	#print (map)
	mapsize = len(map)
	x=find_middle(mapsize)
	y=x
	check_tile(x,y,map)
	pos= str(x)+str(y)
	land_list=land_list+[pos]
	for item in land_list:
		x = int(item[0])
		y = int(item[1])
		check_tile(x,y,map)
	
	print(size)
	
main()

# # My attempt to count adjacent land tiles
# # It does not fully work yet.

# #Setting up record of connected pieces of land
# land_list = []
# #Setting up a count to keep track of connected land
# #THis means that there are two ways of counting the connected land
# count = 0

# #This function takes a string and a list as an input
# #It converts a coordinate to an index position of the map list 
# #for a given mapsize
# def coordinate_convert(string, map):
# 	mapsize = math.sqrt(len(map))
# 	string = str(string)
# 	x = string[0]
# 	x = int(x)
# 	y = int(string[1])
# 	#converting to a reference in list
# 	y= int(x + (mapsize * y))
# 	return y
	
# #This function takes a string to convert into a coordinate
# # to store in land_list

# def reference_convert(ref, map):
# 	ref = int(ref)
# 	mapsize = int(math.sqrt(len(map)))
# 	x, y = divmod(ref, mapsize)
# 	coordinate = str(x)+str(y)
# 	return coordinate

# #Both functions above are to help think about the map as a space.

# #This function is designed to check the land on and adjacent to the current tile
# #I'm not sure it works
# def check_current_tile(x, map):
# 	global land_list
# 	global count
# 	mapsize = int(math.sqrt(len(map)))
# 	ref = int(coordinate_convert(x, map))
# 	print("Checking tile", reference_convert(ref,map))

# 	if map[ref] == 1:
# 		print('land ahoy!')
# 		land_list = land_list + [reference_convert(ref, map)]
# 		count = count + 1

# 		#Indexs of adjacent tiles in the same row
# 		#Current tile is duplicated so can be used to generate subsequent rows
# 		current_row = [ref - 1, ref, ref + 1]

# 		#Indexes of tiles that are adjacent in the row below (i.e. SW,S,SE)

# 		row_below = []
# 		for ref in current_row:
# 			ref = ref - mapsize
# 			row_below = row_below + [ref]	

# 		#Indexes of tiles that are adjacent in the row above (i.e. NW,N, NE)
# 		row_above = []
# 		for ref in current_row:
# 			ref = ref + mapsize
# 			row_above = row_above + [ref]

# 		#creates a list of the indexes of all adjacent squares to check in map list
# 		refs_to_check = row_above + current_row + row_below
		
# 		#checks each vaue in the refs_to_check list to see if it is land
# 		for ref in refs_to_check:
# 			ref = int(ref)
# 			if ref>-1 and ref<len(map):
# 				check_one_tile(ref, map)
# 			else:
# 				pass

# 		#print(row_above)
# 		#print(current_row)
# 		#print(row_below)
# 	else:
# 		print("No land here!")
	
# def check_one_tile(ref,map):
# 	global count
# 	global land_list
# 	#Checks to see if square is land
# 	if map[ref] == 1:
# 		#Trying to ignore duplicates
# 		if reference_convert(ref,map) in land_list:
# 			pass
# 		else:
# 			#Adding adjacent land to land_list
# 			land_list = land_list + [reference_convert(ref, map)]
# 			#Updating the count
# 			count +=1
# 			#print(land_list)
		
	
	
# def map_generate(mapsize):
# 	#Initalises variables to choose
# 	# 0 represents water
# 	# 1 represents land
# 	var = (0, 1)
# 	#initalises map list
# 	map = []
# 	#Creates mapsize squared values randomly selected from 0 and 1
# 	for x in range(0, mapsize ** 2):
# 		map = map + [secrets.choice(var)]
# 	print(map)
# 	return map

# #	Attempt to define a function to split map string to produce a more visual image of map
# #	Something is not quite right with it
# #
# # def print_map(map):
# # 	mapsize = int(math.sqrt(len(map)))
# # 	for x in range(0, mapsize):
# # 		#To print grid the right way up
# # 		value = mapsize  -x - 1
# # 		#Prints map splitting into lines
# # 		print(map[value-1:value+mapsize])


# def find_centre(mapsize):
# 	x = int(mapsize // 2)
# 	y = x
# 	#Centre is then converted to a form to use.
# 	centre = str(x)+str(y)
# 	return centre


# def check():
# 	global land_list
# 	global count
# 	#map1 was used for some testing
# 	#map1 = [0,0,0,1,1,1,1,0,0]

# 	mapsize = 11
# 	land_list = []
# 	map2 = map_generate(mapsize)

# 	print(len(map2))
# 	centre = find_centre(mapsize)
# 	check_current_tile(centre,map2)

# 	for land in land_list:
# 		check_current_tile(reference_convert(land,map2),map2)
	
# 	print("The land has size ", len(land_list))
# 	print("The count is", count)
	
# 	#print(reference_convert(2,map1))





	





