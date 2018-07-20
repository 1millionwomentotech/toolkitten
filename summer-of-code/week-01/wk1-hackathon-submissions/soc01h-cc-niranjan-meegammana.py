# -*- coding: utf-8 -*-
"""
Calculate the size of a continent you are standing on in your 11 x 11 world in Civilization III.
Bonuses for:
1. calculate continent size for all continents in the world
2. random world generator
3. fastest program
4. benchmarking
5. extension of the problem to n x n size world

Assumption for world generation
71% of world covered with water , 96.5 of that is see so 68.5 is sea area
so water to land ratio is 68.5 : 31.5 , 685:315

outputs
matrix_n.txt matrix generated 
matrix_log.txt program log
matix_results1.txt results 

create 
@author: Niranjan Meegammana, Shilpa Sayura Foundation , Sri Lanka
"""
import time
import random
import sys

#configuration variables
fillinladwater=True # fix inland water bodies
outputtoscreen=True 
outputtofile=True
randomization = False # Random Grid Sizing or series 
ntests=3 # number of tests to run - updated again below


def logtime(s0,s1,filename):
    ts=str(time.time()-starttime) # time difference
    s2=s0 + " : " + s1+ " : " + str(ts)  # log action and time
    if (outputtofile):
        file=open("matrix_log.txt", 'a') #open for append
        file.write(s2  + "\n")
        file.close()
        file1=open(filename, 'a') #open for append
        if (s1):
            file1.write (s1 + "\n")
        #file1.write (ts  + "\n")
        file1.close()
    if (outputtoscreen):
          print(s2)

def getfilename(): # a unique file name for each test
   fl= "matrix_"+ str(int((time.time()-1513728000)*10)) + ".txt"
   if (outputtofile):
        file=open(fl, 'w') #open for writing test
        file.close()

   return fl

def fillinlandwater(matrix):
    lx=len(matrix)-1
    ly=len(matrix[0])-1
    # algorithm to seach and fill inland water
    for x in range(len(matrix)):
      for y in range(len(matrix[0])):
          if (matrix[x][y]==0): # water
                 if ((x > 0) and (x < lx) and (y > 0) and (y < ly)) : #not edge but inside
                     #diagonal not considered
                     if ((matrix [x - 1][y]==1) and (matrix [x +1][y]==1) and (matrix [x][y-1]==1) and (matrix [x][y+1]==1)) :
                         matrix[x][y]=1 # convert to a land

    return matrix

def generateworld(h, w): #generate matrix of given size x->h,y-w
  if ((h <=0) or (w<=0)):
      return [[]]
      
  matrix= [[generatetile() for i in range(w)]for i in range(h)]
  if (fillinladwater): # convert inland water bodies as land
      matrix=fillinlandwater(matrix)
  return matrix

def generatetile():
    '''
    71% of world covered with water , 96.5 of that is see so 68.5 is sea area
    so water to land ratio is 68.5 : 31.5 , 685:315
    '''
    if (random.randint(0,1000) < 315):
        return 1
    else:
        return 0

def removecontinent(matrix, x, y) : #recursive algorthm x row y cols
        if (matrix[x][y]==1) :
            matrix[x][y] = 0
            tiles[len(tiles)-1]=tiles[len(tiles)-1]+1
            
            if (x > 0) :
                removecontinent(matrix, x-1, y ) #top
            
            if (x < len(matrix) - 1) :
                removecontinent(matrix, x+1, y ) #down
                
            if (y > 0) :
                removecontinent(matrix, x , y-1) #left

            if (y < len(matrix[x]) - 1) :
                removecontinent(matrix, x, y+1) #right

            if ((x > 0) and (y > 0)):
                removecontinent(matrix, x - 1, y-1) #left up

            if ((x > 0)  and (y > len(matrix[x])-1) ):
                    removecontinent(matrix, x - 1, y+1) #Right up

            if ((y < len(matrix[x])-1) and (x < len(matrix) - 1)) :
                    removecontinent(matrix, x + 1, y+1) #Right down

            if ((y > 0)   and (x < len(matrix)-1)):
                    removecontinent(matrix, x + 1, y-1) #left down


