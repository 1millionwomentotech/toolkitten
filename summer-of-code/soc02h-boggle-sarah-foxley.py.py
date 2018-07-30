#The Boggle Solver Problem

#We were challenged to build a Boggle Solver in Python and this is the main solution.

#This solution:
#   - Generates a random 4x4 board by making a random selection for each dice based on the 6 sides available in a
#       standard board.
#   - Using the list of permutations available (loaded as pickle files) generates a list of possible words based on rules
#   - Compares the resulting words with the dictionary provided and returns only those words contained within he dictionary
#   - provides a summary of the maximum score that can be made from the board and a list of the words that can be created,
#       sorted by length of word
#   - Indicates how long it took for the solution to be provided. This is usually between 1 minute and 1 minute 15 seconds.


#Note:
#In the game of Boggle words can only be created by selecting a letter adjacent to the previous letter (left, right, up,
#down, or diagonally) and letters can not be reused. As the possible number of permutations is so large it takes around an
#hour to generate these from scratch. As the permutations are created using grid references for each die (i.e. (0,0) is the top left hand die
#and (3,3) is the bottom right) these will never change. Therefore I captured lists of all the possible permutations and saved them
#using pickling to enable them to be loaded into this program and used straight away to save time. As a result this solution
#only works for a standard Boggle Board of 4x4.

#Dictionary used was downloaded from https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt



#Libraries
#I imported libraries to assist with timing how long the program runs, importing pickle files,
#working out frequency of different sized words and selecting letters at random
from timeit import default_timer as timer
import pickle
from collections import Counter
import random


#Builds the dictionary from the text file provided
def buildDictionary():
    global dictionary_words
    dictionary_words = []
    with open("dictionary.txt", 'r') as f:
        for line in f:
            dictionary_words.append(line.rstrip())
    dictionary_words = set(dictionary_words)
    return dictionary_words


#This was the static board created to enable testing of the various parts of the program
def staticBoard():
    global boggle_board
    boggle_board = dict()
    boggle_board[(0,1)] = 'S'
    boggle_board[(1,2)] = 'L'
    boggle_board[(3,2)] = 'E'
    boggle_board[(0,0)] = 'R'
    boggle_board[(3,3)] = 'U'
    boggle_board[(3,0)] = 'T'
    boggle_board[(3,1)] = 'I'
    boggle_board[(2,1)] = 'D'
    boggle_board[(0,2)] = 'O'
    boggle_board[(2,0)] = 'W'
    boggle_board[(1,3)] = 'H'
    boggle_board[(2,3)] = 'H'
    boggle_board[(2,2)] = 'E'
    boggle_board[(1,0)] = 'I'
    boggle_board[(0,3)] = 'T'
    boggle_board[(1,1)] = 'O'
    
  
#This is based on the new list of die faces provided at
#https://www.boardgamegeek.com/thread/300565/review-boggle-veteran-and-beware-different-version
def randomBoggleBoard():
    global boggle_board
    boggle_board = dict()
    die1 = ['A', 'A', 'E', 'E', 'G', 'N']
    boggle_board[(0,0)] = random.choice(die1)
    die2 = ['E', 'L', 'R', 'T', 'T', 'Y']
    boggle_board[(0,1)] = random.choice(die2)
    die3 = ['A', 'O', 'O', 'T', 'T', 'W']
    boggle_board[(0,2)] = random.choice(die3)
    die4 = ['A', 'B', 'B', 'J', 'O', 'O']
    boggle_board[(0,3)] = random.choice(die4)
    die5 = ['E', 'H', 'R', 'T', 'V', 'W']
    boggle_board[(1,0)] = random.choice(die5)
    die6 = ['C', 'I', 'M', 'O', 'T', 'U']
    boggle_board[(1,1)] = random.choice(die6)
    die7 = ['D', 'I', 'S', 'T', 'T', 'Y']
    boggle_board[(1,2)] = random.choice(die7)
    die8 = ['E', 'I', 'O', 'S', 'S', 'T']
    boggle_board[(1,3)] = random.choice(die8)
    die9 = ['D', 'E', 'L', 'R', 'V', 'Y']
    boggle_board[(2,0)] = random.choice(die9)
    die10 = ['A', 'C', 'H', 'O', 'P', 'S']
    boggle_board[(2,1)] = random.choice(die10)
    die11 = ['H', 'I', 'M', 'N', 'Q', 'U']
    boggle_board[(2,2)] = random.choice(die11)
    die12 = ['E', 'E', 'I', 'N', 'S', 'U']
    boggle_board[(2,3)] = random.choice(die12)
    die13 = ['E', 'E', 'G', 'H', 'N', 'W']
    boggle_board[(3,0)] = random.choice(die13)
    die14 = ['A', 'F', 'F', 'K', 'P', 'S']
    boggle_board[(3,1)] = random.choice(die14)
    die15 = ['H', 'L', 'N', 'N', 'R', 'Z']
    boggle_board[(3,2)] = random.choice(die15)
    die16 = ['D', 'E', 'I', 'L', 'R', 'X']
    boggle_board[(3,3)] = random.choice(die16)
    
    
  
    
#This imports a pickle file and converts all the grid references to the corresponding letter for that die
#Chose to use list comprehension rather that loop to convert grid references to words
#Made sure to concatenate letters into words within each list
#Converted list to set and back to list in an effort to remove any duplicate words that may have occurred
def replaceLetters(aFile):
    global list_words 
    list_words = []
    convert_words = newCombos = pickle.load(open(aFile,"rb"))
    convert_words = [[boggle_board.get(x) for x in line] for line in convert_words]
    list_words = [''.join(item) for item in convert_words]
    final_words = set(list_words)
    list_words = list(final_words)

#This compares the list of words generated with the dictionary to give only actual, recognised words for the solution
def legalwords():
    global results
    word_set = set(list_words)
    initial_results = word_set.intersection(dictionary_words)
    results = results + list(initial_results)


#calculates the score for the solution
def score():
    global results, score
    score_card = Counter(map(len,results))
    score = 0
    for key, value in score_card.items():
        score = score + ((key-2) * value)
    

#Ensures the results are generated as prescribed in the 
def finalDisplay():
    global results, score
    final_results = dict()
    final_results['score'] = score
    final_results['words'] = results
    print('results =', final_results)
    


    
#Pulls all the functions together to generate the results
def sim1():
    global results
    buildDictionary()
    randomBoggleBoard()
    results = []
    comboFiles = ['legalCombinations1.p', 'legalCombinations2.p', 'legalCombinations3.p', 'legalCombinations4.p', 'legalCombinations5.p', 'legalCombinations6.p']
    for item in comboFiles:
          replaceLetters(item)
          legalwords()
    results.sort()
    results.sort(key = len)
    score()
    finalDisplay()
    
start = timer()
sim1()
end = timer()
seconds = (end-start) % 60
minutes = (end-start-seconds)/60
print('This solution was generated in', round(minutes), 'minutes and', round(seconds), 'seconds.')