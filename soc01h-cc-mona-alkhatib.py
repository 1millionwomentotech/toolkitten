import random
'''
* My solution could be applied to any nxn world, the function would primarly take 3 parameters for the worl array, the x index and the y index.
* The player standing on onw land would mark his land as already counted, then we would go through each corner around this position (which are 8 routes in total), and each tile when reached is also marked as counted so that it wont be counted again.
* Applying these scenarios using recursive calling for the 8 routes.
'''
x = 'earth'
o = 'water'
World = [[x,x,o,o,x,o,x,o,o,x,o], 
         [x,o,x,o,o,o,o,x,x,o,x], 
         [x,o,o,x,x,o,o,o,o,o,x], 
         [x,x,x,o,o,x,x,o,x,x,o], 
         [o,o,o,o,o,x,o,o,o,o,x], 
         [o,x,o,x,x,x,o,x,o,x,o], 
         [x,o,x,o,x,o,x,o,o,o,x], 
         [o,o,o,x,o,o,o,x,x,x,x], 
         [x,x,x,x,o,o,o,x,o,x,o], 
         [x,o,x,x,x,x,x,x,x,x,o], 
         [o,x,o,o,o,x,x,x,o,x,x]]


def find_size(world, x, y):
  if world[y][x] != 'earth':
    return 0
  else:
    size = 1 # start count size from standing point with 1
    world[y][x] = 'already counted tile' # change the tile value once reached
    numrows = len(world)   # number of rows in 2 dimentional array
    numcols = len(world[0]) # number of cols in 2 dimentional array

    # each if statement to make sure that the next position doesn't go out of the array range
    if (x-1) >= 0 and (y-1) >= 0 and (x-1) < numcols and (y-1) < numrows:
      size += find_size(world, x-1, y-1)
    if (x) >= 0 and (y-1) >= 0 and (x) < numcols and (y-1) < numrows:
      size += find_size(world, x, y-1)
    if (x+1) >= 0 and (y-1) >= 0 and (x+1) < numcols and (y-1) < numrows:
      size += find_size(world, x+1, y-1)
    if (x-1) >= 0 and (y) >= 0 and (x-1) < numcols and (y) < numrows:
      size += find_size(world, x-1, y)
    if (x+1) >= 0 and (y) >= 0 and (x+1) < numcols and (y) < numrows:
      size += find_size(world, x+1, y)
    if (x-1) >= 0 and (y+1) >= 0 and (x-1) < numcols and (y+1) < numrows:
      size += find_size(world, x-1, y+1)
    if (x) >= 0 and (y+1) >= 0 and (x) < numcols and (y+1) < numrows:
      size += find_size(world, x, y+1)
    if (x+1) >= 0 and (y+1) >= 0 and (x+1) < numcols and (y+1) < numrows:
      size += find_size(world, x+1, y+1)

    return size


print("11x11 World Case: Continent size from tile({},{}) = {}.".format(5,5, find_size(World, 5, 5)))
#print("Continent size from tile({},{}) = {}.".format(0,0, find_size(World, 0, 0)))
#print("Continent size from tile({},{}) = {}.".format(6,10, find_size(World, 6, 10)))


# random array generator section
choices = [o, x]
#rand = random.choice(choices)
#print(rand)
M = 6 
N = 4
random_world = [[random.choice(choices) for i in range(N)] for j in range(M)]
print(random_world)

print("{}x{} Random World Case: Continent size from tile({},{}) = {}.".format(N,M, 0,0, find_size(random_world, 0, 0)))

  
