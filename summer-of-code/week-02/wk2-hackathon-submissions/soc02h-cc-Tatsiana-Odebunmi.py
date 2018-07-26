import numpy as np
import math
import random
import time

def open_dictinary(dictinary):
	english_dict_path="english_sowpods.txt"
	american_dict_path="american_sowpods.txt"
	path=''
	words_list=[]
	new_word_list=[]
	if dictinary==1:
		path=english_dict_path
	else:
		path=american_dict_path
	try:
		with open(path,encoding = 'utf-8') as f:
			words_list=f.readlines()
		for word in words_list:
			new_word_list.append(word.replace('\n','').upper())
		
	except FileNotFoundError:
		print("ERROR!!! Dictinary not found! Please check ")
	return new_word_list
def dice_and_board(board_size):
	board=np.array(range(board_size*board_size), dtype='str').reshape(board_size,board_size)
	dices=[]
	dices_small=[["L","G","J","I","H","X"],["D","Y","E","B","O","A"],["C","P","E","A","Y","K"],
	["I","N","L","K","P","W"],["U","T","S","W","Y","A"],["O","O","Q","E","H","N"],["O","P","R","M","L","T"],
	["E","G","R","Z","S","R"],["A","B","F","E","C","D"]]
	dices_classic_new=[["A","A","E","E","G","N"],["E","L","R","T","T","Y"],["A","O","O","T","T","W"],
	["A","B","B","J","O","O"],["E","H","R","T","V","W"],["C","I","M","O","T","U"],
	["D","I","S","T","T","Y"],["E","I","O","S","S","T"],["D","E","L","R","V","Y"],
	["A","C","H","O","P","S"],["H","I","M","N","Q","U"],["E","E","I","N","S","U"],
	["E","E","G","H","N","W"],["A","F","F","K","P","S"],["H","L","N","N","R","Z"],
	["D","E","I","L","R","X"]]
	dices_classic_old=[["A","A","C","I","O","T"],["A","H","M","O","R","S"],["E","G","K","L","U","Y"],
	["A","B","I","L","T","Y"],["A","C","D","E","M","P"],["E","G","I","N","T","V"],
	["G","I","L","R","U","W"],["E","L","P","S","T","U"],["D","E","N","O","S","W"],
	["A","C","E","L","R","S"],["A","B","J","M","O","Q"],["E","E","F","H","I","Y"],
	["E","H","I","N","P","S"],["D","K","N","O","T","U"],["A","D","E","N","V","Z"],
	["B","I","F","O","R","X"]]
	dicese_big=[["B","J","K","Q","X","Z"],["O","O","O","T","T","U"],["G","O","R","R","V","W"],
	["A","A","A","F","R","S"],["A","E","E","G","M","U"],["D","H","H","L","O","R"],
	["D","H","H","N","O","T"],["D","H","L","N","O","R"],["A","A","F","I","R","S"],
	["A","F","I","R","S","Y"],["C","E","I","L","P","T"],["E","N","S","S","S","U"],
	["H","I","P","R","R","Y"],["D","D","L","N","O","R"],["C","C","N","S","T","W"],
	["E","M","O","T","T","T"],["C","E","I","P","S","T"],["A","D","E","N","N","N"],
	["A","E","G","M","N","N"],["N","O","O","T","U","W"],["A","A","E","E","E","E"],
	["F","I","P","R","S","Y"],["A","E","E","E","E","M"],["E","I","I","I","T","T"],
	["C","E","I","I","L","T"]]

	if board_size==4:
		while True:
			try:
				print("\nChoose the dice distribution:\n1.New version\n2.Old version")
				choice=int(input(">"))
			except ValueError:
				print("\nWrong input!!!Please, input 1 or 2")
			if choice==1 :
				dices=dices_classic_new
				break
			elif choice==2 :
				dices=dices_classic_old
				break
			else:
				print("\nWrong input!!!Please, input 1 or 2")
	elif board_size==3:
		dices=dices_small
	elif board_size==5:
		dices=dicese_big
	board_time_start=time.time()
	num=0
	for x in range(0,(board_size)):
		for y in range(0,(board_size)):
			if num>=board_size*board_size:
				break
			a=random.randint(0,5)
			board[x][y]=dices[num][a]
			num+=1
	board_time=time.time()-board_time_start
	return board, board_time
# looking for words on the board the board an
def find_words(letters_list,dictinary):
	# looking for possible words which contain just letters from the board
	possible_words=[]
	for word in dictinary:
		check=0
		for letter in word: # for each letter on the board checking if the words from the dictinary have it
			count_letters=letters_list.count(letter)
			if count_letters==0:
				break
			count_word=word.count(letter)

			if count_word>count_letters:
				break
			check+=1
		if check==len(word):
			possible_words.append(word)
	possible_words.remove('')
	return possible_words
