from math import fabs
from random import randint
import time

# Check if the variable is an integer
def isInt(intVar):
  try:
    int(intVar)
    return True
  except ValueError:
    return False

# Read the dictionary file provided
def readDictFile(fileName):
    f = open(fileName, "r")

    fileRead = []
    fileRead = f.read().splitlines()
    for line in f:
        fileRead.append(line)

    return fileRead

# Return the number of dices according to the board size
def createDices(size):
    dices = [['A', 'A', 'E', 'E', 'G', 'N'],
             ['E', 'L', 'R', 'T', 'T', 'Y'],
             ['A', 'O', 'O', 'T', 'T', 'W'],
             ['A', 'B', 'B', 'J', 'O', 'O'],
             ['E', 'H', 'R', 'T', 'V', 'W'],
             ['C', 'I', 'M', 'O', 'T', 'U'],
             ['D', 'I', 'S', 'T', 'T', 'Y'],
             ['E', 'I', 'O', 'S', 'S', 'T'],
             ['D', 'E', 'L', 'R', 'V', 'Y'],
             ['A', 'C', 'H', 'O', 'P', 'S'],
             ['H', 'I', 'M', 'N', 'Q', 'U'],
             ['E', 'E', 'I', 'N', 'S', 'U'],
             ['E', 'E', 'G', 'H', 'N', 'W'],
             ['A', 'F', 'F', 'K', 'P', 'S'],
             ['H', 'L', 'N', 'N', 'R', 'Z'],
             ['D', 'E', 'I', 'L', 'R', 'X'],
             ['A', 'A', 'E', 'E', 'G', 'N'],
             ['E', 'L', 'R', 'T', 'T', 'Y'],
             ['A', 'O', 'O', 'T', 'T', 'W'],
             ['A', 'B', 'B', 'J', 'O', 'O'],
             ['E', 'H', 'R', 'T', 'V', 'W'],
             ['C', 'I', 'M', 'O', 'T', 'U'],
             ['D', 'I', 'S', 'T', 'T', 'Y'],
             ['E', 'I', 'O', 'S', 'S', 'T'],
             ['D', 'E', 'L', 'R', 'V', 'Y']]

    return dices[0:size*size]

# Print the Boggle board
def printBoard(board, size):
    for x in range(size):
        print(board[x])

# Create the Boggle board according to the size provided
def createBoard(size):
    dices = createDices(size)
    line = []
    matrix = []

    for x in range(size):
        for y in range(size):
            dice = randint(1, len(dices)) - 1
            letter = dices[dice][randint(0, 5)]
            line.append(letter)
            dices.pop(dice)
        matrix.append(line)
        line = []

    return matrix

# First attempt, create all possible words in Boggle boardself
# Down side, takes too long and requires making deep copies of the board
# def getWord(markedBoard, size, curLine, curCol, wordSize, word, wordsList):
#     if(wordSize == 0):
#         if (word in wordsList):
#             return
#         return wordsList.append(word)
#     elif (curLine == size or curCol == size or curLine < 0 or curCol < 0 or markedBoard[curLine][curCol] == 'XX'):
#         return
#
#     letter = markedBoard[curLine][curCol]
#     markedBoard[curLine][curCol] = 'XX'
#     keepBoard = copy.deepcopy(markedBoard)
#
#     getWord(markedBoard, size, curLine, curCol + 1, wordSize - 1, word + letter, wordsList)
#     markedBoard = copy.deepcopy(keepBoard)
#
#     getWord(markedBoard, size, curLine, curCol - 1, wordSize - 1, word + letter, wordsList)
#     markedBoard = copy.deepcopy(keepBoard)
#
#     getWord(markedBoard, size, curLine - 1, curCol, wordSize - 1, word + letter, wordsList)
#     markedBoard = copy.deepcopy(keepBoard)
#
#     getWord(markedBoard, size, curLine - 1, curCol - 1, wordSize - 1, word + letter, wordsList)
#     markedBoard = copy.deepcopy(keepBoard)
#
#     getWord(markedBoard, size, curLine - 1, curCol + 1, wordSize - 1, word + letter, wordsList)
#     markedBoard = copy.deepcopy(keepBoard)
#
#     getWord(markedBoard, size, curLine + 1, curCol, wordSize - 1, word + letter, wordsList)
#     markedBoard = copy.deepcopy(keepBoard)
#
#     getWord(markedBoard, size, curLine + 1, curCol - 1, wordSize - 1, word + letter, wordsList)
#     markedBoard = copy.deepcopy(keepBoard)
#
#     getWord(markedBoard, size, curLine + 1, curCol + 1, wordSize - 1, word + letter, wordsList)
#
# def checkWords(wordsList, dict, validWords):
#     points = 0
#     for w in wordsList:
#         if(w in dict):
#             validWords.append(w)
#             points = points + len(w) - 2
#
#     return points

# Put the letters and its position on the board on a dictionary
def createLettersHashMap(board, boardize):
    letters = {}
    for i in range(boardize):
        for j in range(boardize):
            if(board[i][j] in letters):
                letters[board[i][j]].append([i, j])
            else:
                letters[board[i][j]] = [[i, j]]

    return letters

# Find all the words that are possible to assemble on the board from the dictionary
def findWords(dict, letters, boardSize):
    wordsFound = []
    points = 0

    # For each word in the dictionary
    for word in dict:
        wordSize = len(word)
        # Check the length of the word to see if it is possible to build it
        if(wordSize >= 3 and wordSize <= boardSize*boardSize):
            # Check if the first letter of the word is in the letters list
            if(word[0] not in letters):
                continue

            # Since there may be more than one letter of each on the board, check all of them
            letterPos = letters[word[0]]
            for curPos in letterPos:
                foundWholeWord = True
                lettersPos = [curPos]
                # Loop through all of the letters in the word
                for i in range(1, wordSize):
                    if(word[i] not in letters):
                        foundWholeWord = False
                        break

                    nextLetterPos = letters[word[i]]
                    # If found the letter in the map, check all possible positions
                    for nextPos in nextLetterPos:
                        # Check if we have already used the letter in this position
                        if(nextPos in lettersPos):
                            foundWholeWord = False
                            continue

                        # Check if the letter is close to the next one
                        if((nextPos[0] == curPos[0] + 1 or nextPos[0] == curPos[0] - 1 or nextPos[0] == curPos[0]) and
                           (nextPos[1] == curPos[1] + 1 or nextPos[1] == curPos[1] - 1 or nextPos[1] == curPos[1])):
                            lettersPos.append(nextPos)
                            curPos = nextPos
                            break
                        else:
                            foundWholeWord = False
                            continue

                # If the whole word could be assembled, count the points and add it to the words found list
                if(foundWholeWord):
                    wordsFound.append(word)
                    points = points + wordSize - 2
                    break

    result = { "score": points,
    "words": wordsFound}

    return result

# Main program
t1=time.time()
dictFile = input("Select dictionary file to be used:")
dict = readDictFile(dictFile)

# Prompt the user for a size until it prompts an integer
boardSize = input("Select Boggle board size:")
while isInt(boardSize) != True:
    boardSize = input("Boggle board size must be an integer:")

# Get positive value of size
boardSize = int(fabs(int(boardSize)))

# Creates the board according to the users choice
board = createBoard(boardSize)
printBoard(board, boardSize)

# Add all the letters in the board to the dictionary hash map
letters = createLettersHashMap(board, boardSize)

# Find all the words in the dictionary
print(findWords(dict, letters, boardSize))
t2=time.time()
print('Elapsed Time: ' + str(t2 - t1))
