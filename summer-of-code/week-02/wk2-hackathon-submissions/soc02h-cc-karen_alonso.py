import random

filename = "dictionary.txt"
file = open(filename, mode='r')
dictionaryBoggle = set(word.strip() for word in file)
file.close()  

boggleBoard = []
diceReaded = [[False for j in range(0,4)] for i in range(0,4)]

points = {
  1: 0,
  2: 0,
  3: 1,
  4: 2,
  5: 3,
  6: 4,
  7: 5,
  8: 6,
  9: 7,
  10: 8,
  11: 9,
  12: 10,
  13: 11,
  14: 12,
  15: 13,
  16: 14,
}

class Result():
  def __init__(self, score, words):
    self.score  = score
    self.words   = words

def WordsFinder(board, i, j, wordString=''):

  if diceReaded[i][j] != False:
    return ''

  diceReaded[i][j] = True

  aboveExist = True
  belowExist = True
  leftExist = True
  rightExist = True

  if i <= 0:
    aboveExist = False
  if i >= 4 - 1:
    belowExist = False
  if j <= 0:
    leftExist = False
  if j >= 4 - 1:
    rightExist = False

  wordString += board[i][j]
  

  wordString = wordString + (WordsFinder(board, i-1, j-1) if aboveExist and leftExist else '')
  wordString = wordString + (WordsFinder(board, i-1, j) if aboveExist else '')
  wordString = wordString + (WordsFinder(board, i-1, j+1) if aboveExist and rightExist else '')

  #same row
  wordString = wordString + (WordsFinder(board, i, j-1) if leftExist else '')
  wordString = wordString + (WordsFinder(board, i, j+1) if rightExist else '')

  #below
  wordString = wordString + (WordsFinder(board, i+1, j-1) if belowExist and leftExist else '')
  wordString = wordString + (WordsFinder(board, i+1, j) if belowExist else '')
  wordString = wordString + (WordsFinder(board, i+1, j+1) if belowExist and rightExist else '')

  ScoreCounter(wordString)
  return wordString


def ScoreCounter(boggleWord):
  totalPoints = 0
  sizeBoggleWord = len(boggleWord)


  if boggleWord in dictionaryBoggle:
    if boggleWord in boggleWords.words:
      return
    else:
      totalPoints = points[sizeBoggleWord]
      boggleWords.words.append(boggleWord)

  boggleWords.score += totalPoints


def getRow(dices, index):
  boggleRow = []
  rangeIndex = index if index == 0 else index * 4

  for i in range (rangeIndex, rangeIndex + 4):
    boggleRow.append(random.choice(dices[i]))

  return boggleRow


def CreateBoard(dices):
  for i in range (0, 4):
    boggleBoard.append(getRow(dices, i))


def DrawBoard(board):
  for i in range (0, 4):
    print(board[i])


dices = [
  ['A','A','E','E','G','N'],
  ['E','L','R','T','T','Y'],
  ['A','O','O','T','T','W'],
  ['A','B','B','J','O','O'],
  ['E','H','R','T','V','W'],
  ['C','I','M','O','T','U'],
  ['D','I','S','T','T','Y'],
  ['E','I','O','S','S','T'],
  ['D','E','L','R','V','Y'],
  ['A','C','H','O','P','S'],
  ['H','I','M','N','Q','U'],
  ['E','E','I','N','S','U'],
  ['E','E','G','H','N','W'],
  ['A','F','F','K','P','S'],
  ['H','L','N','N','R','Z'],
  ['D','E','I','L','R','X']
]


boggleWords = Result(0, [])
CreateBoard(dices)
DrawBoard(boggleBoard)


for i in range(0,4):
  for j in range(0,4):
    WordsFinder(boggleBoard, i, j)
    diceReaded = [[False for j in range(0,4)] for i in range(0,4)]


print('Accepted words: ', sorted(boggleWords.words))
print('Total score: ', boggleWords.score)
