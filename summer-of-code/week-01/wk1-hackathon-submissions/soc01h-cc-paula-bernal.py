

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
	