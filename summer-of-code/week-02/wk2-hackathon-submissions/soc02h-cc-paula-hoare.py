# 1mwtt Summer of Code Week 2 Hackathon
# Author: Paula Hoare
import random
import urllib.request

# ---------------------------------------------------
# Setup the word list
# ---------------------------------------------------

# Select the word list URL
word_ref_url_sowpods = 'https://www.wordgamedictionary.com/sowpods/download/sowpods.txt'
word_ref_url_default = 'https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt'
print('Please select your dictionary.\nOPTIONS:')
print(' - Press Enter for default.')
print(' - Enter "sowpods" for SOWPODS word list')
print(' - Or enter a URL')
word_ref_url = input('')
word_ref = ''
if len(word_ref_url) == 0 :
    word_ref_url = word_ref_url_default
elif word_ref_url.lower() == 'sowpods' :
    word_ref_url = word_ref_url_sowpods

print('...Using word list at '+word_ref_url_default)

# Load the word list
try :
    url_resp = urllib.request.urlopen(word_ref_url)
except :
    print('Fatal Error: Unable to load the word list at '+word_ref_url)
    exit()
print('URL located')
print('Reading the word list, please wait...')
try :
    word_ref = url_resp.read()
except :
    print('Fatal Error: unable to read the word list')
    exit()

# read the list until you come to 'aa' or 'AA'
# only search the first 500 characters so we can exit quickly if it is not there
word_ref_lower = True

word_ref_start_pos = word_ref.find(b'aa\n',0,500)
if (word_ref_start_pos == -1) :
    # Unable to find 'aa'
    # - Look for uppercase 'AA'
    word_ref_start_pos = word_ref.find(b'AA\n',0,500)
    word_ref_lower = False

if word_ref_start_pos > 0 :
    # check that we don't just have the end of a word
    previous_letter = word_ref[word_ref_start_pos-1:word_ref_start_pos]
    if previous_letter != b'\n' :
        word_ref_start_pos = -1

if (word_ref_start_pos == -1) :
    # Unable to find start of word list
    print('Fatal Error: Unable to locate start of words (starting with the word "aa" or "AA")')
    exit()

# ensure that the list starts and ends with \n
# because we check for a complete word by looking for \nword\n
# and the start of a word by looking for \nword
if word_ref_start_pos == 0 :
    # word list starts without a new line
    if word_ref.endswith(b'\n') :
        word_ref = b'\n'+word_ref
    else :
        word_ref = b'\n'+word_ref+b'\n'
elif not word_ref.endswith(b'\n') :
    word_ref = word_ref+b'\n'

print('Done!\n\nReady to play!\n')

# ---------------------------------------------------
# Functions
# ---------------------------------------------------

# Function: is this the start of a word?
def is_start_word(word, new_words) :
    global word_ref, word_ref_start_pos

    if len(word) == 1 :
        return True

    start_word = '\n'+word
    pos = word_ref.find(start_word.encode(), word_ref_start_pos)
    if pos >= 0 :
        # this is the start of a word
        # check is it also a complete word?
        end_pos = pos + len(start_word)
        next_char = word_ref[end_pos:end_pos+1]
        if next_char == b'\n' :
            # complete word - append to our list of new words
            new_words.append(word)
        return True

    return False

# Function: check_word
# builds/tests words
def check_word(dice, letter_pos, new_words, working_word, used_coords) :
    global word_ref_lower

    # check that we have not already used this coordiate in our word
    if letter_pos in used_coords :
        return False
    # build the next word
    next_letter = dice[letter_pos[0]][letter_pos[1]]
    if word_ref_lower :
        next_letter = next_letter.lower()
    word = working_word + next_letter
    # check if this would be the start of a new word (or a complete word)
    if is_start_word(word, new_words) :
        # this could be the start of a word
        # set up our new working word (our word in progress)
        working_word = word
        # add these coordiinates to our used coordinates list
        used_coords.append(letter_pos)
        # circle this letter
        circle_letter(dice, letter_pos, new_words, working_word, used_coords)
        # return true
        return True
    return False

