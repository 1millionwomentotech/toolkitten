import random
from pprint import pprint

# define size of world
size = 5 # might use user input in future

# generate world using list comprehension
world = [[random.randint(0,1) for x in range(size)] for x in range(size)]

# get random starting point
def get_start(size, matrix):
  x = random.randint(0,size-1)
  y = random.randint(0,size-1)
  if matrix[x][y]:
    return x, y
  else:
    get_start(size, matrix)

startX, startY = get_start(size, world)

pprint(world)
print(startX)
print(startY)