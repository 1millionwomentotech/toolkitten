import random
import operator

list_of_tiles = []
list_of_close_tiles = []


def generate_random_world():
    random.seed()
    list_of_tiles = [(random.randint(0, 11), random.randint(0, 11)) for k in range(30)]  # here we have to add some code to not repeat tiles
    return list_of_tiles


def sort_list_of_tiles_by_x_y(list_of_tiles):
    list_of_tiles = sorted(list_of_tiles, key=operator.itemgetter(0, 1))
    return list_of_tiles


def add_default_coordinates(coordinates):
    list_of_close_tiles.append(coordinates)
    return list_of_close_tiles


def count_area(list_of_tiles, coordinates, list_of_close_tiles):
    print(list_of_close_tiles)
    for item in list_of_tiles:
        if item[0] == coordinates[0] or item[0] == coordinates[0] - 1 or item[0] == coordinates[0] + 1:
            if item[1] == coordinates[1] or item[1] == coordinates[1] - 1 or item[1] == coordinates[1] + 1:
                if item != coordinates:
                    list_of_close_tiles.append(item)
    return list_of_close_tiles
