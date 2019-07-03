import random
import string

dictionary = {}
with open("dictionary.txt", "r") as d:
    for line in d:
        dictionary[line[:-1]] = 1


def make_board(size):
    return [[random.choice(string.ascii_uppercase) for i in range(size)] for j in range(size)]


size = 0
while True:
    size = input("what size the board should be? ")
    print(int(size))
    if int(size) != 3 and int(size) != 4 and int(size) != 5:
        print("Wrong size, you can only enter 3, 4 or 5")
    else:
        break

board = make_board(int(size))
for i in board:
    print(i)

helper_array = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]


def dfs_search(board, i, j, visited, dictionary, word, words):
    visited[i][j] = True
    word = word + board[i][j]
    if word in dictionary:  # I'm looking for all the words, even when the lenght is smaller then 3
        words[word] = 1
    for v in helper_array:
        m = i + v[0]
        n = j + v[1]
        if (m >= 0) and (m < len(board)) and (n >= 0) and (n < len(board)):
            if not visited[m][n]:
                dfs_search(board, m, n, visited, dictionary, word, words)
    visited[i][j] = False


def search_all_the_words(board):
    words = {}
    for i in range(len(board)):
        for j in range(len(board)):
            dfs_search(board, i, j, [[False for k in range(len(board))] for l in range(len(board))], dictionary, "",
                       words)
    words_list = list(words)
    print(list(words))
    points = 0
    for w in words_list:
        if (len(w) >= 3):
            points = points + len(w) - 2
    result = {"score": points, "words": words_list}
    print(result)
    return result


search_all_the_words(board)
