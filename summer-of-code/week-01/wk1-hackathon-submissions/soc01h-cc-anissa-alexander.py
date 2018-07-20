#########################################################
# Civilization III Text Map Generator                   #
# Features:                                             #
#       + Benchmarking                                  #
#       + Saving and loading maps                       #
#       + Generating Maps                               #
#       + Displaying Maps                               #
#       + Counting Contient (User or Random)            #
#                                                       #
#########################################################

# imports
import os 
from os import path
import random # map.py/calc_map.py
from collections import deque #calc_map.py
from operator import eq #calc_map.py


##################################################################
# Code formally in seperate map.py file                          #
##################################################################
arr = []
world = []


def add_list(t):
    i = 0
    while i < t:
        n = random.randint(0, 1)
        arr.append(n)
        i += 1


def build_world(t):
    reset_map()
    for x in range(0, t):
        arr.clear()
        add_list(t)
        x += 1
        world.append(arr.copy())
    return world

def reset_map():
    global arr
    global world
    arr = []
    world = []

def load_map(filename):
    
    if not os.path.exists((os.path.join("maps",filename))):
        return None
    else:
        reset_map()
        print(os.path.join("maps",filename))
        f = open(os.path.join("maps",filename),"r")
        if f.mode == 'r': # check to make sure that the file was opened
            fl = f.readlines()
            for line in fl:
                line = line.rstrip("\n")
                world.append([int(val) for val in line.split(" ")])
        f.close()
    
    return world

def save_map(filename):
    global world
    f = open(os.path.join("maps",filename),"w")
    if f.mode == 'w': # check to make sure that the file was opened
        print_out =[]
        for line in world:
            line = [str(elem) for elem in line]
            print_out.append(" ".join(line))
        
        result = "\n".join(print_out)

        f.writelines(result)
    f.close()

def print_world(world):
    for row in world:
        print(row)

    #print(f"world: {world}")

##################################################################
# Code formally in seperate calc_map.py file                     #
##################################################################
## to make random
map = []

def explore_continent_rand_pos(map):
    """ Starting at a random position, (i, j) search 8 directions:
        1 block north, 1 block east, 1 block south, 1 block west
        1 block northeast, 1 block southeast, 1 block southwest, 1 block northwest
        by adding/subtracting 1 from `i` and `j`

                   (-1, -1)  (-1, 0)  (-1, +1)
                          \     |     /
                 (0, -1) --   (i,j)   -- (0, +1)
                          /     |     \
                   (+1, -1)  (+1, 0)  (+1, +1)
    """
    neighbors = (-1, 0), (0, +1), (+1, 0), (0, -1), (-1, +1), (+1, +1), (+1, -1), (-1, -1)

    """ Generate a random position in the map """
    randomPosition = random.randint(0, len(map)-1), random.randint(0, len(map)-1)

    """ similar means that the spont we land on and the neighboring tile are the same: a == b """
    similar = eq

    """ Make sure that the starting position is a land tile
        If it's not, generate a new starting position and check again
        Continue until we get a land tile
    """
    if(get_tile(map, randomPosition) == 0):
        loop = get_tile(map, randomPosition)
        while(loop == 0):
            randomPosition = random.randint(0, len(map)-1), random.randint(0, len(map)-1)
            loop = get_tile(map, randomPosition)

        for j in range(0, len(map)):
            print(map[j])

    else:
        for j in range(0, len(map)):
            print(map[j])
    print("Starting at: " + 
            str(randomPosition) + 
            ":  " + 
            str(get_tile(map, randomPosition))
        )
    print(list(explore_map(map, neighbors, randomPosition, similar)))

# assume that map, row and col are all valid 
def explore_continent_user_pos(map, row, col):
    """ Starting at a random position, (i, j) search 8 directions:
        1 block north, 1 block east, 1 block south, 1 block west
        1 block northeast, 1 block southeast, 1 block southwest, 1 block northwest
        by adding/subtracting 1 from `i` and `j`

                   (-1, -1)  (-1, 0)  (-1, +1)
                          \     |     /
                 (0, -1) --   (i,j)   -- (0, +1)
                          /     |     \
                   (+1, -1)  (+1, 0)  (+1, +1)
    """
    neighbors = (-1, 0), (0, +1), (+1, 0), (0, -1), (-1, +1), (+1, +1), (+1, -1), (-1, -1)

    """ Generate a random position in the map """
    position = row, col

    """ similar means that the spont we land on and the neighboring tile are the same: a == b """
    similar = eq
  
    for j in range(0, len(map)):
        print(map[j])

    print("Starting at: " + 
        str(position) + 
        ":  " + 
        str(get_tile(map, position))
    )
    print("Indices invloved in current continent: ")
    print(list(explore_map(map, neighbors, position, similar)))

