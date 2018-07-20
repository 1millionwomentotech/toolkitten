
#create the civilization world
world = [[1,1,1,1,0,0,0,0,0,0,0], [1,1,1,0,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0,0],[0,0,0,1,1,1,1,0,0,1,0],
[0,0,0,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,1,0,0]]

size = 11

#prepare vars - changing
myContinent = 1

row = 5
col = 5
mySet = set()
mySet.add((row,col))

myMap = set()
myMap.add((row,col))
allCont = 1

#stable vars
cursorR = row
cursorC = col
cursor = (cursorR, cursorC)
startR = row
startC = col
start = (row, col)

#MOVE LEFT
def moveLeft(r,c, world = world, n = size):
  global mySet
  global myContinent
  global myMap
  global allCont
  # global myMap
  while c > -1:
    if c == -1:
        break
    lastCount = (r,c)
    if world[r][c] == 1 and not (lastCount in myMap):
      allCont = allCont + 1
            #C1
      if (r-1) > -1 and (c-1) > -1 and world[r - 1][c - 1] == 1 and (r-1,c-1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C2
      elif (r-1) > -1 and world[r - 1][c] == 1 and (r-1,c) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C3
      elif (r-1) > -1 and (c+1) < n and world[r - 1][c + 1] == 1 and (r-1,c+1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C4
      elif (c+1) < n and world[r][c + 1] == 1 and (r,c+1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C5
      elif (r+1) < n and (c+1) < n and world[r + 1][c + 1] == 1 and (r+1,c+1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C6
      elif (r+1) < n and world[r + 1][c] == 1 and (r+1,c) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C7
      elif (r+1) < n and (c-1) > -1 and world[r + 1][c - 1] == 1 and (r+1,c-1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C8
      elif (c-1) > -1 and world[r][c - 1] == 1 and (r,c-1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
    myMap.add(lastCount)
    c = c - 1


#MOVE RIGHT
def moveRight(r,c, world = world, n = size):
  global myContinent
  global mySet
  global myMap
  global allCont
  while c < n:
    if c == n:
        break
    lastCount = (r,c)
    if world[r][c] == 1 and not (lastCount in myMap):
      allCont = allCont + 1
            #C1
      if (r-1) > -1 and (c-1) > -1 and world[r - 1][c - 1] == 1 and (r-1, c-1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C2
      elif (r-1) > -1 and world[r - 1][c] == 1 and (r-1, c) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C3
      elif (r-1) > -1 and (c+1) < n and world[r - 1][c + 1] == 1 and (r-1, c+1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C4
      elif (c+1) < n and world[r][c + 1] == 1 and (r, c+1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C5
      elif (c+1) < n  and (r+1) < n and world[r + 1][c + 1] == 1 and (r+1, c+1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C6
      elif (r+1) < n and world[r + 1][c] == 1 and (r+1,c) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C7
      elif (r+1) < n and world[r + 1][c - 1] == 1 and (r+1, c-1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
            #C8
      elif (c-1) > -1 and world[r][c - 1] == 1 and (r, c-1) in mySet:
        mySet.add(lastCount)
        myContinent = myContinent + 1
      else:
        mySet = mySet
        myContinent = myContinent
    myMap.add(lastCount)
    c = c + 1

#MOVE UP
def moveUp():
  global cursorR
  global cursor
  cursorR = cursorR - 1
  cursor = (cursorR, cursorC)
  moveLeft(cursorR, cursorC)
  moveRight(cursorR, cursorC)
#MOVE DOWN
def moveDown():
  global cursorR
  global cursor
  cursorR = cursorR + 1
  cursor = (cursorR, cursorC)
  moveLeft(cursorR, cursorC)
  moveRight(cursorR, cursorC)

#FINAL COUNT FUNCTION
def mapWorld():
    global cursorR
    global cursorC
    global cursor
    moveLeft(cursorR, cursorC)
    moveRight(cursorR, cursorC)
    for i in range(1,size - startR):
      moveUp()
    cursorR = startR
    cursorC = startC
    cursor = start
    for i in range(1,size - startR):
      moveDown()

#RESET FUNCTION
def resetCheck():
    global cursorR
    global cursorC
    global myMap
    global myContinent
    global allCont
    myContinent = 1
    allCont = 1
    cursorR = startR
    cursorC = startC
    myMap = set()
    myMap.add((cursorR,cursorC))

#CHECK FUNCTION
def proofRead():
    resetCheck()
    mySetCheck = len(mySet)
    for i in range(0, startR):
      mapWorld()
    return(mySetCheck == len(mySet))


#RUN RUN RUN
mapWorld()

while proofRead() == False:
  mapWorld()

print("Results")
print("my Continent size: ", myContinent)
print("all continents  together: ", allCont)
