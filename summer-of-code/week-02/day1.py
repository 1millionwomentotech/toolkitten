# Make a function that returns n number of 'moo's

# Functions, parameters
def moo(n):
  #print('moo' * n)
  return 'moo' * n

# moo(0)
# moo(1)
# moo(2)

# for i in range(3):
#   moo(i)

def ask_recursively(question):
  print(question)
  reply = input('> ').lower()
  if reply == 'yes':
    return True
  elif reply == 'no':
    return False
  else:
    print('Please answer "yes" or "no".')
    ask_recursively(question)

ask_recursively('Do you wet the bed?')



# Testing see test_day1.py


# Reading and writing files

filename = "alice_in_wonderland.txt"
file = open(filename, "r",encoding="utf8")

# for line in file:
#   print(line)

raw = file.read()
print('from zero to sixty-five: ' + raw[:65])

print('AGAIN: ' + raw[0:65])

print('the length of Alice in Wonderland in this text file is: ' + str(len(raw)) )

# #163817

print(raw[163000:])

# Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in Alice in Wonderland (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)
# a: 34,560
# b: 5,027
# ...
# z: 893



