def frequency_distribution():
	file = open('alice_in_wonderland.txt',"r",encoding="utf8")
	frequency_distribution = [['a', 0],['b', 0],['c', 0],['d', 0],['e', 0],
							  ['f', 0],['g', 0],['h', 0],['i', 0],['j', 0],
							  ['k', 0],['l', 0],['m', 0],['n', 0],['o', 0],
							  ['p', 0],['q', 0],['r', 0],['s', 0],['t', 0],
							  ['u', 0],['v', 0],['w', 0],['x', 0],['y', 0],
							  ['z', 0]]

	for line in file:
		for c in line:
			if c.isalpha():
				c = c.lower()
				for alphabet in frequency_distribution:
					if c == alphabet[0]:
						alphabet[1] += 1

	return frequency_distribution

print(frequency_distribution())