def explore_map(array, neighbors, randomPosition, similar):
    continentSize = 1       # start at 1 because we start on a land tile
    startingTile = get_tile(array, randomPosition)             # This is the position starting tile on the map
    block = {randomPosition}                                   # dictionary of the random starting position and elements that match it (the continent). We put the starting positin because it's land
    visit = deque(block)      # double-ended queue: ordered collection that supports removing elements from either end only (https://pymotw.com/2/collections/deque.html)
    nextTile = deque.popleft     # popleft: Remove and return the leftmost element/start from the left and remove elements going to the right
    while visit:    # while on this row
        thisTile = nextTile(visit)     # get the tile to the left
        for neighboringTile in neighbors:   # iterate through the 8 directions/for each of (north, south, ..., etc)
            index = get_next_tile(thisTile, neighboringTile)    # Get the next tile in the given direction
            if index not in block:   # If the neighboring tile is not one I visited
                block.add(index)     # Add it to the dictionary of tiles
                if is_valid(array, index):  # If the tile is not out of bounds
                    value = get_tile(array, index)   # Get the value of the tile (x or 0/ water or land)
                    if similar(value, startingTile):  # IF the value of the neighboring tile matches my starting tile (if it is land)
                        visit.append(index) # 
                        continentSize += 1
        #print(visit)
        yield thisTile      # https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

    print(continentSize)        

def get_tile(array, index):
    """ Get the tile based on the position we're in now
        Initially, this is the randomPosition generated
        Subsequently, this is the tile we move to after we've explored around our position
    """
    row, column = index
    return array[row][column]


def get_next_tile(thisTile, neighboringTile):
    """ Look 1 tile over in the direction specified by the value passed in neighboringTile (north, south, ..., etc.) """
    row, column = thisTile      # thisTile[i, j]
    row_neighboringTile, column_neighboringTile = neighboringTile   # neighborTile[k, l], where [k, l] is the direction we're searching (ex: (-1,0) to go one tile north)

    """ the return value is the end position. This means that I moved in one of the 8 directions from my current tile 
        This is called 8 times for each starting position because I want to check all directions around me for a land mass 
    """
    return row + row_neighboringTile, column + column_neighboringTile


def is_valid(array, index):
    """ Verify that the index is in range of the map """
    row, column = index
    return 0 <= row < len(array) and 0 <= column < len(array[row])

##################################################################
# Code formally in seperate driver.py file                     #
##################################################################

def main():
    quit = False
    curr_map = []

    # if maps folder doesn't already exist make it 
    if not os.path.exists("maps"):
        os.mkdir("maps")

    print("Welcome to the Civilization Text Map Generator\n")
    print("Please not that all maps are expected in a maps folder, \n where this Python script is running.")    

    while (not quit):
        print("[1] Generate New Map")
        print("[2] Load Map")
        print("[3] Save Map")
        print("[4] Print Map")
        print("[5] Find Size of Current Continent (User Given Position)")
        print("[6] Find Size of Current Continent (Random Position)")
        print("[Q] Quit")
        
        choice = input("What action do you want to perform?")

        while not(choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or   choice == "Q" ):
            choice = input("Please enter a valid choice.")
        
        if choice == "1":
            #rows = int(input("How many Rows for your map?\n"))
            cols = int(input("How many #x# for your map?\n"))
            if curr_map:
                curr_map = None
            curr_map = build_world(cols)
        elif choice == "2":
            print("Expected file organization is a nxn matrix of space seperated 1s and 0s \n , where 1 = land and 0 = water")
            file_name = input("What file would you like to load from the maps folder?\n")

            while file_name[-4:] != ".txt":
                file_name = input("Please enter a text file: ")

            curr_map = load_map(file_name)

            if not curr_map:
                print("Map is not avaliable to load")
        elif choice == "3":
            if curr_map:
                file_name = input("What file would you like to save to the maps folder?\n")

                while file_name[-4:] != ".txt":
                    file_name = input("Please enter a text file name: ")

                save_map(file_name)
            else:
                 print("Map is not avaliable to save")
    
        elif choice == "4":
            if curr_map:
                print_world(curr_map)
            else:
                print("There is no map saved to print.")
        elif choice == "5":
            if curr_map:
                print("Enter a starting location.\n")
                print("The Top Left Corner is (0,0)\n")
                print("The bottom Left is ({0},{1})".format(len(curr_map)-1, len(curr_map[0])-1))

                row = int(input("Row: "))
                col = int(input("Col: "))

                while not is_valid(curr_map,(row,col)) or get_tile(curr_map,(row,col)) != 1:
                    print("Invalid Starting location, either in water or out of bounds")
                    print("Enter a starting location.\n")
                    print("The Top Left Corner is (0,0)\n")
                    print("The Bottom Right is ({0},{1})".format(len(curr_map)-1, len(curr_map[0])-1))

                    row = int(input("Row: "))
                    col = int(input("Col: "))

                explore_continent_user_pos(curr_map,row,col)
            else:
                print("There is no current map.")

        elif choice == "6":
            if curr_map:
                print("Starting at a random position")
                explore_continent_rand_pos(curr_map)
            else:
                print("There is no current map.")

        elif choice == "Q":
            print("Quit")
            quit = True


if __name__ == "__main__":
    main()