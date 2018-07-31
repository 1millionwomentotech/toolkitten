#Count letters in a book

import string

alphabet = list(string.ascii_lowercase)
counterAlphabet = [0] * len(alphabet)
dictionary_alice = dict()

filename = "../alice_in_wonderland.txt"
file = open(filename, mode='r', encoding='utf-8-sig')
raw = file.read()	

lengthFile = len(raw)

def counterLetter(positionLetterAlphabet):
	counterAlphabet[positionLetterAlphabet] += 1

def createDictionary(letter, counterValue):
		dictionary_alice[letter] = counterValue[i]

for positionLetterAlicia in range (0, lengthFile - 1):
	letterAlicia = raw[positionLetterAlicia]	
	if letterAlicia in alphabet:
		positionLetterAlphabet = alphabet.index(letterAlicia.lower())
		counterLetter(positionLetterAlphabet)

print('Counter for amount of letter in Alice in Wonderland')

for i in range(0, len(alphabet)):
	dictionary_alice[alphabet[i]] = counterAlphabet[i]

print(dictionary_alice)



print('######')
print('Own dictionary')

dictionary_karen = dict(name='', surname='', favourite_color='')
dictionary_karen['name'] = 'Karen'
dictionary_karen['surname'] = 'Alonso'
dictionary_karen['favourite_color'] = 'Blue'

print(dictionary_karen)
dictionary_karen['favourite_color']='Red'
print(dictionary_karen)

