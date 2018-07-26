from random import randint

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

def check_prefix(word, dictionary):
  for entry in dictionary:
    if entry.startswith(word):
      return True
  return False

def load_dict(filename):
  word_list = set()
  file = open(filename, 'r')
  for line in file:
    # TODO: only add if all letters are on board
    word_list.add(line.rstrip('\n'))
  return word_list

boggle_dict = load_dict('dictionary.txt')
found = set()

def build_word(current, used):
  # add letter to word
  used.add(current)
  word = "".join([ board[x][y] for (x,y) in used ])
  # check if word in dict
  if word in boggle_dict:
    found.add(word)
  # check if word starts an entry
  if check_prefix(word, boggle_dict):
    for x in range(max(0, current[0]-1), min(current[0]+2, len(board))):
      for y in range(max(0, current[1]-1), min(current[1]+2, len(board))):
        if (x,y) not in used:
          build_word((x,y), used)

def solve():
  pass
