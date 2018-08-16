#PSEUDO CODE
#
#Begin from centre (list 5, index 5)
#
#Check 8 surrounding squares
#
#	If sq = 1 AND total of surrounding 8 squares > 0
#		count += 1



#Pre-generated world, one island, count size of island

# world  = 	([0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
# 			 [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
# 			 [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
# 			 [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
# 			 [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
# 			 [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
# 			 [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
# 			 [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
# 			 [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
# 			 [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
# 			 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


# def land_count(world):
# 	count = 0
# 	for l in world:
# 		for p in l:
# 			if p == 1:
# 				count += 1
# 	return count

# print (land_count(world))







import random

import numpy as np


world = np.random.random_integers(0, 1, (11, 11))

print (world)

r = len(world)
c = len(world[0])

position = world[r][c]
surround = world[r-1][c] + world[r+1][c] + world[r-1][c+1] + world[r][c+1] + world [r+1][c+1] + world[r-1][c-1] + world[r][c-1] + world[r+1][c-1]

def where_are_you(r, c):
	if position ==0:
		print ("You're not standing on land!")
		if surround > 0:
			print ("but there is land around you!")
		else:
			print ("You're in the middle of the sea!")

	if position ==1:
		print ("You're standing on land!")
		if surround > 0:
			print ("and there is more land, too!")
		else:
			print ("You appear to be on a deserted island... Wilson!")



