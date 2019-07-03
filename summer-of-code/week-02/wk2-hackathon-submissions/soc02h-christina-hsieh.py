from random import randint
import re

def create_board(filename):
  dice = set()
  board = ''
  file = open(filename, 'r')
  for line in file:
    dice.add(line.rstrip('\n'))
  while dice:
    board += dice.pop()[randint(0,5)]
  return [board[i:i+4] for i in range(0,len(board), 4)]

board = create_board('dice.txt')
# board = ['DNKO', 'EWTN', 'ELBH', 'QTCW']
print(board)

def check_prefix(word, dictionary):
  for entry in dictionary:
    if entry.startswith(word):
      return True
  return False

def load_dict(filename):
  word_list = set()
  file = open(filename, 'r')
  letters = ''.join(board)
  pattern = re.compile('[^'+letters+']').search
  for line in file:
    if not pattern(line.rstrip('\n')):
      word_list.add(line.rstrip('\n'))
  return word_list

boggle_dict = load_dict('dictionary.txt')
# print(boggle_dict)
found = []

def build_word(prefix, path):
  # check if prefix is a word
  if prefix in boggle_dict:
    found.append(prefix)
  # check if prefix starts a word
  if check_prefix(prefix, boggle_dict):
    coord = path[-1]
    for x in range(max(0, coord[0]-1), min(coord[0]+2, len(board))):
      for y in range(max(0, coord[1]-1), min(coord[1]+2, len(board))):
        if (x,y) not in path:
          build_word(prefix + board[x][y], path + ((x, y),))

def solve():
  for x in range(0, len(board)):
    for y in range(0, len(board)):
      build_word(board[x][y], ((x,y),))
  found.sort()
  score = 0
  for word in found:
    score += max(0, len(word) - 2)
  return {
    "score": score,
    "words": found
  }

print(solve())