# to count the number of each letters in the file alice_in_wonderland
import collections
file = open("alice_in_wonderland.txt", "r", encoding = "utf8")
counts = dict()
for line in file:
	line = line.rstrip() # to remove the rightmost new line
	for letter in line:
		if letter.isalpha() and letter.islower(): # to find frequency of only lower case letters
			if letter not in counts:
				counts[letter] = 1
			else:
				counts[letter] += 1
	# for letter in line:  # shorthand way 
	# 	if letter.isalpha():
	# 		counts[letter] = counts.get(letter,0) + 1

# To show te result in alphabetical order by key
new_count = collections.OrderedDict(sorted(counts.items()))
for k, v in new_count.items():
	print(k," : ", v)