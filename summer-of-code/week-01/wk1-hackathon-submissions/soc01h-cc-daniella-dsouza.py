# ```
# soc01h-cc-daniella-dsouza.py
# ```
# Author : Daniella D'Souza
# Created : July 18th , 2018
# 1MWTT Week 1 Hackathon
#Next Steps - Encapsulate to a class
#              Add Unit Tests
# Last Updated - 08/09/18
# Results from benchmarking
# Continent Size        Time
# 

import random


#Instantly make your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you're done!



class Civilization():
    """Builds a randowm world that consists of continents and oceans.
       Given the coordinates of your location, is able to tell if you are on land or water"""
    
    def __init__(self, dim):
        print("Initializing class Civilization")
        self.dimension = dim
        self.land = []
        self.civilization = []
        self.final_continents = []
        
    def set_dimension(self,dimension):
        if dimension != 0:
            self.dimension = dimension
            
    
    def get_dimension(self):
        return self.dimension
    
    
    def build_world(self):
        """ A 2D worlds that consists of random cells that are either "W" or "L"""
        
        print("Generating a random world size {}".format(self.dimension))
        choices = ['W', 'L']
        
        row = []
        for j in range(self.dimension):
           
            row = [random.choice(choices) for i in range(self.dimension)]
                
            print(row)
                
            self.civilization.append(row)

        #print(self.civilization)

    
    def find_neighbors(self, tile_index, tile, continents):
        """Updates the collection of continents with new pieces of land discovered
           scans for neighbours
           A continent is a collection of tuples corresponding to coordinates of each tile

           Could be named better - Add tile to a continent
        >>> find_neighbors(tile_index, tile, land, continents)

        """
        # Iterate thru the Continents 
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
    
        for j, l in enumerate(self.land):
            merged = False
            if (j != tile_index):  # don't want to compare with itself 
                if ((abs(l[0] - tile[0]) < 2) and (abs(l[1] - tile[1]) < 2)):
                    # We are neighbors
                    # Check if l exists on a certain continent, do a lookup
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
            # I am a new continent Yeah!
            continents.append(current_continent)
                                                            
        return

    def discover_land(self):
        """Returns the individual tiles of land in the world.

        >>> find_land("WWWWLLLL","LLWWLLLL")
        [(0,0),(0,1),(0,2),(0,3),(1,2),(1,3)]"""
        
        row = []
        i = 0
        
        for i, row in enumerate(self.civilization):
            for j, c in enumerate(row):
                t = (i,j)
                if (c == "L"):
                    self.land.append(t)
        print("find_land()")
        return

    
    def find_continents(self):
        """find_continents returns a list of lists of land""

        >>>find_continents([(0,0),(0,1),(0,2),(1,0),(3,0)) returns list of two lists
        (0,0),(0,1),(0,2),(1,0) and (3,0)"""
        
        print("find_continents")
        
        continents = []
    
        for index, t in enumerate(self.land):
            self.find_neighbors(index, t, continents)

        continents.sort(key=lambda c:len(c), reverse = True)
        merged_continent = False
        merged = []

        for i, c in enumerate(continents):
            sub_continent = continents[i+1:]
            for j, d in enumerate(sub_continent):
                merged_continent = False
                for l in d:
                    if ((l in continents[i]) or self.is_neighbor(l ,continents[i])):
                        continents[i] = self.merge(continents[i], d)
                        #print(i, continents[i])
                        continents[j+1] = []
                        merged_continent = True
                    if (merged_continent == True):
                       break
    
        self.final_continents = [c for c in continents if len(c) > 0]
        print("The number of continents = {}".format(len(self.final_continents)))

    

     
    def find_continent(self, tile):
        for index, c in enumerate((self.final_continents)):
            if (tile in c):
                print("You are on a continent {} of size {} ".format(index, len(c)))
                return index
            
        print("You are in the ocean")
        return 0

    
    def merge(self, list1, list2):
        return list(set(list1 + list2))

    
    def is_neighbor(self, tile ,continent):
        for t in continent:
            if ((abs(t[0] - tile[0]) < 2) and (abs(t[1] - tile[1]) < 2)):
                return True

        return False
    
    def compare_programs(self):
        """ Contrast usage of lists with usage of arrays """
        print("Comparing programs")       


if __name__ == "__main__":

    print("In main")
    world = Civilization(11)

    # 1. Randomly generate Civilization III world.
    
    world.build_world()
    n = world.get_dimension()
    world.discover_land()
    
    world.find_continents()
    
    message = "Please enter a number between 1 and {} ".format(str(n)) 
    y = 0
    
    while (y < 1 or y > n):
        y = int(input(message))
    
    print("Let us assume you are standing on tile ({}, {})".format(y, y))

    
    world.find_continent((y-1, y-1))
