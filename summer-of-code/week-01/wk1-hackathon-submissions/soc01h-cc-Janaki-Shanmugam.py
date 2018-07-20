#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SOC Week 1 Hackathon challenge
"""

from numpy import random
from matplotlib import pyplot as plt

# Generate pre-defined map with one central continent
WorldMap = [[0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,0,0,0,0],
            [0,0,0,1,1,1,1,1,0,0,0],
            [0,0,0,0,1,1,0,1,0,0,0],
            [0,0,0,0,0,1,1,0,0,0,0],
            [0,0,0,0,0,1,1,0,0,0,0],
            [0,0,0,0,1,1,0,1,1,0,0],
            [0,0,1,1,1,1,0,0,1,1,0],
            [0,1,1,1,1,1,1,1,1,0,0],
            [0,0,1,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]]

plt.imshow(WorldMap,cmap = 'BuGn')
plt.show()

#Initialise LandCount variable
LandCount = 0
# Counting continent size
for j in range (0, len(WorldMap)):
    for i in range (0, len(WorldMap)):
        if WorldMap[i][j]==1:
            LandCount += 1
   
print("Size of continent is", LandCount, ".")

"""
Random world map generation
"""
# Specify grid size (m-by-n)
m = 11
n = 11
# Create random world map 
RandMap = [[random.randint(0,2) for j in range(n)] for i in range(m)]
# show map, where 0 is water (white) and 1 is land (green)
plt.imshow(RandMap,cmap = 'BuGn')
plt.show()

"""Counting continent sizes for random world not finished yet!
# grid index - starting from centre land tile (5,5)
x = 5
y = 5
RandMap[5][5] = 2 # initialise land tile at grid (5,5)
# initialise var - for land tiles
LandCount = 1

def LandSearch(x,y):
    global LandCount
    # neighbouring coordinate search 
    if x < m-1 and y < n-1:
        gridsearch_x = [x-1, x, x+1]
        gridsearch_y = [y-1, y, y+1]
        for a in gridsearch_y:
            for b in gridsearch_x:
                if WorldMap[a][b] == 1:
                    LandCount += 1 # add to land tile count
                    WorldMap[a][b] = 2 # to prevent double-counting