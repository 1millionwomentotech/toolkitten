import itertools
import numpy as np
from collections import Counter
from scipy.ndimage.measurements import label
LAND_PERCENT = 0.5


def find_largest_island(side):
    """Find all the continents in the world of a given size.
       Calculate their areas and return the largest one.
       The smallest possible world consists of 1 tile.
    """
    # Generate new world
    world = generate_world(side)
    # Use label to find all linked areas, including diagonally connected ones
    structure = np.ones((3, 3))
    labeled_world, islands_num = label(world, structure)
    # Join the rows of 2d grid and calculate islands' areas
    islands_area = Counter(i for i in list(itertools.chain.from_iterable(labeled_world)) if i != 0)
    print(world)
    # Calculate and return the area of the largest island
    # Return 0 if no land found
    if islands_area:
        islands_max = max(islands_area.values())
        print("There are", islands_num, "continents in this world.")
        print("Their sizes are:", ', '.join(str(e) for e in islands_area.values()))
        print("The size of the largest one is", islands_max)
        return islands_max
    else:
        print("No continents found in this world")
        return 0


def generate_world(side):
    """Create new world of a given size."""
    shape = (side, side)
    # Calculate the total number of tiles
    size = np.prod(shape)
    # Calculate the number of earth tiles given LAND_PERCENT constant
    land = int(round(size * LAND_PERCENT))
    # Create two arrays of 1s and 0s for earth/water
    ones = np.ones(land)
    zeros = np.zeros(size - land)
    # Link the arrays
    board = np.concatenate([ones, zeros])
    # Shuffle the board for random land distribution
    np.random.shuffle(board)
    # Create 2d grid
    result = np.reshape(board, shape)
    return result


# find_largest_island(1)
# find_largest_island(6)
# find_largest_island(13)
