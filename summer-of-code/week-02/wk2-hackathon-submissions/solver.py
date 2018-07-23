import string
import random
from datetime import datetime

filename = 'sowpods-dictionary.txt'


def create_board(side: int):
    b = []
    for i in range(side):
        b.append(random.sample(string.ascii_lowercase, side))
    return b


def choose_starting_letters(count: int):
    return ''.join(random.sample(string.ascii_lowercase, count))


def preprocess():
    found = []
    looking_for = choose_starting_letters(2)
    print('Looking for the pattern {}'.format(looking_for))
    start = datetime.now()
    with open(filename, 'r', newline='') as infile:
        for line in infile:
            if looking_for in line:
                found.append(line.rstrip('\n'))
    duration = datetime.now() - start
    for item in found:
        print(item)
    print('For the pattern {} we found {} terms in {}:'.format(looking_for, len(found), duration))


def valid_operations(x: int, y: int, side: int) -> list:
    ops = []
    if y > 0:
        ops.append((x, y -1))
    if y < side - 1:
        ops.append((x, y+1))
    if x > 0:
        ops.append((x - 1, y))
        if y > 0:
            ops.append((x - 1, y - 1))
        if y < side - 1:
            ops.append((x - 1, y + 1))
    if x < side - 1:
        ops.append((x + 1, y))
        if y > 0:
            ops.append((x + 1, y - 1))
        if y < side - 1:
            ops.append((x + 1, y + 1))
    return ops

side = 4
#my_board = create_board(side)
my_board = [['l', 'w', 'k', 'x'], ['k', 'c', 'm', 'h'], ['d', 'u', 'x', 't'], ['k', 'o', 't', 'i']]

starting_point = (0,0)

word = (starting_point,)


#preprocess()

