import random
import timeit

### 1MWTT SOC WEEK 2 HACKATHON -- BOGGLE ###

# Boggle is a 4x4 word game with 16 dice.

# https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Boggle.jpg/220px-Boggle.jpg

# After the board is shaken, players have 3 minutes to write down all word they see on the board.

# Points are given in the following way:

# 1 and 2 letter words = 0 points 3 letter words = 1 point 4 letter words = 2 points 5 letter words = 3 points

# (length of the word above 2)

# The longest possible word 16 letter word = 14 points

# When you build a word, you can only use one letter once: in other words if you travel along the board and you used a letter, you cannot use it again for the same word, however, you CAN use it for a new word.

# You can travel in any direction on the board, diagonal travel is allowed.

# The person with the most points win.

# Challenge: write a boggle solver that finds all possible words on a given board. You should pick a fixed vocabulary (dictionary): Hasbro standard English dictionary

# Bonuses:

# fastest algorithm
# choose dictionary
# choose dice distribution
# extend to 3x3 and 5x5
# benchmark
# What is the MOST number of points possible in boggle? That is, what is the holy grail of Boggle with a fixed dictionary?


class BoggleGame():
	"""
	A class for representing and solving the board game Boggle.

	Attributes:
		default_dice (list) -- Default dice configuration for Boggle
		old_dice (list) -- Dice configuration for original Boggle game
		twentyfive_dice (list) -- Dice configuration for 'Big' (5x5) Boggle game
		default_dictionary_path (string) -- Path to file with default wordlist

		size (int) -- Size of each dimension of (square) board
		boggle_words (list) -- List of boggle words that are found in current board
		dictionary (string) -- Path to external dictionary file
		dice (list) -- List of dice configurations
		board (list) -- List of lists with a letter from a rolled die in each place
		t_map (dictionary) -- Mapping of board state information for graph traveral
		wordlist (list) -- flat list of all words from dictionary file
		prefix_tree (dictionary) -- trie for efficient search of wordlist
	"""

	default_dice = [
		['A', 'A', 'E', 'E', 'G', 'N'],
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
		['D', 'E', 'I', 'L', 'R', 'X']
	]

	old_dice = [
		['R', 'I', 'F', 'O', 'B', 'X'],
		['I', 'F', 'E', 'H', 'E', 'Y'],
		['D', 'E', 'N', 'O', 'W', 'S'],
		['U', 'T', 'O', 'K', 'N', 'D'],
		['H', 'M', 'S', 'R', 'A', 'O'],
		['L', 'U', 'P', 'E', 'T', 'S'],
		['A', 'C', 'I', 'T', 'O', 'A'],
		['Y', 'L', 'G', 'K', 'U', 'E'],
		['Q', 'B', 'M', 'J', 'O', 'A'],
		['E', 'H', 'I', 'S', 'P', 'N'],
		['V', 'E', 'T', 'I', 'G', 'N'],
		['B', 'A', 'L', 'I', 'Y', 'T'],
		['E', 'Z', 'A', 'V', 'N', 'D'],
		['R', 'A', 'L', 'E', 'S', 'C'],
		['U', 'W', 'I', 'L', 'R', 'G'],
		['P', 'A', 'C', 'E', 'M', 'D']
	]

	twentyfive_dice = [
		['A', 'A', 'A', 'F', 'R', 'S'],
		['A', 'A', 'E', 'E', 'E', 'E'],
		['A', 'A', 'F', 'I', 'R', 'S'],
		['A', 'D', 'E', 'N', 'N', 'N'],
		['A', 'E', 'E', 'E', 'E', 'M'],
		['A', 'E', 'E', 'G', 'M', 'U'],
		['A', 'E', 'G', 'M', 'N', 'N'],
		['A', 'F', 'I', 'R', 'S', 'Y'],
		['B', 'J', 'K', 'Q', 'X', 'Z'],
		['C', 'C', 'N', 'S', 'T', 'W'],
		['C', 'E', 'I', 'I', 'L', 'T'],
		['C', 'E', 'I', 'L', 'P', 'T'],
		['C', 'E', 'I', 'P', 'S', 'T'],
		['D', 'H', 'H', 'N', 'O', 'T'],
		['D', 'H', 'H', 'L', 'O', 'R'],
		['D', 'H', 'L', 'N', 'O', 'R'],
		['D', 'D', 'L', 'N', 'O', 'R'],
		['E', 'I', 'I', 'I', 'T', 'T'],
		['E', 'M', 'O', 'T', 'T', 'T'],
		['E', 'N', 'S', 'S', 'S', 'U'],
		['F', 'I', 'P', 'R', 'S', 'Y'],
		['G', 'O', 'R', 'R', 'V', 'W'],
		['H', 'I', 'P', 'R', 'R', 'Y'],
		['N', 'O', 'O', 'T', 'U', 'W'],
		['O', 'O', 'O', 'T', 'T', 'U']
	]

	default_dictionary_path = './dictionary.txt'

	def __init__(self, size=4, dictionary='./dictionary.txt', dice_set='default'):
		"""
		Constructor function for Boggle game solver.

		Parameters:
		size (int) -- optional -- default 4: Dimension of one side of the (square) board
		dictionary (string) -- optional -- default './dictionary.txt': Path to wordlist file
		dice_set (string) -- optional -- default 'default': Dice setup to use, or path to 
			custom dice file. Built-in options include 'default', 'old', and 'big'.
		"""
		self.size = size
		self.paths = []
		self.boggle_words = []
		self.dictionary = dictionary
		# Use different dice sets depending on the size of the board and/or user input
		if self.size > 5 and dice_set == 'default':
			self.dice = self.twentyfive_dice
		elif dice_set == 'default':
			self.dice = self.default_dice
		elif dice_set == 'old':
			self.dice = self.old_dice
		elif dice_set == 'big':
			self.dice = self.twentyfive_dice
		else:
			self.dice = self.__import_dice(dice_set)
		self.board = self.__construct_board()
		self.t_map = self.__create_mapping()
		self.wordlist = self.__import_dictionary()
		self.prefix_tree = self.__construct_trie()
	
	def __str__(self):
		"""
		Print a representation of the board layout

		Returns: String showing the current board state.
		"""
		str = ""
		for i in range(self.size):
			str = str + f'{self.board[i]}\n'
		return str

	def __construct_board(self):
		"""
		Construct a board to play boggle

		Returns: List of lists of random die rolls
		"""
		dice = self.dice
		# Accomodate larger boards even if our dice set is limited to 16/25 dice
		while len(dice) < self.size ** 2:
			dice += dice

		random_dice = random.sample(dice, self.size ** 2)
		board = []
		for row in range(self.size):
			board_row = []
			for col in range(self.size):
				die = random_dice.pop()
				board_row.append(random.choice(die))
			board.append(board_row)
		return board

	def __create_mapping(self):
		"""
		Transform the board state into a mapping representing the board in a way that
		makes it easier to search through the graph. Each vertex is indicated in the
		following format:
		0: [1, 5, 6], 'M'

		Returns: Dictionary representing the state of the board
		"""
		transition_map = {}
		nodes = [[x, y] for x in range(self.size) for y in range(self.size)]
		for idx, node in enumerate(nodes):
			neighbor_nodes = self.__detect_neighbors(node[0], node[1])
			neighbor_indices = [n[0] + n[1] * self.size for n in neighbor_nodes]
			if idx in neighbor_indices:
				neighbor_indices.remove(idx)
			transition_map[idx] = [neighbor_indices, self.board[node[1]][node[0]]]
		return(transition_map)

	def __import_dictionary(self):
		"""
		Imports a custom dictionary, if file is indicated, or else the default dictionary.

		Returns: List of words
		"""
		try:
			f = open(self.dictionary, 'r')
		except:
			print('No valid dictionary file found, using default dictionary instead')
			self.dictionary = self.default_dictionary_path
			f = open(self.dictionary, 'r')
		dictionary = f.read().splitlines()
		f.close
		return dictionary

	def __import_dice(self, diceset):
		"""
		Imports a custom set of dice from an external file.

		File should have one line per dice, as follows:
		AAAFRS
		AAEEEE
		AAFIRS
		ADENNN
		AEEEEM
			...etc

		Parameters:
		diceset (string) -- path to an external file containing a custom set of dice

		Returns: Nested list of the faces of each die
		"""
		try:
			f = open(diceset, 'r')
			dice = [list(line.strip()) for line in f.readlines()]
			f.close()
			print(dice)
			return dice
		except:
			print('No valid dice file found, using default dice set instead')
			return self.default_dice

	def __construct_trie(self):
		"""
		Construct a trie, so that we can easily check inclusion of any given word or set of
		words with a given prefix very quickly.

		To learn about tries, I made use of the following tutorial:
		https://tutorialedge.net/compsci/data-structures/getting-started-with-tries-in-python/

		Returns: Dictionary representing the wordlist vocabulary in trie form.
		"""
		trie = {}
		for word in self.wordlist:
			temp_dict = trie
			for letter in word:
				temp_dict = temp_dict.setdefault(letter, {})
			temp_dict['*'] = '*'
		return trie

	def check_match(self, word):
		"""
		Check if a word exists in the wordlist by doing a lookup against the trie.

		Parameters:
		word (string) -- Word to check against the trie

		Returns: Boolean indicating inclusion
		"""
		sub_trie = self.prefix_tree

		for char in word:
			if char in sub_trie:
				sub_trie = sub_trie[char]
			else: 
				return False
		else:
			return True if '*' in sub_trie else False

	def check_partial_match(self, current_word):
		"""
		Check if a word fragment occurs in any word in the wordlist, by doing a lookup
		against the trie. This allows pruning of any branches which cannot result in matches.

		Parameters:
		current_word (string) -- Word fragment to check against the trie.

		Returns: Boolean indicating if there are any words beginning with the given sequence
		"""
		sub_trie = self.prefix_tree
		for char in current_word:
			if char in sub_trie:
				sub_trie = sub_trie[char]
			else:
				return False
		return True

	def search_all_nodes(self):
		"""
		Do a search of all paths starting from each node (die) on the board, and append
		any found words to the boggle_words list.

		Returns: None
		"""
		for node in self.t_map.keys():
			self.search_from_node(node)

	def search_from_node(self, start, path=[], current_word=''):
		"""
		Traverse the graph from a given node using depth first search. For each step
		on the found paths, determine whether the letters from the dice on the path
		represent a word in the vocabulary. If they do, add them to the list.

		Prune if the sequence of letters on the path does not match the beginning
		of any word in the vocabulary.

		Parameters:
		start (int) -- Index of 
		path (list) -- default [] -- List representing the nodes in the current path
		current_word (string) -- default '' -- Sequence created by letters in current path

		Returns: None
		"""
		path = path + [start]
		current_word = current_word + self.t_map[start][1]
		if self.check_match(current_word) and current_word not in self.boggle_words:
			self.boggle_words.append(current_word)
		possible_neighbors = [i for i in self.t_map[start][0] if i not in path]

		# Prune if there are no further matches in the prefix-tree, or we've run out of 
		# possible adjoining dice.
		if not self.check_partial_match(current_word) or len(possible_neighbors) == 0: 
			self.paths.append(path)
		else:
			for i in possible_neighbors:
				self.search_from_node(i, path, current_word)

	def score(self):
		"""
		Calculate the score for the current set of solved boggle words.

		Returns: Score object with the following format:
			result = {
			    "score": 143,
			    "words": [ "" , "", "", "", ... , ""]
			}
		"""
		score = 0
		for word in self.boggle_words:
			score += len(word) - 2
		valid_words = sorted(self.boggle_words)
		return {"score": score, "words": valid_words}

	def get_new_board(self, length=4, dice_set='default'):
		"""
		Create a new board

		Parameters:
		length (int) -- default 4 -- Size of each dimension of (square) board
		dice_set (string) -- default 'default' -- Path to a custom dice set or string
			representing which built-in dice set to use ('default', 'old', 'big')
		"""
		self.size = length
		# Use different dice sets depending on the size of the board and/or user input
		if self.size > 5 and dice_set == 'default':
			self.dice = self.twentyfive_dice
		elif dice_set == 'default':
			self.dice = self.default_dice
		elif dice_set == 'old':
			self.dice = self.old_dice
		elif dice_set == 'big':
			self.dice = self.twentyfive_dice
		else:
			self.dice = self.__import_dice(dice_set)
		self.board = self.__construct_board()
		self.t_map = self.__create_mapping()
		self.boggle_words = []

	def play_boggle_game(self):
		self.search_all_nodes()
		report = self.score()
		return report

	def play_new_game(self, length=4):
		self.get_new_board(length)
		result = self.play_boggle_game()
		return result


	def __detect_neighbors(self, x, y):
		return [[tile_x, tile_y] for tile_x in range(x - 1, x + 2)
                                    for tile_y in range(y - 1, y + 2)
                                    if tile_x >= 0 and tile_y >= 0
                                    and tile_x < self.size and tile_y < self.size]

