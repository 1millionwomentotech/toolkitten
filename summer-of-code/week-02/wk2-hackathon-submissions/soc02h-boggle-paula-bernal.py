
import random


filename = 'dictionary.txt'

file = open('dictionary.txt', 'r')


words = []

for word in file:
	if len(word) > 2:
		words.append(word[:-1])


board = []
		
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


for x in range(0,4):
	row = []
	for y in range(0,4):
		pos = random.randint(0,25)
		letter = alphabet[pos].upper()
		row.append(letter)

	board.append(row)

for row in board:
	print(row)

results = []

def addLetter(x,y,w):
	if(x > 0 and x < 4 and y > 0 and y < 4):
		newWord = w + board[x][y]
		if w in words:
			if not w in results and len(w) > 2:
				results.append(w)
		if any(word.startswith(newWord) for word in words):
			addLetter(x-1,y,newWord)
			addLetter(x-1,y-1,newWord)
			addLetter(x-1,y+1,newWord)
			addLetter(x,y-1,newWord)
			addLetter(x,y+1,newWord)
			addLetter(x+1,y,newWord)
			addLetter(x+1,y-1,newWord)
			addLetter(x+1,y+1,newWord)

for x in range(0,4):
	for y in range(0,4):
		s = ""
		addLetter(x,y,s)


print(results)




	





