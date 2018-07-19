# ```
# soc01h-cc-daniella-dsouza.py
# ```
# Author : Daniella D'Souza
# Dated : July 18th , 2018
# 1MWTT Week 1 Hackathon


def find_neighbors(index, l, land, continents):
    # Iterate thru the tuples
    continent = []

    found_continent = False
    print("Incoming tile", l)
    for c in continents:
        #print(c, l)
        if l in c:
            continent = c
            found_continent = True
            break

    if (found_continent == False): 
        continent.append(l)
        continents.append(continent)
            
    #print(remainingland)
        
    #land.pop(index)

    length = len(land)
    
    for j, t in enumerate(land):
        if (j != index):  # don't want to compare with itself
            #print(j,t)
            
            if ((abs(l[0] - land[j][0]) < 2) and (abs(l[1] - land[j][1]) < 2)):
                            # Check if t exists on a certain continent, do a lookup
                if t not in continent:
                    continent.append(t)
                    #print(continent)
                                                        
    #print(continents)
    
    return 
    
def find_continents(land):
    """find_continents returns a list of lists of land""

    >>>find_continents([(0,0),(0,1),(0,2),(1,0),(3,0)) returns list of two lists
    (0,0),(0,1),(0,2),(1,0) and (3,0)"""
    continents = []
    print("find_continents")
    
    for index, t in enumerate(land):
        find_neighbors(index, t, land, continents)
        
    for c in continents:
        print(c, len(c))

    continents.sort(key=lambda c:len(c), reverse = True)
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
            #print(t)
            if (c == "L"):
                land.append(t)
                    
    print(land)
    print(len(land))
    print("End find_land()")
    return land


if __name__ == "__main__":
    row1 = "W" * 3
    row1 = row1 + "L" *3 + "W" * 3 + "L" * 2
    row2 = "L" * 9
    row2 = row2 + "W" * 2
    rows = [row1, row2]

    print(rows)
    land = find_land(rows)
    find_continents(land)
