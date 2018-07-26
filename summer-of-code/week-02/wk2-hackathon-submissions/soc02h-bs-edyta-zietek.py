#!/usr/bin/env python3
import random
filename = "dictionary.txt"
file = open(filename, encoding= "utf8")
dictionary = file.readlines()
dictionary = set([x.strip() for x in dictionary])

#New version of Boggle used
boggle_board =[['A', 'A', 'E', 'E', 'G', 'N'],
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
['D', 'E', 'I', 'L', 'R', 'X']]
game_board = []
for i in range(len(boggle_board)):
    dice = boggle_board[i]
    game_board.append(random.choice(dice))
# Shuffle the letters for part of the game
random.shuffle(game_board)
# grid size
n = 4
# Split list for similar in boggle game
final = [game_board[i * n:(i+1)*n] for i in range((len(game_board)+n-1)//n)]
print(final)

queue = [(2,2), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (2,1), (0,0), (2,3), (2,0), (3,0), (3,1), (3,2), (3,3)]
path = []
words = []

def boggle_calc(path, coordinate):
    #print(path.count(coordinate))
    if (coordinate in path) == True:
        return
    path.append(coordinate)
    letter = ""
    for i in range(len(path)):
        a,b = path[i]
        letter += final[a][b]
    word_exist = letter in dictionary
    if word_exist and letter not in words and len(letter)>2:
        words.append(letter)
        print(letter)
        #print(words)


    if coordinate[0]>0 and coordinate[1]>0:
        temp = path[:]
        boggle_calc(temp, (coordinate[0]-1, coordinate[1]-1))
    if coordinate[1]>0:
        temp = path[:]
        boggle_calc(temp, (coordinate[0] , coordinate[1]-1))
    if coordinate[1]>0 and coordinate[0] < 3:
        temp = path[:]
        boggle_calc(temp, (coordinate[0]+1, coordinate[1]-1))
    if coordinate[0]>0:
        temp = path[:]
        boggle_calc(temp, (coordinate[0]-1, coordinate[1] ))
    if coordinate[0]<3:
        temp = path[:]
        boggle_calc(temp, (coordinate[0]+1, coordinate[1] ))
    if coordinate[1]<3 and coordinate[0] >0:
        temp = path[:]
        boggle_calc(temp, (coordinate[0]-1, coordinate[1]+1))
    if coordinate[1] <3:
        temp = path[:]
        boggle_calc(temp, (coordinate[0] , coordinate[1]+1))
    if coordinate[0]<3 and coordinate[1]<3:
        temp = path[:]
        boggle_calc(temp, (coordinate[0]+1, coordinate[1]+1))


while len(queue) > 0:
    path.clear()
    p = queue.pop(0)
    boggle_calc(path, p)

score = 0
for i in range(len(words)):
    l = len(words[i])
    score += l-2

words.sort()
result = {
    "score": score,
    "words": words 
}
print(result)