# def count_points(matched_words):
# 	return score
#  Checking if the letter on the board already part ofthe word
# #Method to check is the word on the board
def word_checker(size,word,board,x,y,letter_number,checked):

	if letter_number==len(word):
		return 1
	if x==size or y==size:
		return 0
	if x < 0 or y < 0:
		return 0
	# print("size=%s, x=%s, y=%s, word=%s, letter_number=%s" %(size,x,y,word,letter_number))
	if board[x][y]==word[letter_number]:
		if checked.count([x,y])>0:
			return 0
		checked.append([x,y])
		ret_word= word_checker(size,word,board,x,(y+1),(letter_number+1),checked)
		if ret_word==1:
			return 1
		ret_word= word_checker(size,word,board,(x+1),(y+1),(letter_number+1),checked)
		if ret_word==1:
			return 1
		ret_word= word_checker(size,word,board,(x-1),(y+1),(letter_number+1),checked)
		if ret_word==1:
			return 1
		ret_word= word_checker(size,word,board,x,(y-1),(letter_number+1),checked)
		if ret_word==1:
			return 1
		ret_word= word_checker(size,word,board,(x+1),(y-1),(letter_number+1),checked)
		if ret_word==1:
			return 1
		ret_word= word_checker(size,word,board,(x-1),(y-1),(letter_number+1),checked)
		if ret_word==1:
			return 1
		ret_word= word_checker(size,word,board,(x+1),y,(letter_number+1),checked)
		if ret_word==1:
			return 1
		ret_word= word_checker(size,word,board,(x-1),y,(letter_number+1),checked)
		if ret_word==1:
			return 1
		return 0
	else:
		if letter_number==0:
			ret_word=word_checker(size,word,board,x,(y+1),letter_number,checked)
			if ret_word==1:
				return 1
			else:
				if (x+1)<size:
					ret_word=word_checker(size,word,board,(x+1),0,letter_number, checked)
					if ret_word==1:
						return 1
				return 0
		else:
			return 0
# Function to count scores
def score_counter(words_list, size):
	score=0

	for word in words_list:
		lenght=len(word)
		if lenght==2 and size==3:
			score+=1
		if lenght==3:
			if size==3:
				score+=2
			elif size==4:
				score+=1
		if lenght==4:
			if size==3:
				score+=3
			else:
				score+=1
		if lenght==5:
			if size==3:
				score+=5
			else:
				score+=2
		if lenght==6:
			if size==3:
				score+=7
			else:
				score+=3
		if lenght==7:
			if size==3:
				score+=11
			else:
				score+=5
		if lenght>=8 and lenght<16:
			score+=11
		if lenght>=16:
			score+=14
	return score
def main():
	start_time=time.time()
	size=0
	while True:
		try:
			print("\nChose the board:\n1.3x3\n2.4x4\n3.5x5 ")
			size=int(input(">"))
			if size>=1 and size<=3:
				break
			else:
				print("\nPlease, input number from 1 to 3")
		except ValueError:
			print("\nWrong input!!!Please, input number from 1 to 3")
	while True:
		try:
			print("\nChose the dictinary:\n1.English\n2.American\n ")
			dictinary=int(input(">"))
			if dictinary==1 or dictinary==2:
				break
			else:
				print("\nPlease, input 1 or 2")
		except ValueError:
			print("\nWrong input!!! Please, input 1 or 2")
	letters_list=[]
	size+=2
	# Creating the board
	board, board_time=dice_and_board(size)
	# printing letteres in the board view
	print("\nBOARD:\n")
	for x in range(size):
		for y in range(size):
			letters_list.append(board[x][y])
			print(" "+board[x][y], end="")
		print()
	dict_time=time.time()
	words_list=open_dictinary(dictinary) # upload dictinary
	search_time=time.time()
	possible_words=find_words(letters_list,words_list)# list of words containing just letters frm the board
	search_finish_time=time.time()
	matched_words=[]
	full_check_time=0
	for word in possible_words: # checking every words on the bord if its matching
		check_time=time.time()
		match=word_checker(size,word,board,0,0,0,[])
		check_finish_time=time.time()
		if match==1:
			matched_words.append(word)
		full_check_time=full_check_time+(check_finish_time-check_time)
	score_time=time.time()
	#Counting score and store the result in the dictinary
	result={"score": score_counter(matched_words, size),"words": matched_words} 
	finish_time=time.time()
	print("\nResult = "+str(result))
	print()
	print("-"*70)
	print("\nBENCHMARKING\n")
	print("---Creation board and dice distribution : " +str(round(board_time,6)))
	print("---Uploading dictinary: "+ str(round(search_time-dict_time,6)))
	print("---Search for possible matching words: " + str(round((search_finish_time-search_time),6)))
	print("---Average time for one word checking: " + str(round((full_check_time/len(possible_words)),6)))
	print("---Total words were checked: "+ str(len(possible_words)))
	print("---Time for all possible words checking: "+ str(round(full_check_time,6)))
	print("---Time to count the score: " + str(round((finish_time-score_time),6)))
	print("---Time from the start of programm: "+ str(round((finish_time-start_time),6)))
	return

main()