def continentCount(matrix,tiles): #scan and count continentals
    numcontinents = 0;
    for x in range(len(matrix)):
      for y in range(len(matrix[0])):
          if (matrix[x][y]==1):
              tiles.append(1)
              removecontinent(matrix, x, y)
              numcontinents=numcontinents+1

    return numcontinents

def dispresults (tiles, filename):
    #rfilename=filename.replace(".txt", "_r.txt")

    if (outputtofile==True):
        f1=open(filename, 'a')
        # f1.write(str(len(tiles)) + "\n")

    for i in range (len(tiles)-1) :
        s=str(i) + " " + str(tiles[i])
        if (outputtofile==True):
            f1.write(s + "\n")
        if (outputtoscreen):
            print (s)
    if (outputtofile==True):
        f1.close()


def displayMatrix (matrix,outputtoscreen,outputtofile,filename):
    if (outputtofile):
        f1=open(filename, 'a')

    for x in range(len(matrix)):
        s=""
        for y in range(len(matrix[x])):
           s=s + " " + str(matrix[x][y] )

        if (outputtofile):
            f1.write(s + "\n")

        if (outputtoscreen):
            print(s)

    if (outputtofile==True):
        f1.close()

def writeresults(program):
    #print (program)
    f2=open("matix_results.txt", 'a') #open for append
    sx=str(program["ctr"]) + "," + str(program["filename"]) + "," + str(program["h"]) + "," + str(program["w"]) + "," 
    sx=sx + str(program["h"] * program["w"]) + "," + str(program["contcount"])  + ","
    sx=sx + str(sum(program["tiles"])) + "," + str(program["genend"] - program["genstart"])  + ","
    sx=sx+ str(program["countendtime"] - program["countstarttime"]) + ","+ str(time.time()) + "\n"
    f2.write(sx)
    f2.close()
 
# main program #########################=
# main variables
ctr=0

#test values

ntests=10
multiplierbase=11
multipliers=[] #grid size multiplier
for i in range (ntests):
    multipliers.append (i* multiplierbase )
    if (multipliers[i] > 11):
        multiplierbase=multiplierbase + multiplierbase
print(multipliers)  

while (ctr < ntests ) :
    starttime=time.time()
    program={}
    tiles=[]
    program["starttime"]=starttime
    program["ctr"] = ctr
    program["tiles"] = tiles
    program["filename"]=getfilename()
    print (program["filename"])
    
    logtime("Starting : " + program["filename"] ,  str(ctr) , program["filename"])
    # Randint produces a float val
    #w=int(random.randint(5,1000))
    #h=int(random.randint(5,1000))
    
    if (randomization==True):
    #randomization for grid in many ways n x n and n x m
        n=int(random.random() * 1000)
        program["h"]=int(random.random() * n) # x
        program["w"]=int(random.random() * n) # y program["w"]
    else:
        n=multipliers[ctr]
        program["h"]=n # x
        program["w"]=n
    #print(n)  
    #program["h"]=program["w"] # int(random.random() * n)
    sx= str(program["h"]) + " " + str(program["w"])
    print("Matrix : " , sx)
    
    logtime("Generating World:", sx, program["filename"])
    #print(program["w"], program["h"])
    program["genstart"]=time.time()
    program["matrix"]= generateworld(program["h"], program["w"]) # x rows ,y cols
    program["genend"]=time.time()
    logtime("Displaying World :","",program["filename"])
    starttime=time.time() # resetset time
    displayMatrix(program["matrix"],outputtoscreen,outputtofile,program["filename"])
    logtime("World File Created" ,"", program["filename"])
    
    logtime("Starting Counting:","",program["filename"])
    starttime=time.time() # resetset time
    program["countstarttime"]=time.time()
    program["contcount"]=continentCount(program["matrix"], program["tiles"])
    program["countendtime"]=time.time()
    logtime("Continentals : " , str(program["contcount"]), program["filename"] )
    logtime("Continentals Sizes: ","",program["filename"] )
    dispresults(program["tiles"], program["filename"])
    writeresults(program)
    logtime("Thank You for waiting : -----","", program["filename"] )
    ctr=ctr+1
    
