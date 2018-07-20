"""
### SUMMER OF CODE -- WEEK 1 HACKATHON ###

This project was created as part of the 1MWTT Summer of Code Initiative --
https://1millionwomentotech.com/summerofcode1/ -- and contains a class representing a 
Civilization III style world. The class contains methods to determine the size of the
continent a 'player' is on, given the starting coordinates, as well as methods to list
the size and locations of all continents on the map, their geographical center. The class
also permits custom maps alongside a default map, used primarily for testing.

Also included, for demonstration purposes, are several instances of the class, along with 
some method calls. These samples will run automatically when the file is run.

Below -- the original problem description located at the SOC wk 1 repo
https://github.com/1millionwomentotech/toolkitten/blob/master/summer-of-code/week-01/wk1-hackathon-submissions/hackathon.md:

Task: Calculate the size of a continent you are standing on in your 11 x 11 world in 
Civilization III.

Bonuses for:
- calculate continent size for all continents in the world
- random world generator
- fastest program
- benchmarking
- extension of the problem to n x n size world

"""
import random

class CivIIIWorld:
    """A civilization-style world

    Attributes:
        width (int) -- optional -- default=11: The width of the map
        height (int) -- optional -- default=11: The height of the map
        amt_land (float) -- optional -- default=0.45: Proportion of map covered by land
        default (bool) -- optional -- default=False: Whether or not to use the default map
                ** Note: Selecting 'True' for default overrides other options
    """

    default_world = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, width=11, height=11, amt_land=.45, default=False):
        """
        Constructor Function for CivIIIWorld

        Parameters:
            width (int) -- optional -- default=11: The width of the map
            height (int) -- optional -- default=11: The height of the map
            amt_land (float) -- optional -- default=0.45: Proportion of map covered by land
            default (bool) -- optional -- default=False: Whether or not to use the default map
                    ** Note: Selecting 'True' for default overrides other options
        """
        self.width = width
        self.height = height
        self.amt_land = amt_land
        self.world = self.generate_custom_world() if default == False else self.default_world
        # Calculating continent size requires correct width and height of map...
        if default == True:
            self.width = 11
            self.height = 11
            self.amt_land = .45
        
        self.player_continent = 1
        self.player_location = []
        self.current_continent = []
        self.all_continents = []
        self.__checked = []



    def __str__(self):
        """
        Print a representation of the map, with 1 representing land and 0 for water
        """
        str = ""
        for i in range(self.height):
            str = str + f'{self.world[i]}\n'
        return str


    def print_world_details(self):
        """
        Print a representation of the map as well as information about the world.
        If the continent data has not been generated and the character not been placed,
        ask the user if they want to complete the board setup now.

        Note: It's also probably not a good idea to be asking the user for input as
        may happen here. I did it anyway because some of the setup that might normally
        be done automatically is suspended so that it's possible to call each method 
        (calculate_from_point, calculate_all_continents) separately.
        """
        print(self)
        if not self.all_continents or not self.player_location:
            response = input('Setup isn\'t complete -- collect continent data and ' +
                'place player now? (Y/N) ')
            if not response or response[0].lower() != 'y':
                return
            else:
                self.calculate_all_continents()
                self.place_player()
        print(f'\nThere are {len(self.all_continents)} continents on this world\n')
        print('Continent List:\n')
        for idx, item in enumerate(self.all_continents):
            print(f'Continent {idx + 1} -- Size {len(item)}\n{item}\n')
        print(f'Player position is {self.player_location} on Continent ' + 
                f'{self.player_continent + 1}')


    def generate_custom_world(self):
        """
        This will generate a custom world based off of the dimensions specified in
        instance construction
        """
        map = [ [1 if random.random() <= self.amt_land else 0 
                 for i in range(self.width)] for j in range(self.height) ]
        return map


    def calculate_from_point(self, x, y):
        """Given a point on a continent, return all the tiles on the continent
        
        Parameters:
            x (int): The x-coordinate of the landmass to be counted
            y (int): The y-coordinate of the landmass to be counted

        Returns:
            The list of tiles in the current continent

        Note: This should probably be a private method, but since the purpose of the
        exercise is to test this method specifically, I am exposing it.
        """
        location_list = self.__create_adjoining_tile_list(x, y)
        location_list.append([x, y]) # Make sure the continent includes the start point
        for tile in location_list:
            if tile not in self.__checked:
                self.__checked.append(tile)
                
                if self.world[tile[1]][tile[0]] == 1:
                    self.current_continent.append(tile)
                    self.calculate_from_point(tile[0], tile[1])
        return(self.current_continent)


    def calculate_all_continents(self):
        """
        Calculates the tile list for each continent in the world, and saves the
        lists in the instance variable all_continents.
        """
        self.__checked = []
        possible_coordinates = [[w, h] for w in range(self.width) 
                               for h in range(self.height) if self.world[h][w] == 1]

        for coordinate in possible_coordinates:
            self.current_continent = []
            continent = self.calculate_from_point(coordinate[0], coordinate[1])
            if continent:
                self.all_continents.append(continent)

        self.all_continents.sort(key=len, reverse=True)
        

    def place_player(self):
        """
        Attempts to place player on a large-ish continent, if there are any
        available. Otherwise, place player on the largest available continent.

        Note: It's also probably not a good idea to be asking the user for input as
        may happen here. I did it anyway because some of the setup that might normally
        be done automatically is suspended so that it's possible to call each method 
        (calculate_from_point, calculate_all_continents) separately.
        """
        if not self.all_continents:
            response = input('We need continent data to place player properly. \n' +
                             'Collect it now? (Y/N) ')
            if response and response[0].lower() == 'y':
                calculate_all_continents()
            else:
                return
        possible_continents = [continent for continent in self.all_continents 
                                if len(continent) > 7]
        if not possible_continents:
            try:
                possible_continents = self.all_continents[0]
            except:
                print('Can\'t place player -- no continents available!')
        self.player_continent = random.randrange(0, len(possible_continents))
        self.player_location = random.choice(possible_continents[self.player_continent])


    def __create_adjoining_tile_list(self, x, y):
        """
        Private helper method for creating a list of surrounding tiles, 
        given coordinates.
        """
        neighbors = [[tile_x, tile_y] for tile_x in range(x - 1, x + 2)
                                    for tile_y in range(y - 1, y + 2)]
        for neighbor in neighbors:
            if neighbor[0] == self.width:
                neighbor[0] = 0
            if neighbor[1] == self.height:
                neighbor[1] = 0
            if neighbor[0] == -1:
                neighbor[0] = self.width - 1
            if neighbor[1] == -1:
                neighbor[1] = self.height - 1
        return neighbors


