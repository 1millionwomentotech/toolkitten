#week 1 hackathon

#The purpose of this code is to
# 1) Generate a random map for Civilisation 3 (see generate_civIII_Map() method)
# 2) Identifies all the different continents and assigns separate letters to each
#       (see )
# 3) Quantifies the size of each continent and provides a list of these
# 4) Identifies the 2 largest continents that would be suitable for playing

#need to import the random library to generate random numbers
import random

#this draws the map that has been generated
def drawMap():
    for s in map:
        print(*s)

#this creates and draws a random 11x11 civilisation III map
#loops are used to create 11 numbers for each row 11 times
def generate_civIII_Map():
    for i in range (0, 11):
        row = []
        for j in range (0,11):
            #this uses a random number generator for the numbers 0 and 1 with 0
            #representing the sea and 1 representing the land
            new = random.randint(0,1)
            row.append(new)
            j +=1
        map.append(row)
        i += 1
    drawMap()
    

#this is the code to check all tiles around a specified tile to see if there
#is a land tile adjacent or diagonal to it. To prevent the code from crashing
#it checks the position of the tile in question and if it is at the top of the map
#it only checks tiles below and either side. If it is situated on the left edge of the map
#it only checks tiles to the right of it and above and below.
def checkAround(t,s, continent):
    for t in range (0,11):
        for s in range (0,11):
            if t == 0 and s == 0:
                if map[t][s] == continent:
                    for y in range (t, t+2):
                        for z in range (s, s+2):
                            if map[y][z] == 1:
                                map[y][z] = continent
            if t == 0 and 0 < s < 10:
                if map[t][s] == continent:
                    for y in range (t, t+2):
                        for z in range (s-1, s+2):
                            if map[y][z] == 1:
                                map[y][z] = continent
            if s == 0 and 0 < t < 10:
                if map[t][s] == continent:
                    for y in range(t-1, t+2):
                        for z in range (s, s+2):
                            if map[y][z] == 1:
                                map[y][z] = continent
            if 0 < s < 10 and 0 < t < 10:
                if map[t][s] == continent:
                    for y in range (t-1, t+2):
                        for z in range (s-1, s+2):
                            if map[y][z] == 1:
                                map[y][z] = continent
  
    
#this is the code that converts all the land squares to a continent
#letter so it is easier to 'see' the seperate continents and
#quantify their mass
def findLandMass():
    i = 0
    j = 0
    continent = 'a'
    global all_continents
    all_continents = []
    for i in range (0, 11):
        for j in range (0, 11):
            if map[i][j] == 1 :
                map[i][j] = continent
                #this needs to be repeated 8 times to ensure all the tiles around each
                #land tile are checked for adjacency.
                for w in range(8):
                    checkAround(i,j,continent)
                all_continents.append(continent)
                #need to use ord to convert the character to an integer to increase and then
                #use chr to convert this back to a character
                continent = chr(ord(continent)+1)


#this calculates the size of each continent and prints out the information for the user
def continentSize():
    print('Continent information')
    rank_size = []
    for x in all_continents:
        xAmount = 0
        for i in range(0,11):
            xAmount = xAmount + map[i].count(x)
        rank_size.append([xAmount, x])
        print('There are', xAmount, 'tile(s) available on continent', x)
    print('')
    rank_size.sort()
    print('The top two continents to play on based on size are:')
    print('Continent', rank_size[len(rank_size)-1][1], 'which has', rank_size[len(rank_size)-1][0], 'tile(s)')
    print('and Continent', rank_size[len(rank_size)-2][1], 'which has', rank_size[len(rank_size)-2][0], 'tile(s).')
    


#this pulls all the code together into a single simulation
def runSim():
    print('Summer of Code Week 1 Hackathon results')
    print('')
    #create a new instance of the map
    global map
    map = []
    #populate the map with random numbers and print the initial copy of it
    print('Initial map')
    generate_civIII_Map()
    print('')
    print('')
    findLandMass()
    #to show how map has been labelled
    print('Map with continents labelled')
    drawMap()
    print('')
    print('This map has', len(all_continents), 'continents')
    print('')
    print('')
    continentSize()
    
    

runSim()
    
