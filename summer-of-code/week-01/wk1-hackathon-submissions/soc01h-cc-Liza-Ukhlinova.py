import random


def gen_world(n):
    return [[random.getrandbits(1) for __ in range(n)] for _ in range(n)]


def print_world(world):
    for row in world:
        print(row)


def gen_neighbours(i, j, n):
    if i != 0 and j != 0:
        yield (i - 1, j - 1)
    if i != 0:
        yield (i - 1, j)
    if i != 0 and j != n - 1:
        yield (i - 1, j + 1)
    if j != 0:
        yield (i, j - 1)
    if j != n - 1:
        yield (i, j + 1)
    if i != n - 1 and j != 0:
        yield (i + 1, j - 1)
    if i != n - 1:
        yield (i + 1, j)
    if i != n - 1 and j != n - 1:
        yield (i + 1, j + 1)


def find_island_square(world, x, y):
    if world[x][y] == 0:
        return 0
    queue = [(x, y)]
    check_cell(world, x, y, queue)
    return len(queue)


def check_cell(world, x, y, queue):
    size = len(world)
    for i, j in gen_neighbours(x, y, size):
        if world[i][j] == 1 and (i, j) not in queue:
            queue.append((i, j))
            check_cell(world, i, j, queue)


if __name__ == '__main__':
    n = int(input())
    rand_world = gen_world(n)
    print_world(rand_world)
    _x = int(input())  # [1, n]
    _y = int(input())  # [1, n]
    print(find_island_square(rand_world, _x + 1, _y + 1))

    # Test Case
    test = False
    if test:
        test_world = [[0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 0, 0, 1, 1, 0]]
        print(find_island_square(test_world, 4, 3))  # 6
