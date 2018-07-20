###################
# Team Members:   #
# - gillybops     #
# - girijakumar   #
# - MirandaBlair  #
# - priyaka-xo    #
# - tltyogg       #
# - TWHou         #
###################

import random
from pprint import pprint

# generate world using list comprehension
def gen_world(size):
  return [[random.randint(0,1) for x in range(size)] for x in range(size)]

# get random starting point
def get_start(matrix):
  x = random.randint(0, len(matrix) - 1)
  y = random.randint(0, len(matrix) - 1)
  if matrix[x][y]:
    return (x, y)
  return get_start(matrix)

# walk from starting point
# use stack to track path and set to track count
def walk(point, matrix, stack, land):
  # add point to land
  land.add(point)
  # check adjacent points
  for i in range(-1, 2):
    for j in range(-1, 2):
      # get coord of new point
      x = point[0] + i
      y = point[1] + j
      # make sure new point is within the world
      if x < 0 or x >= len(matrix):
        x = point[0]
      if y < 0 or y >= len(matrix):
        y = point[1]
      # check if new point is land and not counted yet
      if matrix[x][y] and (x, y) not in land:
        # add new point to land
        path.append((x, y))
        # move to new point
        walk((x, y), matrix, stack, land)
  # reach end of land, retrace last step
  if stack:
    walk(stack.pop(), matrix, stack, land)

# define size of world
size = int(input('How big would this world be?: '))

world = gen_world(size)
print(f"This is your {size} x {size} world")
pprint(world)

start = get_start(world)
print(f"You will be starting at {start}")

path = [start]
land = set()

walk(start, world, path, land)
print(f"Your contient has {len(land)} title(s)")