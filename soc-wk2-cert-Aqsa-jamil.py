from random import choice
from string import ascii_uppercase
import logging
import time

# logging.basicConfig(level=logging.INFO)


def timeit(method):
    """Calculates time taken to run a function when called"""
    def timed(*args, **kw):
        t1 = time.time()
        result = method(*args, **kw)
        print ('%r %2.2f sec' % (method.__name__, time.time() -t1))
        return result

    return timed


def get_grid():
    """Return a dictionary of grid positions to random letters"""
    return {(x, y): choice(ascii_uppercase) for x in range(X) for y in range(Y)}


def get_neighbours():
    """Return a dictionary with all the neighbours surrounding a particular position"""
    neighbours = {}

    for position in grid:
        x, y = position
        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                     (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
        neighbours[position] = [p for p in positions if 0 <= p[0] < X and 0 <= p[1] < Y]
    return neighbours


def path_to_word(path):
    """Convert a list of grid positions to a word"""
    return ''.join([grid[p] for p in path])


def search(path):
    """Recursively search the grid for words"""
    word = path_to_word(path)
    logging.debug('%s: %s' % (path, word))
    if word not in stems:
        return
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbours[path[-1]]:
        if next_pos not in path:
            search(path + [next_pos])
        else:
            logging.debug('skipping %s because in path' % grid[next_pos])

def get_dictionary():
    """Return a list of uppercase english words, including word stems"""
    stems, dictionary = set(), set()
    with open('dictionary.txt') as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)

            for i in range(len(word)):
                stems.add(word[:i + 1])

    return dictionary, stems


@timeit
def get_words():
    """Search each grid position and return all the words found"""
    for position in grid:
        logging.info('searching %s' % str(position))
        search([position])
    return [path_to_word(p) for p in paths]


def print_grid(grid):
    """Print the grid as a readable string"""
    s = ''
    for y in range(Y):
        for x in range(X):
            s += grid[x, y] + ' '
        s += '\n'
    print (s)


size = X, Y = 4, 4
grid = get_grid()
neighbours = get_neighbours()
dictionary, stems = get_dictionary()
paths = []


print_grid(grid)
words = get_words()
print (words)
