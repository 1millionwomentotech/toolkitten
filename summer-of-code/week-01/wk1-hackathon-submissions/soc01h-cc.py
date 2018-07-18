#TODO:
#   further testing
#   generate random world of size nxn
#   benchmark (timeit module..?)
#   counting size of other continents, options:-
#       search function to find '1' (...allowed?)
#       linear search

import pdb

def continent_counter(world,indices):
    # pdb.set_trace()
    # print(''.join([str(i) for i in world])) #DEBUGGING
    count=0
    x=indices[0]
    y=indices[1]
    if(world[x][y]==1):
        world[x][y]=0 #already counted
        count=count+1
                
        # print(''.join([str(i) for i in world])) #DEBUGGING
        
        count += continent_counter(world,(x+1,y))
        count += continent_counter(world,(x+1,y-1))
        count += continent_counter(world,(x+1,y+1))
        count += continent_counter(world,(x,y-1))
        count += continent_counter(world,(x,y+1))
        count += continent_counter(world,(x-1,y))
        count += continent_counter(world,(x-1,y-1))
        count += continent_counter(world,(x-1,y+1))
        
    return count
    
    
my_world=[[0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0],
          [0,0,0,0,0,0,1,0,0,0,0],
          [0,0,0,1,0,0,1,0,0,0,0],
          [0,0,0,1,1,1,1,0,0,0,0],
          [0,0,0,1,1,1,1,1,0,0,0],
          [0,0,1,1,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0]]

ans=continent_counter(my_world,(5,5))
print(ans)
