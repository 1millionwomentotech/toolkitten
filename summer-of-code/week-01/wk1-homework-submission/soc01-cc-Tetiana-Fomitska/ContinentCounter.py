import configparser
from WorldGenerator import WorldGenerator

config = configparser.ConfigParser()
config.read('config.properties')
length = int(config.get('Generated world', 'length'))
width = int(config.get('Generated world', 'width'))

generator = WorldGenerator()
world = generator.generate_world(length, width)


def generate_continents_statistics():
    checked_points = set()

    # While moving from point to point we mark 'land' points as checked and belonging to continent
    def check_neighbours(k, l):
        if checked_points.__contains__((k, l)):
            return
        checked_points.add((k, l))
        if world[k][l] > 0:
            continent.append((k, l))
        if world[k + 1][l] > 0:
            check_neighbours(k + 1, l)
        if world[k + 1][l + 1] > 0:
            check_neighbours(k + 1, l + 1)
        if world[k][l + 1] > 0:
            check_neighbours(k, l + 1)
        if world[k - 1][l + 1] > 0:
            check_neighbours(k - 1, l + 1)
        if world[k + 1][l - 1] > 0:
            check_neighbours(k + 1, l - 1)
        if world[k - 1][l] > 0:
            check_neighbours(k - 1, l)
        if world[k][l - 1] > 0:
            check_neighbours(k, l - 1)
        return

    continents = []
    for i in range(1, generator.length - 1):
        for j in range(1, generator.width - 1):
            if checked_points.__contains__((i, j)):
                continue
            if world[i][j] <= 0:
                checked_points.add((i, j))
            else:
                continent = []
                check_neighbours(i, j)
                continents.append(continent.__len__())
    return continents


# Print list of sizes of continents in descending order
print(sorted(generate_continents_statistics(), key=int, reverse=True))
