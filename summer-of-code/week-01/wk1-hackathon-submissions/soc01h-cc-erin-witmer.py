# Erin Witmer
# Week 1 Hackathon
# This program builds a world and then finds the size of continents, or continguous land masses in the world.

import random

cont = []

#matrixSize = 11
countries = [['a',0]]
countryIndex = 0
callStack = []

#builds a world of 0s and 1s of size matrixSize
def buildWorld(size):
    for i in range(matrixSize):
        inner = []
        for j in range(matrixSize):
            inner.append(random.randint(0, 1))
        cont.append(inner)

#changes the '1' to the country name and increments the country size counter
def updateNode(i,j):
    cont[i][j] = countries[countryIndex][0]
    countries[countryIndex][1] = countries[countryIndex][1] + 1

#when finding children, pushes to call stack for recursive call
def pushToCallStack(i, j):
    callStack.insert(0,[i, j])
       
#updates the child node and pushes to call stack     
def updateChild(i, j):
    if(cont[i][j] == 1):
        updateNode(i, j)
        pushToCallStack(i, j) 

#finds all children depending on where the node is in the grid
def findChildren(i, j):
  
    # Top left corner 
    if (i == 0 and j == 0):
        updateChild(i+1,j)       #downCenter
        updateChild(i+1,j+1)     #downRight
        updateChild(i,j+1)       #inRight
    
    # Top right corner
    elif (i == 0 and j == matrixSize - 1):
        updateChild(i,j-1)       #inLeft
        updateChild(i+1,j-1)     #downLeft
        updateChild(i+1,j)       #downCenter
    
    # Bottom left corner
    elif (i == matrixSize - 1 and j == 0):
        updateChild(i-1,j)       #upCenter
        updateChild(i-1,j+1)     #upRight
        updateChild(i,j+1)       #inRight               
        
    # Bottom right corner
    elif (i == matrixSize - 1 and j == matrixSize - 1):
        updateChild(i,j-1)        #inLeft
        updateChild(i-1,j-1)      #upLeft
        updateChild(i-1,j)        #upCenter
    
    # Top row
    elif (i == 0):
        updateChild(i,j-1)       #inLeft
        updateChild(i+1,j-1)     #downLeft
        updateChild(i+1,j)       #downCenter
        updateChild(i+1,j+1)     #downRight
        updateChild(i,j+1)       #inRight
    
    # Left side
    elif (j == 0):
        updateChild(i-1,j)       #upCenter
        updateChild(i-1,j+1)     #upRight
        updateChild(i,j+1)       #inRight
        updateChild(i+1,j+1)     #downRight
        updateChild(i+1,j)       #downCenter
    
    # Right side
    elif (j == matrixSize - 1):
        updateChild(i-1,j)       #upCenter
        updateChild(i-1,j-1)     #upLeft
        updateChild(i,j-1)       #inLeft
        updateChild(i+1,j-1)     #downLeft
        updateChild(i+1,j)       #downCenter
    
    # Bottom row
    elif (i == matrixSize - 1):
        updateChild(i,j-1)       #inLeft
        updateChild(i-1,j-1)     #upLeft
        updateChild(i-1,j)       #upCenter
        updateChild(i-1,j+1)     #upRight
        updateChild(i,j+1)       #inRight
        
    # Center cells
    else:
        updateChild(i,j-1)        #inLeft
        updateChild(i-1,j-1)      #upLeft
        updateChild(i-1,j)        #upCenter
        updateChild(i-1,j+1)      #upRight
        updateChild(i,j+1)        #inRight
        updateChild(i+1,j-1)      #downLeft
        updateChild(i+1,j)        #downCenter
        updateChild(i+1,j+1)      #downRight       

print("Welcome to Civilations III!")
print("This program will randomly generate an (n x n) world and tell you how large each continent is.")
matrixSize = int(input("How large would you like the board to be? (n): "))

buildWorld(matrixSize)

print("Here is your board: ")

# prints out original
for i in range(matrixSize):
    print(cont[i])

# for all rows
for i in range(matrixSize):
    #for all columns
    for j in range(matrixSize):
        #if you land on a '1', 
        if(cont[i][j] == 1):
            # update it
            updateNode(i,j)
            # find its children and push them to the call stack
            findChildren(i, j)
            #while there are nodes in the call stack
            while len(callStack) > 0:
                #pop the current one off and recursively find its children
                current = callStack.pop()
                findChildren(current[0],current[1])
            # once the call stack is empty, create a new country and seach the board for additional land masses
            nextCountryName = chr(ord(countries[countryIndex][0]) + 1)
            countries.append([nextCountryName,0])
            countryIndex = countryIndex+1
        

print("\n")
print("A continent is a contiguous land mass (including land masses adjoined diagonally.)")
print("Here is the board identified by continent.")
print("\n")
for i in range(matrixSize):
    print(cont[i])
print("\n")
print("Here is the total size of each country")
for i in range(len(countries)-1):
    print countries[i][0],':',countries[i][1]
        
