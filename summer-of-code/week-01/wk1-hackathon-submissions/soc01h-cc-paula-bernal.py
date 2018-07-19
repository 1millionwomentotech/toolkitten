

#Solution for a completely beginner 1 continent world :)


L = "land"
w = "water"

world = [[w,w,w,w,w,L,L,w,w,w,w],
		 [w,w,w,w,w,L,L,L,w,w,w],
		 [w,w,w,L,L,L,L,w,w,w,w],
		 [w,w,w,L,L,L,L,w,w,w,w],
		 [w,w,w,w,L,L,L,L,w,w,w],
		 [w,w,w,w,w,L,L,L,w,w,w],
		 [w,w,w,w,L,L,L,L,w,w,w],
		 [w,w,w,w,w,L,L,L,L,w,w],
		 [w,w,w,w,w,L,L,w,w,w,w],
		 [w,w,w,w,L,L,w,w,w,w,w],
		 [w,w,w,w,w,w,w,w,w,w,w]]

size = 0
for x in world:
	size += x.count(L)

print(size)


#returns 32 for this example


#Create a random world 11x11 tiles

import random
options = ['w','L']
world = list()
for x in range (11):
	col = list()
	for y in range (11):
		tile = random.choice(options)
		col.append(tile)
	world.append(col)
	

	