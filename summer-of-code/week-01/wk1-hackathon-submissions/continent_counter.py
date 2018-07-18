import random
import operator

list_of_tiles = []
list_of_close_tiles = []
coordinates = (5, 5)

random.seed()
list_of_tiles = [(random.randint(0, 11), random.randint(0, 11)) for k in range(30)]  # here we have to add some code to not repeat tiles

sorted_by_x = sorted(list_of_tiles, key=operator.itemgetter(0, 1))
list_of_close_tiles.append(coordinates)

for item in list_of_tiles:
    if item[0] == coordinates[0] or item[0] == coordinates[0] - 1 or item[0] == coordinates[0] + 1:
        if item[1] == coordinates[1] or item[1] == coordinates[1] - 1 or item[1] == coordinates[1] + 1:
            if item != coordinates:
            list_of_close_tiles.append(item)

print(list_of_close_tiles)
