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

class boggle():  
    '''
    Class to build boogle board and solve it
	'''
    # board : 4x4 unless specified to a nxn grid when class object called.
    def __init__(self, height = 4, width = 4):
        self.counter = 0
        self.height = height
        self.width = width
        self.words = []
        self.filename = 'sowpods-dictionary.txt'
        self.dictionary = self.generate_dictionary()
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P' , 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.board =  self.generate_board()
   

    def generate_dictionary(self):
        dictionary = []
        with open(self.filename,'r') as f:
            for line in f:
                dictionary.append(line)
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
        board = [
            ['A', 'S', 'I', 'F'],
            ['L', 'B', 'T', 'O'],
            ['L', 'O', 'O', 'R'],
            ['S', 'E', 'E', 'X']
        ]
        return board

    def check_valid_coords(self):
        pass
    
    def check_for_match(self):
        pass
    
    def check_neighbours(self):
        pass
        
    def start_checking(self):
        pass
        
if __name__ == '__main__':
    # make board object from class setting grid height and width
    game = boggle()
    # print board out - for checking
    for row in game.board:
        print(row)
    # print length of dictionary
    print(len(game.dictionary))