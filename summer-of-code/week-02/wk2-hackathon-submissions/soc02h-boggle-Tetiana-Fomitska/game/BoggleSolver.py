from game.SpellChecker import SpellChecker
import configparser
import string
import random as r


config = configparser.ConfigParser()
config.read('config.properties')


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()

def shake_board():
    length = int(config.get('Board', 'length'))
    width = int(config.get('Board', 'width'))
    board = [[r.choice(string.ascii_uppercase) for x in range(width)] for y in range(length)]
    print_board(board)


# def get_all_valid_words(board):


# def score_of(word):


shake_board()

dictionary_file_name = config.get('Dictionary', 'file')
spell_checker = SpellChecker('dictionary/' + dictionary_file_name)






