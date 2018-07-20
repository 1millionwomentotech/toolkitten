# CIVILIZATION III Map


# Week 1 Hackathon Challenge: Continent Counter
# Task: Calculate the size of a continent you are
# standing on in your 11 x 11 world in Civilization III.

# Bonuses for:

# calculate continent size for all continents in the world
# random world generator
# fastest program
# benchmarking
# extension of the problem to n x n size world

# SOLUTION:


import random
import numpy as np
import collections
from PIL import Image, ImageDraw

# Create a grid of n x n pixels (default is 11 x 11)
noOfrows = int(input("Enter the grid size") or '11')
CanvasSize = 200
tileSize = CanvasSize / noOfrows
image = Image.new(mode='RGB', size=(CanvasSize,
                                    CanvasSize), color=0)
draw = ImageDraw.Draw(image)
x = 0
y = 0

# Randomly generate world
worldGrid = np.random.randint(2, size=(noOfrows,
                                       noOfrows))


# Print the world
for i in worldGrid:
    print(*i)


# Draw the fictional world map
for i in range(noOfrows):
    for j in range(noOfrows):

        if(worldGrid[i, j] == 1):
            gridColor = (0, 128, 0)
        else:
            gridColor = (0, 0, 128)

        draw.rectangle([(x, y), (x + tileSize, y + tileSize)],
                       fill=gridColor,
                       outline=(0, 0, 0))
        y = y + tileSize
    x = x + tileSize
    y = 0

image.save("WorldMap.png")


continents = np.zeros((2, 2))
water = np.zeros((2, 2))


def TraverseContinent(x, y):
    neighbors = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                 (x, y - 1), (x, y + 1), (x + 1, y - 1),
                 (x + 1, y), (x + 1, y + 1)]
    for (i, j) in neighbors:

        if((worldGrid[i, j] == 1) and ((i > -1) and (j > -1))):
            continents.append([i, j])
            print("There is a piece at ", i, j)


# Enter the tile as x y eg. 1 2
ix, iy = input("Enter the tile you want to stand on: ").split(' ')
ix = int(ix)
iy = int(iy)

if(worldGrid[ix, iy] == 1):
    print("You are on land!")
    continents = [[ix, iy]]
    TraverseContinent(ix, iy)

for i in range(1, len(continents) + 1):
    TraverseContinent(continents[i][0], continents[i][1])

finalList = []
[finalList.append(x) for x in continents if x not in finalList]
print("The size of the continent is: ", len(finalList), "tiles")