# function: circle_letter
# checks for words by circling around the letters surrounding the current letter
def circle_letter(dice, letter_pos, new_words, working_word, used_coords) :
    x, y = letter_pos
    board_size = len(dice)
    # row above
    if x > 0 :
        if y > 0 :
            check_word(dice, (x-1,y-1), new_words, working_word, used_coords)
        check_word(dice, (x-1, y), new_words, working_word, used_coords)
        if y < board_size-1 :
            check_word(dice, (x-1,y+1), new_words, working_word, used_coords)
    # same row
    if y > 0 :
        check_word(dice, (x,y-1), new_words, working_word, used_coords)
    if y < board_size-1 :
        check_word(dice, (x,y+1), new_words, working_word, used_coords)
    # next row
    if x < board_size-1 :
        if y > 0 :
            check_word(dice, (x+1,y-1), new_words, working_word, used_coords)
        check_word(dice, (x+1, y), new_words, working_word, used_coords)
        if y < board_size-1 :
            check_word(dice, (x+1,y+1), new_words, working_word, used_coords)
    # we have come to the end
    # - remove last character from working word
    working_word = working_word[:-1]
    # - remove last coordinates
    used_coords.pop()

# function: find words starting at the specified position
def find_words(dice,start_pos) :
    global word_ref_lower

    new_words = list()

    start_letter = dice[start_pos[0]][start_pos[1]]
    if word_ref_lower :
        start_letter = start_letter.lower()

    # create our working_word string which will be built up to create words
    working_word = start_letter

    # create our used coordinates list
    # - each die position can be used only once in the working word
    used_coords = list()
    used_coords.append(start_pos)

    # keep circling round the letters
    while len(used_coords) > 0 :
        circle_letter(dice, start_pos, new_words, working_word, used_coords)

    return new_words

# ---------------------------------------------------
# Classes
# ---------------------------------------------------
class BoggleResult:
    score = 0
    words = None

    def __init__(self) :
        self.words = list()

    def add_word(self,word) :
        if len(word) > 2 :
            self.score += len(word)-2
        self.words.append(word)

    def print_results(self) :
        print('Score: ',self.score)
        print('Number of words: ',len(self.words))
        print('Words:', self.words)

    def get_results(self) :
        return {'score':self.score, 'words': self.words}

# ---------------------------------------------------
# Play the game
# ---------------------------------------------------

# chose board size
board_size = 4
print('Please select your board size')
print('OPTIONS:')
print(' - Enter 3 for 3x3, 4 for 4x4 or 5 for 5x5')
print(' - Or press Enter for default (4x4)')
board_size_inp = input()
try :
    board_size = int(board_size_inp)
except:
    board_size = 4

if board_size not in [3,4,5] :
    board_size = 4

# create the 4x4 Boogle dice -  16 dice each with 6 letters
dice = [['A','A','E','E','G','N']
       ,['E','L','R','T','T','Y']
       ,['A','O','O','T','T','W']
       ,['A','B','B','J','O','O']
       ,['E','H','R','T','V','W']
       ,['C','I','M','O','T','U']
       ,['D','I','S','T','T','Y']
       ,['E','I','O','S','S','T']
       ,['D','E','L','R','V','Y']
       ,['A','C','H','O','P','S']
       ,['H','I','M','N','Q','U']
       ,['E','E','I','N','S','U']
       ,['E','E','G','H','N','W']
       ,['A','F','F','K','P','S']
       ,['H','L','N','N','R','Z']
       ,['D','E','I','L','R','X']
       ]

# adjust the number of dice according to the board size
if board_size == 5:
    #  we need at least 25 dice in total
    dice = dice * 2

# roll the dice to create the board
board = list()
used_dice = list()
i = 0   # counter for dice
x = 0   # column counter for board
y = 0   # row counter for board
while i < board_size**2 :
    # pick a die to put in our current position
    die_num = random.randint(0,len(dice)-1)
    this_die = dice.pop(die_num)
    used_dice.append(this_die)
    # pick a letter from the die
    letter = this_die[random.randint(0,5)]
    # add it to the board
    if (x==0) :
        # add a new row to the board
        board.append(list())
    board[y].append(letter)
    x += 1
    if (x == board_size) :
        # we are at the end of a row - reset rows and cols
        x = 0
        y += 1
    i += 1

# print out our board
print('Here is our ',board_size,'x',board_size,' Boggle board ')
x = 0
while x < board_size :
    print(board[x])
    x += 1

# find words in our board
print('Finding words, please wait...')
words = list()
# loop through each starting letter on the board
x = 0
while x < board_size :
    y = 0
    while y < board_size :
        # find the words starting at this letter
        new_words = find_words(board,(x,y))
        if (len(new_words)) :
            words += new_words
        y += 1
    x += 1

# output results
game_results = BoggleResult()
if len(words) :
    # sort words in alphabetical order
    words.sort()
    # print out the words, removing duplicates and calculating the score
    last_word = ''
    for word in words :
        if word != last_word :
            game_results.add_word(word)
            last_word = word

print('\nRESULTS:')
game_results.print_results()
print('--- Game Complete ---\nReturning results as a python dictionary...\n\n')

exit(game_results.get_results())
