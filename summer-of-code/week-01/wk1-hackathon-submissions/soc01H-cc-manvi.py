import random
from queue import Queue

my_world = [[1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]

helper_array = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]


def make_neighbour_matrix(world):
    result = [[[] for x in range(0, len(world))] for y in range(0, len(world))]
    for i in range(len(world)):
        for j in range(len(world)):
            for k in helper_array:
                if i + k[0] < len(world) and i + k[0] >= 0 and j + k[1] < len(world) and j + k[1] >= 0 and world[i][j] == 1:
                    if world[i + k[0]][j + k[1]] == 1:
                        result[i][j].append((i + k[0], j + k[1]))
    return result


def bfs_count(neighbours, visited, i, j):
    result = 0
    q = Queue()
    q.put((i,j))
    while not q.empty():
        v = q.get()
        if not visited[v[0]][v[1]]:
            result += 1
            visited[v[0]][v[1]] = True
            for n in neighbours[v[0]][v[1]]:
                q.put((n[0], n[1]))
    return result


def count_the_continent(map, i, j):
    if map[i][j] == 0:
        return 0
    neighbours = make_neighbour_matrix(map)
    visited = [[False for x in range(0, len(neighbours))] for y in range(0, len(neighbours))]
    return bfs_count(neighbours, visited,  i, j)


print(count_the_continent(my_world, 0, 0)

def bfs_count_all(neighbours, map):
    visited = [[False for x in range(0, len(map))] for y in range(0, len(map))]
    result = []
    for i in range(0, len(neighbours)):
        for j in range(0, len(neighbours)):
            if not visited[i][j] and map[i][j] == 1:
                result.append(bfs_count(neighbours, visited, i, j))
    return result


def count_continents(map):    neighbours = make_neighbour_matrix(map)
   return bfs_count_all(neighbours, map)

print(count_continents(my_world))


def generate_world(size):
   world = [[random.randint(0, 1) for x in range(size)] for y in range(size)]
    return world


world_size = input('What size the world should be? ')

new_world = generate_world(int(world_size))

print(count_continents(new_world))