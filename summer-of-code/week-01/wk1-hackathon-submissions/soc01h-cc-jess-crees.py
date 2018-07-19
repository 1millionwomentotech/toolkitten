# IMPORTS
from random import randint


# GLOBAL VARIABLES
world = []
current_tile_coords = []
land_counter = 0
continents = []


# FUNCTIONS
def generateWorld(size):
    for i in range(int(size)):
        world.append([])

        for j in range(int(size)):
            world[i].append(randint(0, 1))



def chooseRandomStartingTile():
    x = randint(0, int(world_size)-1)
    y = randint(0, int(world_size)-1)
    return [x, y]



def traverseMap(x, y, fill, default):
    global land_counter

    # Define the boundary values
    boundary = 2

    # if coords are outside of map boundaries, break out of function
    if x >= int(world_size) or y >= int(world_size) or x < 0 or y < 0:
        return

    # Check if current point is default colour, if it is then...
    if world[x][y] == default:
        # Change default colour to fill colour at current point
        world[x][y] = fill

        # Increase land counter
        land_counter = land_counter + 1
        
        # Call function recursively 8 more times to fill surrounding pixels
        traverseMap(x-1, y, fill, default)
    
        traverseMap(x+1, y, fill, default)
        
        traverseMap(x, y-1, fill, default)
        
        traverseMap(x, y+1, fill, default)
        
        traverseMap(x-1, y+1, fill, default)
        
        traverseMap(x+1, y+1, fill, default)
        
        traverseMap(x+1, y-1, fill, default)
        
        traverseMap(x-1, y-1, fill, default)



# STEP 1 - USER INPUT
world_size = input("How large is your world in squares? ")
print('\n')


# STEP 2 - GENERATE WORLD
generateWorld(world_size)

while '1' not in str(world):
    generateWorld(world_size)

# Show the world to the user
for i in range(int(world_size)):
    print(world[i])

print('\n')


while '1' in str(world):
    #STEP 3 - pick a random starting point
    current_tile_coords = chooseRandomStartingTile()

    while world[int(current_tile_coords[0])][int(current_tile_coords[1])] != 1:
        current_tile_coords = chooseRandomStartingTile()

    # STEP 4 - check world map
    # Initialise first point, fill tile, and target tile
    traverseMap(current_tile_coords[0], current_tile_coords[1], 2, 1)

    # Add land count to continents list
    continents.append(land_counter)

    # Reset land counter
    land_counter = 0


# STEP 6 - output continent ranking
continents.sort(reverse = True)

if len(continents) == 2:
    print("The largest 2 continents on this world are made up of " + str(continents[0]) + " land tiles and " + str(continents[1]) + " land tiles.")
else:
    print("The largest continent on this world is made up of " + str(continents[0]) + " land tiles.")

print('\n')
