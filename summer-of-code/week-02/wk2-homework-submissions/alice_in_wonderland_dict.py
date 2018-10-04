#Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

filename = "alice_in_wonderland.txt"

def alice_letter_counter_dict():
	with open(filename) as file:
		raw = file.read()
		raw = raw.lower()
		text = []
		for n in range(len(raw)):
			if raw[n].isalpha():
				text.append(raw[n])
		jointtext = ('').join(text)


	freq = 0
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	alice_dict = {}
	for i in range(len(alphabet)):
		alice_dict[alphabet[i]] =  str(raw.count(alphabet[i]))
	print(alice_dict)
	return alice_dict

alice_letter_counter_dict()