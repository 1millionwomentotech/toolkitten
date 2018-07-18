import random
from pprint import pprint

# define size of world
size = 11 # might use user input in future

# generate world using list comprehension
world = [[random.randint(0,1) for x in range(size)] for x in range(size)]
pprint(world)

# get random starting point
def get_start(matrix):
  x = random.randint(0, len(matrix) - 1)
  y = random.randint(0, len(matrix) - 1)
  if matrix[x][y]:
    return (x, y)
  return get_start(matrix)

start = get_start(world)

print(start)

# walk from starting point
# use stack to track path and set to track count
path = [start]
land = set()
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
    # back = stack.pop()
    walk(stack.pop(), matrix, stack, land)

walk(start, world, path, land)

print(len(land))