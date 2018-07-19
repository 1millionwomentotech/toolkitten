import numpy as np
import queue as queue

# Civilization map assignment
# @author: Vi Nguyen

# Getting map size
map_size = int(input("Please enter size of the map: "))
while map_size <= 0:
    print("Invalid map size: {}! Value should be > 0".format(map_size))
    map_size = int(input("Please enter size of the map: "))

print("Map size: {}".format(map_size))

# create map
map = np.random.random_integers(0, 1, size = (map_size, map_size))
print("Civilization map, 0 is water and 1 is land")
print(map)
print("---------------------")

def retrieve_starting_tile():
    tile = input("Starting tile, for example: '1,3' -- row 1 and column 3. Note: negative value is rounded to 1... ")
    tile = tile.split(',')
    try:
        return [max(int(tile[0]), 1) - 1, max(int(tile[0]), 1) - 1]
    except:
        print("Invalid starting tile: {}! ".format(tile))
        return retrieve_starting_tile()

# Landing on the map...
stating_tile = retrieve_starting_tile()
while 1:
    try:
        if map[stating_tile[0], stating_tile[1]] == 1:
            break
        print("Invalid starting tile: {} {}! "
              "It is a water tile".format(stating_tile[0] + 1, stating_tile[1] + 1))
        stating_tile = retrieve_starting_tile()
    except:
        print("Invalid starting tile: {} {}! "
              "It doesn't exist".format(stating_tile[0] + 1, stating_tile[1] + 1))
        stating_tile = retrieve_starting_tile()

"""
Visit all adjacent tiles of a given tile
if an adjacent tile is connected and is a land piece,
mark it in the continent matrix
and put it in the queue to visit it next time
"""
def visit_adjacent_tiles(s):
    tile = q.get()
    x = tile['x']
    y = tile['y']

    if map[(x, y)] == 0 or continent[(x, y)] == 1:
        return
    else:
        continent[(x, y)] = 1

    print("Visiting adjacent tiles of ({},{})".format(x, y))

    for x, y in [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
        if 0 <= x < s and 0 <= y < s and map[(x, y)] == 1 and continent[(x, y)] == 0:
            continent[(x, y)] == 1
            q.put({'x': x, 'y': y})
    return


# mark continent
continent = np.zeros((map_size, map_size), np.int8)

q = queue.Queue()

# mapping the continent from the starting tile...
print("Mapping the continent from the starting tile...")
q.put({'x': stating_tile[0], 'y': stating_tile[1]})
while not q.empty():
    visit_adjacent_tiles(map_size)

print("This is the map of the continent you are standing (marked as 1)")
print(continent)
print("--------------------------------")

# calculate size
print("Size: {}".format(continent.sum()))








