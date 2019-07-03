from datetime import datetime

filename = 'sowpods-dictionary.txt'

"""
import string
import random

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
            if line.startswith(looking_for):
                found.append(line.rstrip('\n'))
    duration = datetime.now() - start
    for item in found:
        print(item)
    print('For the pattern {} we found {} terms in {}:'.format(looking_for, len(found), duration))
"""


def decode_word(word: tuple, board: list):
    decoded = ''
    for item in word:
        decoded += board[item[0]][item[1]]
    return decoded


def search_in_dict(word: tuple, board: list):
    found = []
    looking_for = decode_word(word, board)
    with open(filename, 'r', newline='') as infile:
        for line in infile:
            if line.startswith(looking_for):
                found.append(line.rstrip('\r\n'))
    return found


def search_in_list(looking_for, all_words):
    full_match = []
    candidates = []
    for a in all_words:
        if a == looking_for:
            full_match.append(a)
        elif a.startswith(looking_for):
            candidates.append(a)
    return full_match, candidates


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


def search_for_words(word, board, side, all_words):
    full_matches = []
    last_position = word[-1]

    # for each of valid operations (but valid only wrt the size of a board)
    for valid_op in valid_operations(*last_position, side):
        # if a coordinate is already in the word
        if valid_op in word:
            # that would be a cycle in the word graph, illegal operation
            continue
        # a new word (coordinates)
        word = (*word, valid_op)
        # decode coords to letters
        decoded_word = decode_word(word, board)
        # search for exact matches and filter potential candidates for longer words
        current_full_match, remaining_words = search_in_list(decoded_word, all_words)
        # if any exact match found, add it to the list
        full_matches.extend(current_full_match)
        # if there are still any words beginning with the decoded_word, keep processing
        if len(remaining_words) > 0:
            full_matches.extend(search_for_words(word, board, side, remaining_words))
    # return all the exact matches found
    return full_matches


def solve(biggle):

    if len(biggle) != len(biggle[0]):
        raise ValueError('Sorry, but a biggle has to be square!')
    result = []
    side = len(biggle)
    for i in range(side):
        for j in range(side):
            last_position = (i, j)
            for valid_op in valid_operations(*last_position, side):
                word = (last_position, valid_op)
                all_words = search_in_dict(word, biggle)
                result.extend(search_for_words(word, biggle, side, all_words))
    return result


if __name__ == '__main__':
    my_board2 = [['t', 'g', 'a', 's'], ['w', 'i', 't', 'h'], ['a', 's', 'e', 'y'], ['l', 'e', 'u', 'g']]
    start = datetime.now()
    solved = solve(my_board2)
    duration = datetime.now() - start
    print(f'Found {len(solved)} in {duration} s')


