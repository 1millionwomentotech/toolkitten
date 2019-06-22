import random


# Create grid
def create_row(w):
    line = [["O"] for i in range(w)]
    return line


def create_grid(h, w):
    grid = [create_row(w) for i in range(h)]
    return grid


# Add all cells surrounding the cell in question to a list
def cells_around(coord_y, coord_x, w, h, new_list):
    if (coord_y-1) >= 0:
        if (coord_x-1) >= 0:
            new_list.append([coord_y - 1, coord_x - 1])
            new_list.append([coord_y - 1, coord_x])
        if (coord_x+1) < w:
            new_list.append([coord_y - 1, coord_x + 1])
    if (coord_x-1) >= 0:
        new_list.append([coord_y, coord_x - 1])
    if (coord_x+1) < w:
        new_list.append([coord_y, coord_x + 1])
    if (coord_y+1) < h:
        if (coord_x-1) >= 0:
            new_list.append([coord_y + 1, coord_x - 1])
            new_list.append([coord_y + 1, coord_x])
        if (coord_x+1) < w:
            new_list.append([coord_y + 1, coord_x + 1])


# Find cells that are not occupied by continents, where new islands can be located, and add them to a list
def free_cells(field, h, w, free_list):
    for k in range(h):
        for j in range(w):
            if field[j][k] == ["O"]:
                surround_cells = []
                add = True
                cells_around(j, k, w, h, surround_cells)
                for m in range(len(surround_cells)):
                    if field[surround_cells[m][0]][surround_cells[m][1]] == ["X"] or field[surround_cells[m][0]][surround_cells[m][1]] == ["Y"]:
                        add = False
                if add:
                    free_list.append([j, k])


# Let's assume that the total area of two super continents is a random integer from 30 to 60.
two_continent_area = random.randint(30, 61)

# The minimum continent area is 15. Let's calculate area of the first continent
first_area = random.randint(15, two_continent_area+1)

# The area of the second continent shall be the rest of two_continent_area
second_area = two_continent_area - first_area

# The total area of islands shall be from 1 to 15

total_islands = random.randint(1, 16)


# Instantiate grid height x width
height = 11
width = 11

game_field = create_grid(height, width)

# Chose random start point for the first continent in the upper half of the field and start point
# for the second continent in the lower half of the field. We will have not less than 2 free tiles between these points
x1 = random.randint(0, int(width/2)-1)
y1 = random.randint(0, int(height/2-1))

x2 = random.randint((int(width/2)+1), width-1)
y2 = random.randint((int(height/2)+1), height-1)

# Put "X" and "Y" in each of the start points
game_field[y1][x1] = ["X"]
game_field[y2][x2] = ["Y"]

# First continent can never touch the second continent so let's make a list of "forbidden cells".
# We will check if these cells are within the grid
forbidden_cells = []
cells_around(y2, x2, width, height, forbidden_cells)

# Let's build the first continent
# The second tile of the first continent should be in the allowed_cells
allowed_cells = []
cells_around(y1, x1, width, height, allowed_cells)

while first_area > 0:
    # Delete all possible "X" from allowed_cells. Delete possible forbidden cells
    for i in range(len(allowed_cells)):
        if i < len(allowed_cells):
            if allowed_cells[i] == ["X"] or allowed_cells[i] == ["Y"]:
                del allowed_cells[i]
            if allowed_cells[i] in forbidden_cells:
                del allowed_cells[i]

    # Random cell to place next tile
    if len(allowed_cells) > 0:
        new_cell_num = random.randint(0, len(allowed_cells)-2)
        new_cell = allowed_cells[new_cell_num]
        # Replace with "X" and delete it from allowed_cells
        game_field[new_cell[0]][new_cell[1]] = ["X"]
        del allowed_cells[new_cell_num]
        # Add new cells to allowed_cells
        cells_around(new_cell[0], new_cell[1], width, height, allowed_cells)
        first_area -= 1
    else:
        break

# Let's build the second continent
while second_area > 0:
    # Delete all possible "X" from allowed_cells. Delete possible forbidden cells
    for i in range(len(forbidden_cells)):
        if i < len(forbidden_cells):
            if forbidden_cells[i] == ["X"]:
                del forbidden_cells[i]
            if forbidden_cells[i] in allowed_cells:
                del forbidden_cells[i]

    # Random cell to place next tile
    if len(forbidden_cells) > 0:
        new_cell_num = random.randint(0, len(forbidden_cells)-1)
        new_cell = forbidden_cells[new_cell_num]
        # Replace with "X" and delete it from allowed_cells
        game_field[new_cell[0]][new_cell[1]] = ["Y"]
        del forbidden_cells[new_cell_num]
        # Add new cells to allowed_cells
        cells_around(new_cell[0], new_cell[1], width, height, forbidden_cells)
        second_area -= 1
    else:
        break

# Instantiate an array for island cells and populate is with possible cells
free_cells_for_islands = []
free_cells(game_field, height, width, free_cells_for_islands)


# Let's put all islands on the map
while total_islands > 0 and len(free_cells_for_islands) > 0:
    random_cell_num = random.randint(0, len(free_cells_for_islands)-1)
    random_cell = free_cells_for_islands[random_cell_num]
    game_field[random_cell[0]][random_cell[1]] = ["Z"]
    del free_cells_for_islands[random_cell_num]
    total_islands -= 1

# Uncomment next two lines to print grid with two different continents and islands for testing
# for i in range(height):
#     print(game_field[i])

# To make area guessing more difficult let's convert all 'earth' tiles into "X"

for i in range(height):
    for j in range(width):
        if game_field[i][j] == ["Y"] or game_field[i][j] == ["Z"]:
            game_field[i][j] = ["X"]

# Print refactored grid
for i in range(height):
    print(game_field[i])

# Calculate the area of total land
total_land = 0
for i in range(height):
    for j in range(width):
        if game_field[i][j] == ["X"]:
            total_land += 1
print("Total area of the land is ", total_land)

# Calculate the area of a random cell
x3 = random.randint(0, width-1)
y3 = random.randint(0, height-1)

if game_field[y3][x3] == ["O"]:
    print("You're in the ocean!")
else:
    print("This is land!")
    count = 1
    count_new = 1
    game_field[y3][x3] = ["L"]
    while True:
        for i in range(height):
            for j in range(width):
                if game_field[i][j] == ["L"]:
                    surrounding = []
                    cells_around(i, j, width, height, surrounding)
                    for k in range(len(surrounding)):
                        if game_field[surrounding[k][0]][surrounding[k][1]] == ["X"]:
                            game_field[surrounding[k][0]][surrounding[k][1]] = ["L"]
                            count_new += 1
        if count == count_new:
            break
        else:
            count = count_new
    print("The area of your land is ", count_new)

