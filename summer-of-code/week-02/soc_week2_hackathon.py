import random
import operator
import itertools

dice = ['AAEEGN',
        'ELRTTY',
        'AOOTTW',
        'ABBJOO',
        'EHRTVW',
        'CIMOTU',
        'DISTTY',
        'EIOSST',
        'DELRVY',
        'ACHOPS',
        'HIMNQU',
        'EEINSU',
        'EEGHNW',
       'AFFKPS',
        'HLNNRZ',
      'DEILRX' ]

possible_movements = [(0,-1), (-1, -1), (-1, 0),(-1,1), (0, 1), (1, 1), (1, 0), (1, -1)]

'opens dictionary and puts each word into words list'
with open("dictionary.txt", "r") as f:
    s = f.read()
dict_words = s.splitlines()

'generates letters from random roll of dice'
def dice_roll():
    letters = []
    for di in dice:
        letters.append(di[random.randint(0,5)])
    random.shuffle(letters)
    print(letters)

    return letters


'filters dictionary by all possible words given letter counts'
def find_possible_words(letters):
    possible_words = []
    for word in dict_words:
        truth_tester = 1
        for letter in word:
            truth_tester = word.count(letter) <= letters.count(letter) * truth_tester
        if truth_tester == 1:
            possible_words.append(word)
    return possible_words


'gets coords for a word in list of letters, then generates all possible paths (whether legal or not)'
def check_words(word, letters):
    raw_coords_path = []
    for letter in word:
        raw_coords = []
        locations = [i for i, x in enumerate(letters) if x == letter]
        for location in locations:
            raw_coords.append(location)
        raw_coords_path.append(raw_coords)

    #generates all possible paths for the word
    all_paths = list(itertools.product(*raw_coords_path))
    for path in all_paths:
        if len(set(path)) != len(path):
            all_paths.remove(path)
    return all_paths


'generates coords in 4*4 grid given number in list'
def generate_coordinates(location):
    coords = (location/4, location % 4)
    return coords

'checks if all moves in path legal'
def check_for_legal_moves(all_paths):
    any_path_checker = 0

    for num_path in range(len(all_paths)):
        path = []
        one_path_checker = 1

        for num_letter in range(len(all_paths[0])-1):
            path.append(all_paths[num_path][num_letter])
            coord1 = generate_coordinates(all_paths[num_path][num_letter])
        coord2 = generate_coordinates(all_paths[num_path][num_letter+1])
            movement = tuple(map(operator.sub, coord1, coord2))
            one_path_checker = one_path_checker * movement in possible_movements
    any_path_checker += one_path_checker

    return any_path_checker > 0

result = {}
'master function to roll dice and generate results'
def roll_and_run():
    all_legal_words = []
    score = 0
    letters_available = dice_roll()
    possible_words = find_possible_words(letters_available)
    for word in possible_words:
        paths = check_words(word, letters_available)
        word_is_legal = check_for_legal_moves(paths)
        if word_is_legal:
            all_legal_words.append(word)
            score += len(word)-2
    result['Words'] = all_legal_words
    result['Score'] = score
    return result

print(roll_and_run())