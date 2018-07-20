import numpy as np
import queue as queue

map_size = int(input("Please enter size of the map: "))
#Validating Size of Map
while map_size <= 0:
    print("Invalid map size: {}! Value should be > 0".format(map_size))
    map_size = int(input("Please enter size of the map: "))

print("Map size: {}".format(map_size))

#Making the actual Map
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


continent = np.zeros((map_size, map_size), np.int8)

Q = queue.Queue()

#From the start
print("Mapping the continent from the starting tile...")
Q.put({'x': stating_tile[0], 'y': stating_tile[1]})
while not Q.empty():
    visit_adjacent_tiles(map_size)

print("This is the map of the continent you are standing (marked as 1)")
print(continent)
print("--------------------------------")

# calculate size
print("Size: {}".format(continent.sum()))
