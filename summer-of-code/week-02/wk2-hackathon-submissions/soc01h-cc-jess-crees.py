# Boggle Solver

import copy
import random



###
# DICE CONFIGURATION
###
dice = [
    ['A', 'A', 'E', 'E', 'G', 'N'],
    ['A', 'B', 'B', 'J', 'O', 'O'],
    ['A', 'C', 'H', 'O', 'P', 'S'],
    ['A', 'F', 'F', 'K', 'P', 'S'],
    ['A', 'O', 'O', 'T', 'T', 'W'],
    ['C', 'I', 'M', 'O', 'T', 'U'],
    ['D', 'E', 'I', 'L', 'R', 'X'],
    ['D', 'E', 'L', 'R', 'V', 'Y'],
    ['D', 'I', 'S', 'T', 'T', 'Y'],
    ['E', 'E', 'G', 'H', 'N', 'W'],
    ['E', 'E', 'I', 'N', 'S', 'U'],
    ['E', 'H', 'R', 'T', 'V', 'W'],
    ['E', 'I', 'O', 'S', 'S', 'T'],
    ['E', 'L', 'R', 'T', 'T', 'Y'],
    ['H', 'I', 'M', 'N', 'U', 'Qu'],
    ['H', 'L', 'N', 'N', 'R', 'Z'],
]



###
# GLOBALS
###
board = []
dictionary = []
found_words = []
score = 0;
result = {}



###
# FUNCTIONS
###
def depthFirstSearch(x, y, string, visited):
    global possible_words

    n = len(board)

    # Check if this coordinate exists on the board
    if x >= int(n) or y >= int(n) or x < 0 or y < 0:
        return

    # Check if this coordinate has already been visited
    if visited[x][y] != True:
        # Add the character at this coordinate to a string
        string += board[x][y]

        # Check if string is a word in the dictionary
        isWord(string)

        # Mark this coordinate as visited
        visited[x][y] = True


    # NEED SOME KIND OF LOOP HERE FOR BACKTRACKING THE PATH


    # Recursively run the function again
    if (x-1 >= int(n) or y >= int(n) or x < 0 or y < 0) == False:
        if visited[x-1][y] != True:
            string += board[x-1][y]
            isWord(string)
            visited[x-1][y] = True
            depthFirstSearch(x-1, y, string, visited)

    if (x+1 >= int(n) or y >= int(n) or x < 0 or y < 0) == False:
        if visited[x+1][y] != True:
            string += board[x+1][y]
            isWord(string)
            visited[x+1][y] = True
            depthFirstSearch(x+1, y, string, visited)

    if (x >= int(n) or y-1 >= int(n) or x < 0 or y < 0) == False:
        if visited[x][y-1] != True:
            string += board[x][y-1]
            isWord(string)
            visited[x][y-1] = True
            depthFirstSearch(x, y-1, string, visited)

    if (x >= int(n) or y+1 >= int(n) or x < 0 or y < 0) == False:
        if visited[x][y+1] != True:
            string += board[x][y+1]
            isWord(string)
            visited[x][y+1] = True
            depthFirstSearch(x, y+1, string, visited)

    if (x-1 >= int(n) or y+1 >= int(n) or x < 0 or y < 0) == False:
        if visited[x-1][y+1] != True:
            string += board[x-1][y+1]
            isWord(string)
            visited[x-1][y+1] = True
            depthFirstSearch(x-1, y+1, string, visited)

    if (x+1 >= int(n) or y+1 >= int(n) or x < 0 or y < 0) == False:
        if visited[x+1][y+1] != True:
            string += board[x+1][y+1]
            isWord(string)
            visited[x+1][y+1] = True
            depthFirstSearch(x+1, y+1, string, visited)

    if (x+1 >= int(n) or y-1 >= int(n) or x < 0 or y < 0) == False:
        if visited[x+1][y-1] != True:
            string += board[x+1][y-1]
            isWord(string)
            visited[x+1][y-1] = True
            depthFirstSearch(x+1, y-1, string, visited)
    
    if (x-1 >= int(n) or y-1 >= int(n) or x < 0 or y < 0) == False:
        if visited[x-1][y-1] != True:
            string += board[x-1][y-1]
            isWord(string)
            visited[x-1][y-1] = True
            depthFirstSearch(x-1, y-1, string, visited)


    # Reset visited back to original board
    visited = copy.deepcopy(board)

    # Reset string
    string = ''



def isWord(string):
    global found_words

    for word in dictionary:
        if string.upper() == word.upper():
            found_words.append(string)



def shuffleDice(dice):
    global board
    letters_left = 16
    
    # For each dice in the dice array, choose one of the characters and add it to a board array
    for die in dice:
        random.shuffle(die)

        letter = random.choice(die)

        # if the number of letters left to choose is divisble by 4 then create a new array
        if letters_left % 4 == 0:
            board.append([])

        # add letter to the board
        if letters_left > 12:
            board[0].append(letter)
        elif letters_left > 8:
            board[1].append(letter)
        elif letters_left > 4:
            board[2].append(letter)
        else:
            board[3].append(letter)

        letters_left -= 1



# 1. Get Dictionary
with open('dictionary.txt') as d:
    for word in d:
        dictionary.append(word)
d.closed

dictionary = [x.strip() for x in dictionary]



# 2. Shuffle Dice
shuffleDice(dice)



# 3. Check board against dictionary
i = 0
while i <= len(board):
    j = 0
    while j <= len(board):
        visited = copy.deepcopy(board)
        depthFirstSearch(i, j, '', visited)
        j += 1
    i += 1



# 4. Score words
for word in found_words:
    if len(word) > 2:
        score += len(word) - 2



# 5.Output result
for row in board:
    print(row)

print('\n')

result['score'] = score
result['words'] = sorted(found_words)

print(result)
