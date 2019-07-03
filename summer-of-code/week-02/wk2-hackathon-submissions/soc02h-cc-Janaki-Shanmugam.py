#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:35:24 2018

@author: shanmugamjanaki
"""

#Boggle is a 4x4 word game with 16 dice.
#
#Points are given in the following way:
#1 and 2 letter words = 0 points 
#3 letter words = 1 point 
#4 letter words = 2 points 
#5 letter words = 3 points
#(length of the word above 2)
#The longest possible word 16 letter word = 14 points
#
#When you build a word, you can only use one letter once: in other words,
#if you travel along the board and you used a letter, 
#you cannot use it again for the same word, however, you CAN use it for a new word.
#
#You can travel in any direction on the board, diagonal travel is allowed.
#
#The person with the most points win.
#
#Challenge: write a boggle solver that finds all possible words on a given board. 
#You should pick a fixed vocabulary (dictionary): Hasbro standard English dictionary
#
#Bonuses:
#fastest algorithm
#choose dictionary
#choose dice distribution
#extend to 3x3 and 5x5
#benchmark
#What is the MOST number of points possible in boggle? 
#That is, what is the holy grail of Boggle with a fixed dictionary?

##############################
# import SOWPODS (Scrabble) dictionary
##############################
filename = "sowpods.txt"
file = open(filename,'r')
dictionary = set(word.strip() for word in file)
# create set of prefixes (2 letters or longer) in words in dictionary
prefixes = set()
for word in dictionary:
    for i in range(1, len(word)+1):
        prefixes.add(word[:i])

# function to check if word exists in dictionary
def check_dict(word):
    return word.lower() in dictionary
# function to check prefixes
def check_prefix(string):
    return string.lower() in prefixes

##############################
# create Boggle_board
##############################
from numpy import random
# Specify board size (size*size)
size = 4

## create board with random letters - not always conducive for word formation
# boggle_board = [[chr(random.randint(65,90)) for j in range(size)] for i in range(size)]

# standard Boggle dice
dice = [["A","A","E","E","G","N"],
        ["E","L","R","T","T","Y"],
        ["A","O","O","T","T","W"],
        ["A","B","B","J","O","O"],
        ["E","H","R","T","V","W"],
        ["C","I","M","O","T","U"],
        ["D","I","S","T","T","Y"],
        ["E","I","O","S","S","T"],
        ["D","E","L","R","V","Y"],
        ["A","C","H","O","P","S"],
        ["H","I","M","N","Q","U"],
        ["E","E","I","N","S","U"],
        ["E","E","G","H","N","W"],
        ["A","F","F","K","P","S"],
        ["H","L","N","N","R","Z"],
        ["D","E","I","L","R","X"]]   
# initialise
boggle_board = [["" for j in range(size)] for i in range(size)]
visited = [[False for j in range(size)] for i in range(size)]
string = ''
word_list = ['']
d = 0
# roll dice
for i in range(size):
    for j in range(size):
        boggle_board[i][j] = str(random.choice(dice[d]))
        d += 1
        
print(boggle_board)

##############################
# solve Boggle
##############################

def solve(boggle_board,visited,word_list,x,y,string):
    
    if x< 0 and x == size and y<0 and y == size:
        return
    
    string += str(boggle_board[y][x])    
    print(string)
    visited[y][x] = True
    if check_prefix(string) == False:
        return 
    
    if check_dict(str(string)):
        word_list.append(str(string))
    
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if 0<=i<size and 0<=j<size:
                if visited[j][i] == False:
                    solve(boggle_board,visited,word_list,i,j,string)

    return(word_list)
##############################        
#
for i in range(size):
    for j in range(size):
        word_list = solve(boggle_board,visited,word_list,i,j,string)
        visited = [[False for j in range(size)] for i in range(size)]
        string = ''

#word_list = solve(boggle_board,visited,word_list,0,1,string)
word_list.remove('')
print(word_list)

##############################
# Scoring
##############################

points = {3:1, 4:2, 5:3, 6:4, 7:5, 8:6, 9:7, 10:8, 
          11:9, 12:10, 13:11, 14:12, 15:13, 16:14}

score = 0

for i in range(len(word_list)):
    for j in range(3,16):
        if len(word_list[i]) == j:
            score += points[j]

print("Total points scored in this round is ",score,".")
