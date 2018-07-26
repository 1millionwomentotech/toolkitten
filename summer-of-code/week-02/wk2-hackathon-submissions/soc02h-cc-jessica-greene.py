'''
Boogle game program

Boggle is a 4x4 word game with 16 dice.

https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Boggle.jpg/220px-Boggle.jpg

After the board is shaken, players have 3 minutes to write down all word they see on the board.

https://ecdn.teacherspayteachers.com/thumbitem/Boggle-Boards-Daily-5-056985700-1372905970-1399574131/original-755526-1.jpg

https://ecdn.teacherspayteachers.com/thumbitem/Boggle-Worksheet-3429774-1507487032/original-3429774-1.jpg

Points are given in the following way:

1 and 2 letter words = 0 points 3 letter words = 1 point 4 letter words = 2 points 5 letter words = 3 points

(length of the word above 2)

The longest possible word 16 letter word = 14 points

When you build a word, you can only use one letter once: in other words if you travel along the board and you used a letter, you cannot use it again for the same word, however, you CAN use it for a new word.

You can travel in any direction on the board, diagonal travel is allowed.

The person with the most points win.
'''

import random
from datetime import datetime

class boggle():
    '''
    Class to build boogle board and solve it
	'''
    # board : 4x4 unless specified to a nxn grid when class object called.
    def __init__(self, height = 4, width = 4):
        self.counter = 0
        self.height = height
        self.width = width
        self.X = 0
        self.Y = 0
        self.next = 0
        self.full_match = []
        self.possibly_words = [[[self.X, self.Y]]]
        self.filename = 'sowpods-dictionary.txt'
        self.dictionary = self.generate_dictionary()
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P' , 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.board =  self.generate_board()

    def generate_dictionary(self):
        '''
        Function to generate dictionary.
        Returns:
            Generated dictionary as list.
        '''
        dictionary = []
        with open(self.filename,'r') as f:
            for line in f:
                dictionary.append(line.rstrip('\r\n'))
        return dictionary

    def generate_board(self):
        '''
        Function to generate board.
        Returns:
            Randomily generated board.
        '''
        board = []
        # random generated world
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(self.alphabet[random.randint(0,len(self.alphabet)-1)])
            board.append(row)
        # hard coded board for testing, comment out to use above world generator
        # board = [
        #    ['A', 'S', 'I', 'F'],
        #    ['L', 'B', 'T', 'O'],
        #    ['L', 'O', 'O', 'R'],
        #    ['S', 'E', 'E', 'X']
        #]
        return board

    def check_coords_valid(self, x, y):
        '''
        Function to check given co-ordinates are valid(within board).
        Returns:
            True if co-ordinates are valid.
            False if co-ordinates are invalid.
        '''
        if x >=0 and x < self.height and y >=0 and y < self.width:
            return True
        else:
            return False

    def decode_coords(self, coords):
        '''
        Function to decode coordinates to letters on boggle board.
        Returns:
            string of letters from boggle board
        '''
        word = ""
        for item in coords:
           word = word + self.board[item[0]][item[1]]
        return word.lower()

    def check_for_match(self, word):
        '''
        Function to check if word has a match or possible match in the dictionary.
        Returns:
            Appends to self.full_match if a full match is detected.
            returns candiates if possible match found
        '''
        candidates = []
        for a in self.dictionary:
            if a == word:
                self.full_match.append(a)
            elif a.startswith(word):
                candidates.append(a)
        return candidates


    def check_neighbours(self):
        '''
        Function to check co-ordinates of neighbour tiles and if they are valid and make a word.
        '''
        to_check = self.possibly_words[self.next]
        X = to_check[len(to_check)-1][0]
        Y = to_check[len(to_check)-1][1]
        neighbours = [
            [X-1, Y+1],
            [X-1, Y],
            [X-1, Y-1],
            [X, Y-1],
            [X+1, Y-1],
            [X+1, Y],
            [X+1, Y+1],
            [X, Y+1]
        ]
        for neighbour in neighbours:
            # check co-ordinates are valid
            if self.check_coords_valid(neighbour[0],neighbour[1]):
                # check co-ordinates are not already used in word
                if neighbour not in to_check:
                    word_to_check = self.decode_coords([*to_check, neighbour])
                    if self.check_for_match(word_to_check):
                        self.possibly_words.append([*to_check, neighbour])

    def calculate_score(self, solutions):
        '''
        Points are given in the following way:
        1 and 2 letter words = 0 points 3 letter words = 1 point 4 letter words = 2 points 5 letter words = 3 points
        '''
        score = 0
        for item in solutions:
            if len(item) == 3:
                score += 1
            elif len(item) == 4:
                score += 2
            elif len(item) == 5:
                score += 3
            elif len(item) == 6:
                score += 4
            elif len(item) == 7:
                score += 5
            elif len(item) == 8:
                score += 6
            elif len(item) == 9:
                score += 7
            elif len(item) == 10:
                score += 8
            elif len(item) == 11:
                score += 9
            elif len(item) == 12:
                score += 10
            elif len(item) == 13:
                score += 11
            elif len(item) == 14:
                score += 12
            elif len(item) == 15:
                score += 13
            elif len(item) == 16:
                score += 14
        return score

    def start_checking(self):
        '''
        Function to start checking for words on the board.
        Returns:
            score
        '''
        while self.X < self.height:
            self.Y = 0
            while self.Y < self.width -1:
                self.possibly_words = [[[self.X, self.Y]]]
                self.next = 0
                while self.next < len(self.possibly_words):
                    self.check_neighbours()
                    self.next += 1
                print(self.X, self.Y)
                self.Y += 1
            print(self.X, self.Y)
            self.X += 1

        solutions = set(self.full_match)
        return self.calculate_score(solutions), [ x for x in solutions if len(x) > 2]


def run_game(board_size):
    height, width = board_size
    # set starting time
    start = datetime.now()
    # make board object from class setting grid height and width
    game = boggle(height, width)
    # print board out - for checking
    for row in game.board:
        print(row)
    # start search and return score
    score, solutions = game.start_checking()
    # return duration
    duration = datetime.now() - start
    # Print score and time taked to find results
    print("\nYou scored {} points with {} possible words. It took {} to calculate this.\nPossible words were: \n\n {}".format(score, len(solutions), duration, solutions))
    return result = {
        "score":score,
        "words": solutions
    }

if __name__ == '__main__':
    # Now with 3x3 board
    print("\n4x4 board of boggle:\n")
    run_game((4,4))
    # Now with 3x3 board
    print("\n3x3 board of boggle:\n")
    run_game((3,3))
    # Now with 5x5 board
    print("\n5x5 board of boggle:\n")
    run_game((5,5))


'''
    Hard coded board runs at about 43s, so need to work on memory and timing.
'''