""" 
    # Program to count the continent size on a 11 x 11 grid like the board of civilisation III.
    # Map class can be given two arguments height and width map(h,w) to set the size of the generated world to hxw. If no values are given this is set # to 11x11. 
    # Each square in the world is randomly assigned either land(1) or sea (0).
    # A continent is made from all land sqaures which connect (also diagonally).
    # The check_initial_coords() function starts the process to calculate the size of the continent you are standing on form randomly generated started point. If this start point is land it will continue to calculate the size of the continent, if it is water you will recieve a message.
"""
import random

class map():
    '''
    Class to build map of size height x width populated with 0 or 1
		
	Returns:
		Map as list.
	'''
    # world set to 11x11 unless specified to a nxn grid when class object called.
    def __init__(self, height = 11, width = 11):
        self.counter = 0
        self.continent = []
        self.height = height
        self.width = width
        self.world =  self.generate_map()
        self.X, self.Y = self.start_coords()
        self.next = 0
        
    def generate_map(self):
        '''
        Function to generate populated world.
            
        Returns: 
            Populated world.
        '''
        world = []
        # random generated world
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(random.randint(0,1))
            world.append(row)
        # hard code world for testing, comment out to use above world generator
        #world = [
        #   [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        #    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        #    [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        #    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        #    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        #    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        #    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        #    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        #    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        #    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        #    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        #]
        return world
        
    def start_coords(self):
        '''
        Function to set random starting co-ordinates.
            
        Returns: 
            Starting co-ordinates.
        '''
        X = random.randint(0,len(self.world)-1)
        Y = random.randint(0,len(self.world[0])-1)
        return(X, Y)
            
    def check_coords_valid(self, x, y):
        '''
        Function to check given co-ordinates are valid(within world).
            
        Returns:
            True if co-ordinates are valid.
            False if co-ordinates are invalid.
        '''
        if x >=0 and x < self.height and y >=0 and y < self.width:
            return True
        else:
            return False
    
    def check_coords(self, x, y):
        '''
        Function to check if given co-ordinates are land and not yet in the continent list.
            
        Returns:
            True if co-ordinates are valid.
            False if co-ordinates are invalid.
        '''
        if self.world[x][y] == 1 and [x, y] not in self.continent:
            # increment counter
            self.counter += 1
            # append co-ordinates to continent
            self.continent.append([x, y])
            return True
        else:
            return False

    def check_neighbours(self):
        '''
        Function to check co-ordinates of neighbour tiles and add them to the continent if they are land.
            
        Returns:
            Runs self.count function after going through neighbours.
        '''
        start_length = len(self.continent)
        neighbours = [
            [self.X-1, self.Y+1],
            [self.X-1, self.Y],  
            [self.X-1, self.Y-1],  
            [self.X, self.Y-1],  
            [self.X+1, self.Y-1],
            [self.X+1, self.Y],  
            [self.X+1, self.Y+1],
            [self.X, self.Y+1]
        ]
        
        for neighbour in neighbours:
            # check co-ordinates are valid
            if self.check_coords_valid(neighbour[0],neighbour[1]):
                # if co-ordinates are land(1) and not already in continent list add to list
                self.check_coords(neighbour[0],neighbour[1])
            # else:
                # print("not valid coords")
        self.next +=1
        self.count()

    def check_initial_coords(self):
        '''
        Function to check initial co-ordinates and whether they are land(1) or sea(0).
        
        Returns:
            If co-ordinates are land and not already in continent runs neighbours function.
            If co-ordinates sea or already in continent then increment on self.next by 1 and run self.count
        '''
        if self.check_coords(self.X, self.Y):
            self.check_neighbours()
        else:
            self.next += 1
            self.count()

    def count(self):
        '''
        Function to check all co-ordinates added to continent list.
        
        Returns:
            If initial square is in the sea, returns print statement saying so.
            If initial square is on land, return number of squares continent contains.
        '''
        if self.next < len(self.continent):
            self.X = self.continent[self.next][0]
            self.Y = self.continent[self.next][1]
            self.check_neighbours()
        elif self.counter == 0:
            print("Plop your in the sea, get to dry land!")
        else:
            print("Size of continent in squares: {}".format(self.counter))

if __name__ == '__main__':
    # make map object from class setting grid height and width
    map = map()
    # assign world from map object to variable
    world = map.world
    # print world out - for checking
    for row in world:
        print(row)
    # print starting co-ordinates - for checking    
    print("Starting co-ordinates: X = {}, Y = {}".format(map.X, map.Y))
    # run program to determine if your starting co-ordinates are on land or sea, and if land how many squares it covers
    map.check_initial_coords()

