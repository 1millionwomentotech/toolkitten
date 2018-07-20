# ```
# soc01h-cc-daniella-dsouza.py
# ```
# Author : Daniella D'Souza
# Dated : July 18th , 2018
# 1MWTT Week 1 Hackathon


def find_neighbors(tile_index, tile, land, continents):
    # Iterate thru the tuples
    current_continent = []
    merged = False

    found_continent = False

    # Does this tile belong to a continent
    for continent in continents:
        if tile in continent:
            current_continent = continent
            found_continent = True
            return
        
    # Let's put in in the temporary bucket
    if (found_continent == False): 
        current_continent.append(tile)

    # Let us start looping over all the land tiles
    merged_with_continent = False
    
    for j, l in enumerate(land):
        merged = False
        if (j != tile_index):  # don't want to compare with itself 
            if ((abs(l[0] - tile[0]) < 2) and (abs(l[1] - tile[1]) < 2)):
                # We are neighbors
                # Check if t exists on a certain continent, do a lookup
                for c in continents:
                    if l in c:
                        # Merge with this continent
                        if (c != current_continent):
                            c.append(tile)
                            merged_with_continent = True
                            #print("merged with a continent")
                            current_continent = c
                            merged = True
                            break
                # either I merge with your continent or you merge with mine
                if (merged == False):    
                    current_continent.append(l)

    if (merged_with_continent == False):
        continents.append(current_continent)
                                                        
    return 

def merge(list1, list2):
    return list(set(list1 + list2))

def is_neighbor(tile ,continent):
    for t in continent:
        if ((abs(t[0] - tile[0]) < 2) and (abs(t[1] - tile[1]) < 2)):
            return True

    return False
        

def find_continents(land):
    """find_continents returns a list of lists of land""

    >>>find_continents([(0,0),(0,1),(0,2),(1,0),(3,0)) returns list of two lists
    (0,0),(0,1),(0,2),(1,0) and (3,0)"""
    continents = []
    
    for index, t in enumerate(land):
        find_neighbors(index, t, land, continents)

    continents.sort(key=lambda c:len(c), reverse = True)
    merged_continent = False
    merged = []

    for i, c in enumerate(continents):
        sub_continent = continents[i+1:]
        for j, d in enumerate(sub_continent):
            merged_continent = False
            for l in d:
                if ((l in continents[i]) or is_neighbor(l ,continents[i])):
                    continents[i] = merge(continents[i], d)
                    #print(i, continents[i])
                    continents[j+1] = []
                    merged_continent = True
                if (merged_continent == True):
                   break
    
    final_continents = [c for c in continents if len(c) > 0]
    
           
    #print(len(continents))
    #print("*", len(final_continents))
    #print(final_continents)
     
    return final_continents

def find_continent(tile, final_continents):
    for c in final_continents:
        if (tile in c):
            print("You are on a continent", "of size", len(c))
            return
    print("You are in the ocean")
            
def find_land(world):
    """Returns the individual tiles of land in the world.

    >>> find_land("WWWWLLLL","LLWWLLLL")
    [(0,0),(0,1),(0,2),(0,3),(1,2),(1,3)]
    """
    #print("find_land()")
    land = []
    for i, row in enumerate(world):
        for j, c in enumerate(row):
            t = (i,j)
            if (c == "L"):
                land.append(t)
                    
    return land


if __name__ == "__main__":
    row1 = "W" * 3
    row1 = row1 + "L" *3 + "W" * 3 + "L" * 2
    row2 = "L" * 9
    row2 = row2 + "W" * 2
    rows = [row1, row2, row1, row2, row1, row2, row1, row2, row1, row2, row1]

    print(rows)
    land = find_land(rows)
    final_continents = find_continents(land)
    x = input("Please enter a number between 1 and 11 ")
    y = int(x)
    print("Let us assume you are standing on tile",y,",", y)
    find_continent((y,y), final_continents)
