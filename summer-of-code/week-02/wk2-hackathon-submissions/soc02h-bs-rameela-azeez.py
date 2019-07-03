#boggle game uses 16 dices with six sides with letters
#find all words and points scored
#Rameela Azeez
#dictionary https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt

from string import ascii_uppercase
import random
       
def boggledices(X,Y):
    grid={}
    i=0
    bd=["AAEEGN","ELRTTY","AOOTTW","ABBJOO","EHRTVW","CIMOTU","DISTTY","EIOSST","DELRVY","ACHOPS","HIMNQU","EEINSU","EEGHNW","AFFKPS","HLNNRZ","DEILRX"]
    i=0
    for x in range(X):
        for y in range(Y):
            grid[x,y]=bd[i][random.randint(0,5)]  
            i+=1
    return grid

def findneighbours():
    ctr=0
    for position in matrix:
        x, y = position
        
        '''
        for each cell there can be maximum 6 neighbours
        [ ][ ][ ]
        [ ][*][ ]
        [ ][ ][ ]
        '''
        #top mid, top right, mid right, bot right, bot mid, bot left, mid left, top left
        positions = [(x-1, y),(x-1, y+ 1),(x,y+1),(x +1, y + 1),(x+1, y) ,(x +1, y -1),(x, y-1),(x - 1, y - 1)]
        
       
        ctr=ctr+1
        thiscellneighbours=[] # array for this cell
        i=0
        for p in positions: # [0,0] ... [1,1]
            #print(position,p)
            if (((p[0] >=0) and (p[0] < x)) and ((p[1] >=0) and (p[1] < y))):
                #print(p)
                thiscellneighbours.append(p)
                
        neighbours[position]=thiscellneighbours # all cells and their neighbours
    
def getdictionary(wordfile):
    with open(wordfile) as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)
            for i in range(len(word)):
                stems.add(word[:i + 1])
                
def pathtoword(path):
    #convert  list of grid positions to a word
    s=''
    for p in path:
        s=s+matrix[p]       
    return s

def search(path):
    # search the grid recursively for words
    word = pathtoword(path)
    if word not in stems:
        return
    
    if word in dictionary:
        paths.append(path)
        
    for nextpos in neighbours[path[-1]]: # path [-1] returns last element
        if nextpos not in path:
            search(path + [nextpos]) # add node to path and do recursion


def findwords():
    for position in matrix:
        search([position])
        for p in paths:
            bogglewords.add(pathtoword(p))

def getpoints():
    pointsys={0:0,1:0,2:0,3:1,4:1, 5:2, 6:3,7:5,8:11}
    points=0
    for word in bogglewords:
        wordpoint=0
        l=len(word)
        if (1 <= l <=8): wordpoint=pointsys[len(word)]
        elif (l>8): wordpoint=11
        if (wordpoint > 0):points+=wordpoint
    return points


neighbours = {} #empty dictionary
stems, dictionary = set(), set()
paths=[]
bogglewords=set()
matrix=boggledices(4,4)
findneighbours()
getdictionary("dictionary.txt")
findwords()
points=getpoints()  
output={"score": points,"words": [ el for el in bogglewords ]}
print (output)