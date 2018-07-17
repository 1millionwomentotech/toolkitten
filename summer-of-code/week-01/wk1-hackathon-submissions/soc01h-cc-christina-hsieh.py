import random

# define size of world
size = 5 # might use user input in future

# generate world using list comprehension
world = [[random.randint(0,1) for x in range(size)] for x in range(size)]