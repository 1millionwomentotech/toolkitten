import random as r
from collections import deque


# Cellular Automata Method for generating random continent-like elements:
# 1. Fill the first map randomly.
# 2. Create 'water' border.
# 3. Repeatedly create new maps using rules:
#   3.1 Merging 'bays': analyzing neighbors to make them homogeneous.
#   3.2 Removing redundant transitions.

class WorldGenerator:

    WATER = 0
    LAND = 1

    def __init__(self):
        self.world = [[]]
        self.length = 0
        self.width = 0

    def generate_world(self, length, width):
        self.length = length
        self.width = width
        self.world = [[r.randint(-1,1) for x in range(width)] for y in range(length)]
        self.create_border()

        # Less than 3 iterations will create more islands, more iterations - bigger continents
        for counter in range(1, 4):
            for x in range(1, self.length - 1):
                for y in range(1, self.width - 1):
                    self.merge_bays(x, y)

        self.delete_redundant_transitions(x, y)
        self.print_world()
        return self.world

    def create_border(self):
        for j in range(0, self.length):
            self.world[j][0] = self.WATER
            self.world[j][self.width -1] = self.WATER
        for j in range(0, self.width):
            self.world[0][j] = self.WATER
            self.world[self.length - 1][j] = self.WATER

    def print_world(self):
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                if self.world[i][j] > 0 :
                    print('.', end=' ')
                else:
                    print('#', end=' ')
            print()

    def merge_bays(self, x, y):
        area = []
        area.append(self.world[x-1][y])
        area.append(self.world[x][y-1])
        area.append(self.world[x][y+1])
        area.append(self.world[x][y])
        if area.count(self.LAND) > area.count(self.WATER):
            self.world[x][y] = 1

    # Check if we have something like this:
    #     ...    .#.
    #     #.#    ...
    #     ...    .#.
    def delete_redundant_transitions(self, x, y):
        if self.world[x][y] > 0:
            world = self.world
            if is_straight_transition(world, x, y) or is_diagonal_transition(world, x, y):
                self.world[x][y] = 0


def is_straight_transition(world, x, y):
    return (world[x - 1][y] > 0 and world[x + 1][y] > 0) or (world[x][y - 1] > 0 and world[x][y + 1] > 0)


def is_diagonal_transition(world, x, y):
    return (world[x + 1][y - 1] > 0 >= world[x][y - 1] and world[x + 1][y] <= 0) or (
            world[x + 1][y + 1] > 0 >= world[x][y + 1] and world[x + 1][y] <= 0)



