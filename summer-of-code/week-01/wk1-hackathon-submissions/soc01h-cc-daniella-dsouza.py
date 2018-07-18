# ```
# soc01h-cc-daniella-dsouza.py
# ```
# Author : Daniella D'Souza
# Dated : July 18th , 2018
# 1MWTT Week 1 Hackathon

def generate_row():
    row = []
    for j in range(11):
        if (j%3):
            row.append('X')
        else:
            row.append('O')
    print(row)
    return row

def build_world(world):
#    for i in range(11):
    row = generate_row()
    world = row
    print(world)

def find_neighbors(index, l, land, continents):
    # Iterate thru the tuples
    continent = []
    
    for c in continents:
        if l in c:
            c.append(l)
            continent = c
        else:
            continent.append(l)
            
    #print(remainingland)
    remainingland = []
    remainingland = land.pop(index)

    length = len(land)
    
    for j, t in enumerate(land):
        if (j != index):  # don't want to compare with itself
            #print(j,t)
            if (j < length-1):
                if ((abs(l[0] - land[j][0]) < 2) and (abs(l[1] - land[j][1]) < 2)):
                    # Check if t exists on a certain continent, do a lookup
                    for c in continents:
                        if t in c:
                            c.append(t)
                        else:
                        # If it does not then attach it to this continent
                            continent.append(t)
                    #remainingland = land.pop(j)

    # find_neighbors(land[j+1:])
    if (len(continent) > 0):
        continents.append(continent)

    print(continents)
    
    return 
    
def find_continents(land):
    """find_continents returns a list of lists of land""

    >>>find_continents([(0,0),(0,1),(0,2),(1,0),(3,0)) returns list of two lists
    (0,0),(0,1),(0,2),(1,0) and (3,0)"""
    continents = []
    print("find_continents")
    for index, t in enumerate(land):
        find_neighbors(index, t, land, continents)
        

    print(continents)
        
    

# Works Well       
def find_land(world):
    """Returns the individual tiles of land in the world.

    >>> find_land("WWWWLLLL","LLWWLLLL")
    [(0,0),(0,1),(0,2),(0,3),(1,2),(1,3)]
    """
    print("find_land()")
    land = []
    for i, row in enumerate(world):
        for j, c in enumerate(row):
            #print("(%d, %d) - %s" % (i, j, c))
            t = (i,j)
            print(t)
            if (c == "L"):
                #check to see if there are neighbors it can join
                land.append(t)
                    
    print(land)
    print(len(land))
    print("End find_land()")
    return land

    
    
    
"""              l = len(land)
                for k, t in enumerate(land):
                    print(k,t)
                    
                    if ((abs(land[k][0] - t[0]) < 2) and (abs(land[k][1] - t[1]) < 2)):
                        # Add logic to check if t is not already part of a continent, if yes then the new tuple should be put in that continent
                        continents.append(t)"""

if __name__ == "__main__":
    row1 = "W" * 3
    row1 = row1 + "L" *3 + "W" * 3 + "L" * 2
    row2 = "L" * 9
    row2 = row2 + "W" * 2
    rows = [row1, row2]
    
    #print(row1)
    #print(row2)

    print(rows)
    land = find_land(rows)
    find_continents(land)
