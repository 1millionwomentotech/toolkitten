#soc02hw

#Things to Try
# - Calculate a table for each letter in the alphabet from a-z, and count how many times 
# each letter appears in `alice_in_wonderland.txt` (fancy word for counting stuff is 
# "frequency distribution" - because you are counting the frequency of something)

# a: 34,560

# b: 5,027

# ...

# z: 893

# Store the results in a list of lists:

# ```python
# result = [  
#             ["a", 34560], 
#             ["b", 5027], 
#             ... 
#             ["z", 893]
#          ]
# ```

# Hint: use python's lower() method to turn all alphabetic letters into small case and 
# count them (so "A" counts towards "a"). 

# Hint: Ignore non-alphabetic numbers, you can check with python isalpha() method.

import collections
import string

def count_letters(filename, case_sensitive=False):
    with open(filename, 'r') as f:
        text = f.read()

    if case_sensitive:
        alphabet = string.ascii_letters
    else:
        alphabet = string.ascii_lowercase
        text = text.lower()

    letter_count = collections.Counter()
    #collections.Counter is, in essence, a dictionary with all values defaulting to 0
    for char in text:
        if char in alphabet:
            letter_count[char] += 1

    for letter in alphabet:
        print(letter, ':', letter_count[letter])

count_letters('alice_in_wonderland.txt')