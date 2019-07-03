# Hackaton Challange 2
from random import choice
import time
filename = "Dictionary.txt" #Check that the name is tha same, mine might be different
file = open(filename,"r")
raw = file.read()
dictionaryToCompare={}
player_answers = []
keyToAdd = ""
points = 0
#load dictionary
for k in range(len(raw)):
	if raw[k] != raw[2]: #raw[2] is the character that devides my words
		keyToAdd += raw[k]
	else:
		dictionaryToCompare[keyToAdd] = 0
		keyToAdd = ""
		#print(dictionaryToCompare)


#Dices definition

dices = [
			['A','A','E','E','G','N'],
			['E','L','R','T','T','Y'],
			['A','O','O','T','T','W'],
			['A','B','B','J','O','O'],
			['E','H','R','T','V','W'],
			['C','I','M','O','T','U'],
			['D','I','S','T','T','Y'],
			['E','I','O','S','S','T'],
			['D','E','L','R','V','Y'],
			['A','C','H','O','P','S'],
			['H','I','M','N','Q','U'],
			['E','E','I','N','S','U'],
			['E','E','G','H','N','W'],
			['A','F','F','K','P','S'],
			['H','L','N','N','R','Z'],
			['D','E','I','L','R','X']]

# Roll dices
board=[
		[" "," "," "," "],
		[" "," "," "," "],
		[" "," "," "," "],
		[" "," "," "," "]
		]

def rollDices(board):
	choices_dices=[i for i in range(0,16)] #creates an array of numbers until 15
	choices_face =[j for j in range(0,6)]
	for i in range (0,4):
		for j in range(0,4):
			dice_index= choice(choices_dices)
			dice_face = choice(choices_face)
			board[i][j] = dices[dice_index][dice_face]
			choices_dices.remove(dice_index) # this dice was already rolled
			

def print_board(a_board):
	row_toprint = " "
	for i in range(len(a_board)):
		for j in range(len(a_board[1])):
			row_toprint += (a_board[i][j]) + " "
		print (row_toprint)
		row_toprint = " "


rollDices(board)
print_board(board)

time_end = time.time() + (60*3) #Change the time range


while time.time() < time_end:
	new_word = input("Type a word: ")
	player_answers.append(new_word)

def lookForWord(thisWord,this_letter,thisBoard,x,y):
	#print(thisBoard)
	#print(thisWord,this_letter,x,y)
	if (x< len(thisBoard) and y< len(thisBoard)):
		if(x>= 0 and y >= 0):
			if (thisBoard[x][y] != thisWord[this_letter]):
				return False # no estoy segura de esto
		else:
			return False
	else:
		return False
	u = True
	if(this_letter<len(thisWord)-1):
		u =  u and lookForWord(thisWord,this_letter+1,thisBoard, x-1, y-1)
		if (u==False):
			u=True
			u =  u and lookForWord(thisWord,this_letter+1,thisBoard,x, y-1)
		if (u==False):
			u=True
			u =  u and lookForWord(thisWord,this_letter+1,thisBoard,x-1, y)
		if (u==False):
			u=True
			u =  u and lookForWord(thisWord,this_letter+1,thisBoard,x+1, y-1)
		if (u==False):
			u=True
			u =  u and lookForWord(thisWord,this_letter+1,thisBoard,x-1, y+1)
		if (u==False):
			u=True
			u =  u and lookForWord(thisWord,this_letter+1,thisBoard,x+1, y)
		if (u==False):
			u=True
			u =  u and lookForWord(thisWord,this_letter+1,thisBoard,x+1, y+1)
		if (u==False):
			u= True
			u =  u and lookForWord(thisWord,this_letter+1,thisBoard,x, y+1)			
	return u 
	# la cosa es q esto va a botar error cuando este en las esquinas 

def checkWord(aWord,aboard):
	found_word = False
	for i in range(len(aboard)):
		for j in range(len(aboard)):
			if(aboard[i][j] == aWord[0].upper()):
				found_word = lookForWord(aWord.upper(),0,aboard,i,j)	
			if found_word == True:
				return True
	return False

#

for word in range(len(player_answers)):
	if(dictionaryToCompare.get(player_answers[word].upper(),"X") != "X" ):
		if(checkWord(player_answers[word],board) == True):
			if(len(player_answers[word]) == 3):
				points +=1
				print(player_answers[word] + " is correct, you get 1 point for this word")
			elif (len(player_answers[word]) < 3):
				points = points
				print(player_answers[word] + " is correct, you get 0 point for this word")
			elif (len(player_answers[word]) ==4):
				points +=2
				print(player_answers[word] + " is correct, you get 2 point for this word")
			elif (len(player_answers[word]) >= 5):
				points +=3
				print(player_answers[word] + " is correct, you get 3 point for this word")

print ("your score is: " + str(points) + " points.")




