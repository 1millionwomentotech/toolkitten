# Boggle is a 4x4 word game with 16 dice.
# 1 and 2 letter words = 0 points 3 letter words = 1 point 4 letter words = 2 points 5 letter words = 3 points
# (length of the word above 2)
# The longest possible word 16 letter word = 14 points
# Challenge: write a boggle solver that finds all possible words on a given board. 
# You should pick a fixed vocabulary (dictionary): Hasbro standard English dictionary

import random
import copy
import datetime

print("===== start of program =====")
start_time = datetime.datetime.now()

size = 4
point = 0
character = ''
result = {"score":0,"words":[]}

dice = ['AAEEGN',
   'ELRTTY',
   'AOOTTW',
   'ABBJOO',
   'EHRTVW',
   'CIMOTU',
   'DISTTY',
   'EIOSST',
   'DELRVY',
   'ACHOPS',
   'HIMNQU',
   'EEINSU',
   'EEGHNW',
   'AFFKPS',
   'HLNNRZ',
   'DEILRX']
	
# initialize n * n rondom character
for i in range(size*size):
	character = character + random.choice(dice[i])

# for testing purpose
# character ='NTOAWUYEESNUWFLR'  7150 Punkte
print(character)

# read standard english dictionary 
# 10k words : https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt
f_wordlist = open("soc02h_wordlist2.txt","r")
wordlist = f_wordlist.readlines()

# match character and dictionary(wordlist)
for word in wordlist:
	temp_char = copy.deepcopy(character)
	word = word.replace('\n','')
	match = 0
	for a in word:
		for i in range(size*size):
			if a in temp_char:
				match +=1
				temp_char = temp_char.replace(a,'',1)
				if(len(word)==match):
					if(len(word)<=2):
						added = 0
					else:
						added = len(word)-2
					result["score"] += added
					result["words"].append(word)
				break
		else:
			break
	continue
# File close
f_wordlist.close()

end_time = datetime.datetime.now()
duration = end_time - start_time
print("===== result =====")
print(result)
print("duration : "+ str(duration))





