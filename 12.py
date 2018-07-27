import random

def loadwords ():
    print ("Loading word list from file.. ")
    wordList = []
    inFile = open ('dictionary.txt','r')
    for line in inFile:
        wordList.append(line.strip().lower())
    #inFile : locates file in the folder, opens it
    #wordlist: list of the words (strings)
    print(len(wordList), "words loaded")
    inFile.close()
    return wordList

def spellCheck (word, wordList):
    if (word in wordList) == True:
        return True
    else:
        return False

def drawBoard (randomLetters):

    '''Takes a randomList of 16 characters
    Prints out a 4 x 4 grid'''

    print (" %s %s %s %s " %(randomLetters [0], randomLetters [1], randomLetters [2], randomLetters [3]))
    print (" %s %s %s %s " %(randomLetters [4], randomLetters [5], randomLetters [6], randomLetters [7]))
    print (" %s %s %s %s " %(randomLetters [8], randomLetters [9], randomLetters [10], randomLetters [11]))
    print (" %s %s %s %s " %(randomLetters [12], randomLetters [13], randomLetters [14], randomLetters [15]))

def wordinput ():
    #asks user to input the longest word they can from grid
    wordinput = raw_input ("Enter a word made up of the letters in the 4x4 table")
    for letters in wordinput:
        letters == randomLetters

def randomLetters ():
    letters = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
    for i in range (0,16,1):
        letters.append(random.choice(alphabet))
    return letters

dictionary = loadwords()
letterList = randomLetters()
drawBoard(letterList)
wordinput(randomLetters)

def wordinput ():
    #asks user to input the longest word they can from grid
    wordinput = raw_input ("Enter a word made up of the letters in the 4x4 table")
    for letters in wordinput:
        letters == randomLetters
    scoreWord(wordInput)

def scoreWord(word):
    #finds the amount of characters in the word
    wordLength = len(word)
    #multiplies the maunt of letters in the word by two to get the score
    #(not sure how boggle scoring works)
    score = wordLength * 2