def create_sample_worlds():
    """
    A set of example worlds to demonstrate the features of the CivIIIWorld class. The
    first world created uses the default settings, for testing purposes.
    """

    # Testing -- for default world ---
    # expect [6, 0] to be added to the larger 'east' continent
    # expect [3, 7] or [9, 5] (diagonals) to be included in respective continents
    # for default world:
        # expect that west continent has 22 tiles
        # expect that small east continent has 5 tiles
        # expect that west continent has 19 tiles

    print('\n########\nWORLD 1 - DEFAULT\n########\n')
    world1 = CivIIIWorld(default=True)
    print(f'Layout of map for World 1: {world1}')
    world1.calculate_from_point(1, 1)
    continent = world1.current_continent
    print(f'The continent that includes 1, 1 also is of length {len(continent)}\n' +
            f'and contains the following list of tiles: \n{continent}\n')
    world1.calculate_all_continents()
    world1.place_player()
    print("A more complete set of details for this world: \n")
    world1.print_world_details()

    # print('\n########\nWORLD 2\n########\n')
    # world2 = CivIIIWorld(15, 5, .5)
    # world2.calculate_all_continents()
    # world2.place_player()
    # world2.print_world_details()

    # print('\n########\nWORLD 3\n########\n')
    # world3 = CivIIIWorld(10, 30, .4)
    # world3.calculate_all_continents()
    # world3.place_player()
    # world3.print_world_details()


if __name__ == '__main__':
    create_sample_worlds()
