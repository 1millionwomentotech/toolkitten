# 1mwtt Summer of Code Week 1 Hackathon
# Author: Paula Hoare
import random

# function: create_test_grid - creates my hard-coded 11 x 11 grid
# 1 = land, 0 = water
def create_test_grid() :
    mygrid = [[1,0,0,1,1,0,0,1,1,1,1]
             ,[1,0,0,1,1,0,0,0,1,0,1]
             ,[1,1,0,0,0,1,0,0,0,0,1]
             ,[0,0,0,0,0,0,0,1,0,0,0]
             ,[0,1,1,1,0,0,0,0,0,1,1]
             ,[0,1,1,1,1,0,0,0,0,1,0]
             ,[0,0,0,1,1,0,0,1,0,0,0]
             ,[0,1,0,0,0,0,0,0,0,0,1]
             ,[0,1,1,1,0,0,0,0,0,0,0]
             ,[0,1,0,1,0,0,0,0,0,0,0]
             ,[0,1,1,1,0,0,0,1,0,0,0]
             ]
    return mygrid

# function: create_grid - generates a grid of the specified size
# 1 = land, 0 = water
def create_grid(grid_size) :
    grid = list()
    i = 0
    while i < grid_size :
          row = list()
          j = 0
          while j < grid_size :
              # assign 0 or 1 to the cell
              row.append(random.randint(0,1))
              j = j + 1
          grid.append(row)
          i = i + 1
    return grid

# function: display_world - print out the world
def display_world(myworld) :
    for row in myworld :
        str_row = ' '
        for cell in row :
            str_row += (str(cell) + ' ')
        print(str_row)

# function: count_land_cells - count the number of land cells matching the specified map_num
def count_land_cells(myworld, grid_size, map_num=1) :
    num_land_cells = 0
    i = 0
    while i < grid_size :
        j = 0
        while j < grid_size :
            if myworld[i][j] == map_num :
                # we have land
                num_land_cells += 1
            j += 1
        i += 1
    return num_land_cells

# function find_continents and map them with numbers
# returns number of continents found
def find_continents(myworld, grid_size):
    start_numbering = 2 # start at 2 because 1 represents unmapped land
    i = 0
    map_num = start_numbering - 1
    # map the continents
    while i < grid_size :
        j = 0
        while j < grid_size :
            if myworld[i][j] == 1 :
                # we have found unmapped land
                # map the continent
                map_num += 1
                map_continent(myworld, grid_size, i, j, map_num)
            j += 1
        i += 1
    # reset the map numbers, so that 1 is the first continent
    i = 0
    while i < grid_size :
        j = 0
        while j < grid_size :
            if myworld[i][j] > 1 :
                myworld[i][j] -= 1
            j += 1
        i += 1
    # return number of continents found
    return map_num-1

# function: map_continent
# maps the continent containing the given coordinates
def map_continent(myworld, grid_size, i, j, map_num) :
    is_land = False
    if myworld[i][j] == 1:
        # we have land that has not yet been counted
        is_land = True
        # set cell to indicate that it has been counted
        myworld[i][j] = map_num
        # look for surrounding land
        # ... row above (i-1)
        if i > 0 :
            if j > 0 and myworld[i-1][j-1] == 1 :
                map_continent(myworld, grid_size, i-1, j-1, map_num)
            if myworld[i-1][j] == 1 :
                map_continent(myworld, grid_size, i-1, j, map_num)
            if j < (grid_size-1) and myworld[i-1][j+1] == 1 :
                map_continent(myworld, grid_size, i-1, j+1, map_num)
        # same row (i) left and right
        if j > 0 and myworld[i][j-1] == 1 :
            map_continent(myworld, grid_size, i, j-1, map_num)
        if j < (grid_size-1) and myworld[i][j+1] == 1 :
            map_continent(myworld, grid_size, i, j+1, map_num)
        # row below (i+1)
        if i < (grid_size-1) :
            if j > 0 and myworld[i+1][j-1] == 1 :
                map_continent(myworld, grid_size, i+1, j-1, map_num)
            if myworld[i+1][j] == 1 :
                map_continent(myworld, grid_size, i+1, j, map_num)
            if j < (grid_size-1) and myworld[i+1][j+1] == 1 :
                map_continent(myworld, grid_size, i+1, j+1, map_num)
    return is_land

# function display_continents: displays info about the continents
def display_continents(grid, grid_size, num_continents) :
    print('There are ',num_continents,' continents')
    c_num = 0
    while c_num < num_continents :
        c_num += 1
        print('Continent #',c_num,': Area = ',count_land_cells(grid,grid_size,c_num))

# start of code
print('Hello world, we start here...')

# First use a hard-coded 11 x 11 grid
print('Create my standard 11 x 11 grid')
grid11 = create_test_grid()
display_world(grid11)
num_land_cells = count_land_cells(grid11,11,1)
print('Number of land cells = ', num_land_cells)

# Find the area of the continent at given coordinates in the grid
print('\nTest with some predefined coordinates...\n')
# test_coords = [(0,0),(4,2),(0,10),(1,3),(10,1),(3,3),(10,10)]
test_coords = [(0,0),(4,2)]
test_num = 1
grid11_test = create_test_grid()
for coord in test_coords :
     print('*** Test ', test_num)
     continent_num = test_num + 1
     print('Find the continent containing the coordinates ',coord,' and map it with the number ',continent_num)
     map_continent(grid11_test,11,coord[0],coord[1],continent_num)
     display_world(grid11_test)
     continent_area = count_land_cells(grid11_test,11,continent_num)
     print('Area of continent at ',coord,' is ',continent_area,'\n')
     test_num += 1

# Find all the continents and their areas
print('\nNow find all the continents in our test grid...\n')
num_continents = find_continents(grid11,11)
display_world(grid11)
display_continents(grid11, 11, num_continents)
print('\nTest Grid DONE!\n')

grid_size = 7      # number of rows/cols in grid
print('Create a ',grid_size,' x ',grid_size,' grid with random land and water cells')
grid = create_grid(grid_size)
display_world(grid)
print('\nNow find all the continents...\n')
num_continents = find_continents(grid, grid_size)
display_world(grid)
display_continents(grid, grid_size, num_continents)
print('\nGenerated Grid DONE!\n')
