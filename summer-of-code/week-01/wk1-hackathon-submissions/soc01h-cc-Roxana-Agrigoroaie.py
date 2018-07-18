#!/usr/bin/env python
"""This is a code for the week 1 hackaton of Summer of Code."""

# v0.1 18/07/2018
# author: Roxana Agrigoroaie

# Task:
"""
Calculate the size of a continent you are standing on in your 11x11 world in 
Civilization III.
Bonus for:
- calculate continent size for all continents in the world
- random world generator
- fastest program
- benchmarking
- extension of the problem to n x n size world
"""

# Solution:
# First of all we need to create our world. We can create it 
# either in a random way or by predefining it. 
# 1 stands for land and 0 stands for water

#import statements
import random

#### variable declarations
# the size of the world
world_size = 11 
# a dictionary containing the size of each continent
continentAreas = {} 
# number of continents
continents = 0 
# declare a matrix for the visited locations
visited = [[False for i in range(world_size)] for j in range(world_size)]
#coordinates of the 8 neighbours
nb_x = [-1, -1, -1,  0, 0,  1, 1, 1];
nb_y = [-1,  0,  1, -1, 1, -1, 0, 1];

#### function definitions

def generateWorld(var_size):
  """Function to randomly generate the world."""
  return [[int(round(random.random())) for x in range(var_size)] for y in range(var_size)] 


def coordinateExist(coordX, coordY):
  """Function that checks if a coordinate can be visited.
  
  Takes as input parameters a set of coordinates 
  And checks if the coordinate has been visited and if it is a land.
  """

  return (
    coordX >= 0 and coordX < world_size and 
    coordY >= 0 and coordY < world_size and
    visited[coordX][coordY] == False and
    world[coordX][coordY] 
    )

def searchNeighbours(x, y, continentID):
  """Function to search all 8 neighbours of a given coordinate."""
  visited[x][y] = True
  if(continentAreas[continentID] == None):
    continentAreas[continentID] = 1
  else:
    continentAreas[continentID] += 1

  for i in range(len(nb_x)):
    newX = x+nb_x[i]
    newY = y+nb_y[i]
    if(coordinateExist(newX, newY)):
      return searchNeighbours(newX, newY, continentID)


def travelWorld():
  """Function to search the Civilizations III world."""
  global continents;
  continentAreas[continents] = None
  for i in range(world_size):
    for j in range(world_size):
      if(visited[i][j] == False and world[i][j] == 1):
        searchNeighbours(i, j, continents)
        continents += 1 
        continentAreas[continents] = None
        
# we generate the world
world = generateWorld(world_size)
# we travel the world
travelWorld()


# Print the results
print 'This is our CIVILIZATIONS III WORLD:'
print "==================================================="
for i in range(world_size):
  print world[i][:]
print "==================================================="

print "In this world we have ", continents, " continents."

for key, value in continentAreas.items():
  if value is not None:
    print 'Continents ', key, ' has a size of ', value, ' units.'