### RUN 4x4 STANDARD BOGGLE GAMES ###
print("Setting up a 4x4 Boggle game -- one moment please!")
print('-' * 50)
boggle = BoggleGame()
print('\nREADY!\n')
print('-' * 50)
print(boggle)
result = boggle.play_boggle_game()
print(result)
print('\n' + '-' * 50 + '\n')
# result2 = boggle.play_new_game()
# print(result2)


### RUN 5x5 'BIG' BOGGLE SAMPLE GAMES ###
print("\nSetting up a 5x5 Boggle game -- one moment please!")
print('-' * 50)
big_boggle = BoggleGame(size=5)
print('\nREADY!\n')
print('-' * 50)
print(big_boggle)
big_result = big_boggle.play_boggle_game()
print(big_result)
# big_result2 = big_boggle.play_new_game()
# print(big_result2)


### HIGH SCORES ###
def run_games_standard(iterations):
	scores = []
	for i in range(iterations):
		scores.append(boggle.play_new_game()['score'])
	print(max(scores))

def run_games_big(iterations):
	scores = []
	for i in range(iterations):
		scores.append(big_boggle.play_new_game(5)['score'])
	print(max(scores))

# run_games_standard(100000)
# run_games_big(10000)

'''
Best scores on experimental basis:
4x4 -- 1867
5x5 -- 2968 

Optimal board configurations(and thus maximum score) could be achieved by selecting 
letters from the densest branches of the trie.
'''

### BENCHMARKING ###

# standard = timeit.timeit('boggle.play_new_game()', number=1000, globals=globals())
# print(f'Ran 1000 Standard (4x4) games, with average solve time of {standard/1000}')
# big = timeit.timeit('big_boggle.play_new_game(5)', number=1000, globals=globals())
# print(f'Ran 1000 Standard (5x5) games, with average solve time of {big/1000}')

''' Sample benchmark output:
Ran 1000 Standard (4x4) games, with average solve time of 0.01174603958
Ran 1000 Standard (5x5) games, with average solve time of 0.035450393345999996
'''