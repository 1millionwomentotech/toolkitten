# Hackathon- Wk 1
# By Katina Mooneyham
# File name: soc01h-cc-firstname-lastname.py
#
# Find the area of an 11 by 11 area, randomly tiled as water or land tiles. Assume each tile is 1 by 1 area. 1 Unit.
#
#
#  TODO: Create a 11 by 11 array. Use 1 as land, 0 as water. Count 1s. Test. ORIGINAL IDEA: Create 11 numpy arrays. Then stack them. Then count 1s in each array. Or a final array.
#
#  TODO: Create 1 random 11 by 11 array. Use 1 as land, 0 as water. Only count 1s that have other 1s touching them. Define continent as 1 that has at 
#        least one other 1 around it. Use numpy.random.randint(2, size = 11, 11)
#
#  TODO: Create a generator that does an N by N world. 
#
#  TODO: Create a world generator that does an N by X world. 
#
#  TODO: Make some logic to create the continents differently.
#
# EXAMPLE GRID
# =============================================================================
# continent = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# =============================================================================
#
# I had an earlier version that used recursion in my function. At lower height and width it was fine. But at higher levels, it got an Max recursion error.
# This version fixes that.
#
import numpy as np

# TODO: Add a place for user input to determine an N by X; tested and getting max recursion error in big grids.
#print('How big is the world?')

#wd, ht = int(input('Enter a width: ')), int(input('Enter a height: '))

wd, ht = 30,30 # This is where you set the variables for location on your grid (map)

cont_map = np.zeros((wd,ht))

curr_map = np.random.randint(2, size = (wd, ht))  # I chose to use the random numpy array

print("==============================================================")
print('Total of All Lands:', np.count_nonzero(curr_map)) # Print map for testing and visual
print('A basic map of land and water...')
print("==============================================================")

# for loop to walk across continent instead of walking down (so to the right)
for y in range(ht): 
    print(end= '\n')
    for x in range(wd):
        print(' ', end = '')		   
        print(curr_map[x, y], end = '')		   


# setting initial variables for use in function below
found_continent = []
current_continent_count = 0
current_continent = -1

# function for counting the whole continent and walking across the continent to find land and water
def count_whole_continent(x,y):
    # global variable so I can use variables declared outside the function
    # up is negative, left is negative, down is positive, right is positive 
    # with 0,0 being where you are at the moment
    global found_continent
    global cont_map

    found_land = []
    
    # setting the coordinates of the array
    ne_x, ne_y = 1, -1 # northeast
    e_x, e_y = 1, 0 # east
    se_x, se_y = 1, 1 # southeast
    s_x, s_y = 0, 1 #south
    sw_x, sw_y = -1, 1 # southwest
    w_x, w_y = -1, 0 # west
    nw_x, nw_y = -1, -1 #northwest
    n_x, n_y = 0, -1 # north
    
    
    # figuring out what to do when you have found land...
    if (x + ne_x) < wd and (y + ne_y) > -1 and  curr_map[x + ne_x, y + ne_y] == 1:
        found_continent[current_continent] += 1
        curr_map[x + ne_x, y + ne_y] = -1
        cont_map[x + ne_x, y + ne_y] = current_continent +1
        found_land.append((x + ne_x, y + ne_y))
    if (x + se_x) < wd and (y + se_y) < ht and curr_map[x + se_x, y + se_y] == 1:
        found_continent[current_continent] += 1
        curr_map[x + se_x, y + se_y] = -1
        cont_map[x + se_x, y + se_y] = current_continent +1
        found_land.append((x + se_x, y + se_y))
    if (y + n_y) > -1 and curr_map[x + n_x, y + n_y] == 1:
        found_continent[current_continent] += 1
        curr_map[x + n_x, y + n_y] = -1
        cont_map[x + n_x, y + n_y] = current_continent +1
        found_land.append((x + n_x, y + n_y))
    if (x + e_x) < wd and curr_map[x + e_x, y + e_y] == 1:
        found_continent[current_continent] += 1
        curr_map[x + e_x, y + e_y] = -1
        cont_map[x + e_x, y + e_y] = current_continent +1
        found_land.append((x + e_x, y + e_y))
    if (x + nw_x) > -1 and (y + nw_y) > -1 and curr_map[x + nw_x, y + nw_y] == 1:
        found_continent[current_continent] += 1
        curr_map[x + nw_x, y + nw_y] = -1
        cont_map[x + nw_x, y + nw_y] = current_continent +1
        found_land.append((x + nw_x, y + nw_y))
    if (x + sw_x) > -1 and (y + sw_y) < ht and curr_map[x + sw_x, y + sw_y] == 1:
        found_continent[current_continent] += 1
        curr_map[x + sw_x, y + sw_y] = -1
        cont_map[x + sw_x, y + sw_y] = current_continent +1
        found_land.append((x + sw_x, y + sw_y))
    if (y + s_y) < ht and curr_map[x + s_x, y + s_y] == 1:
        found_continent[current_continent] += 1
        curr_map[x + s_x, y + s_y] = -1
        cont_map[x + s_x, y + s_y] = current_continent +1
        found_land.append((x + s_x, y + s_y))
    if (x + w_x) > -1 and curr_map[x + w_x, y + w_y] == 1:
        found_continent[current_continent] += 1
        curr_map[x + w_x, y + w_y] = -1
        cont_map[x + w_x, y + w_y] = current_continent +1
        found_land.append((x + w_x, y + w_y))
    return found_land
        
        
# adding to the found_continent
for y in range(ht):
    for x in range(wd):
        if curr_map[x,y] == 1:
             found_continent.append(1)
             current_continent += 1
             curr_map[x,y] = -1
             cont_map[x,y] = current_continent +1
             check_next = count_whole_continent(x,y) #adding to last continent
             while check_next != []:
                 next_check = check_next.pop()
                 nxt_x, nxt_y = next_check
                 more_land = count_whole_continent(nxt_x, nxt_y)
                 for new_land in more_land:
                     check_next.append(new_land)


# printing the found_continent list      
print(end = '\n')
print("==============================================================") 
print()
print('The continents found are ', found_continent)

    
# Final map of continents
for y in range(ht): 
    print(end= '\n')
    for x in range(wd):
        print(' ', end = '')		   
        print(int(cont_map[x, y]), end = '')		   

print(end = '\n')
print("==============================================================") 
print('This is the final map listing ALL the FOUND continents')


# finding the biggest continents by finding the length of the list
found_continent.sort(reverse=True)
if len(found_continent) == 0:
    highest_continents = []
elif len(found_continent) == 1:
    highest_continents = [found_continent[0]]
else:
    highest_continents = found_continent[0:2]

# finding the total area of the biggest continents
total_area = 0
for continent in highest_continents:
    total_area += continent           

# printing out the largest continents and area

print("==============================================================")
print()
print('The largest continent(s): ',end = '')
if highest_continents == []:
    print('There were no continents. Welcome to water world!')
elif len(highest_continents) == 1:
    print(highest_continents[0])
else:
    print(highest_continents[0], ' and ', highest_continents[1])

print(end = '\n')


if highest_continents == []:
    print('')
else:
    print('The largest continent is ', highest_continents[0], ' units.')

print()
print('The total area of the largest land(s): ', total_area, ' units')

print()
print("==============================================================")