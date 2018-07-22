### Week 1 Hackathon Challenge: Continent Counter

import random

'''
Task: Calculate the size of a continent you are standing on in your 11 x 11 world 
in Civilization III.

Bonuses for:
- calculate continent size for all continents in the world
- random world generator
- fastest program
- benchmarking
- extension of the problem to n x n size world
'''


world = []

for i in range(0, 11):
    continent = []
    world.append(continent)
    for i in range(0, 11):
        random_num = random.randint(0, 1)
        continent.append(random_num)

for i in world:
    print(i)



