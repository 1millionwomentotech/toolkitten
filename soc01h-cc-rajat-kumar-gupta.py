import random as rand
import numpy as np

#0 for water
#1 for land
#Random world generator
# world = []
# row = int(input("Enter number of rows in the matrix: "))
# col= int(input("Enter number of columns in the matrix: "))
# for i in range(row):
#     one_d_world = []
#     for j in range(col):
#         one_d_world.append(rand.randint(0,1))
#     world.append(one_d_world)

# Fixed world input
world = [
[0,0,0,0,1],
[0,0,0,1,0],
[0,0,1,0,0],
[1,1,0,0,1],
[0,1,0,0,1]
]
row = len(world)
col = len(world[0])


#User input
# row = int(input("Enter number of rows in the matrix: "))
# col= int(input("Enter number of columns in the matrix: "))
# world = []
# for i in range(row):
#     world.append([])
#     for j in range(col):
#         world[i].append(int(input()))


# A utility function to do DFS for a 2D boolean matrix.
def applyDfs(x, y, visited):

    # These arrays are used to get row and column numbers of 8 neighbours of a given cell
    rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
    colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]

    # Mark this cell as visited
    visited[x][y] = True
    count = 1
    for k in range(8):
        if isSafe(x + rowNbr[k], y + colNbr[k], visited):
            count = count + applyDfs(x + rowNbr[k], y + colNbr[k], visited)

    return count

def isSafe(i, j, visited):
        # row number is in range,
        # column number is in range
        # world[i][j] not yet visited
        # world[i][j] is land
        return (i >= 0 and i < row and
                j >= 0 and j < col and
                not visited[i][j] and world[i][j])

def countContinents():
    # visited array of booleans
    # initializing each element to False
    visited = [[False for j in range(row)]for i in range(col)]
    print(np.matrix(world))
    print ("Where are you standing?Position x : ")
    x = int(input())
    print ("Where are you standing?Position y : ")
    y = int(input())

    #Calculating size by position
    if visited[x][y] == False and world[x][y] == 1:
                applyDfs(x,y,visited)

    # Assumption : Taking each tile 1 unit long and 1 unit wide so area is 1 unit square
    # to avoid complexity
    size = 0
    for k in range(len(visited)):
        for l in range(len(visited[k])):
            if visited[k][l] == True:
                size+=1
    print(f"Size of the continent that you are standing on:{size}")

    # Finding number of continents to calculate each of their size
    visited = [[False for j in range(row)]for i in range(col)]
    number_of_continents = 0
    for i in range(row):
        for j in range(col):
            if visited[i][j] == False and world[i][j] == 1:
                tempVal = applyDfs(i,j,visited)
                number_of_continents+=1
                print(f"Size of continent {number_of_continents} --> {tempVal}")

    print(f"Number of continents in this world: {number_of_continents}")

countContinents()
