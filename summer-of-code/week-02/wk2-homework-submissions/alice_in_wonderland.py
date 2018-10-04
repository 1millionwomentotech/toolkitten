filename = "alice_in_wonderland.txt"

def alice_letter_counter():
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
	freq_list = []
	for i in range(len(alphabet)):
		freq_list.append([alphabet[i] + ': ' + str(raw.count(alphabet[i]))])
	print(freq_list)
	return freq_list

alice_letter_counter()
