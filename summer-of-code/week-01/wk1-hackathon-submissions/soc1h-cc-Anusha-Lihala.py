import random
import time

def random_world_generator(n):
    """
    Generates a random world; a square board of size n x n containing 1s and 0s  
    
    Arguments:
    n -- dimensions of board 
    
    Returns:
    random_board -- 2d list of size n x n containing 1s and 0s  
    """
    random_board = [[random.randint(0,1) for j in range(n)] for i in range(n)]
    return random_board
    
def print_world(world):
    """
    Prints 2d list in tabular form
    
    Arguments:
    world -- 2d list containing 1s and 0s  
    """
    for row in world:
        print(row)

def continent_counter(world,indices):
    """
    Counts the size of the continent containing the row indices[0] and column indices[1]
    
    Arguments:
    world -- 2d list containing 1s and 0s  
    indices -- position within continent whose area is to be counted
    
    Returns:
    area -- size of continent
    """
    area=0
    x=indices[0]
    y=indices[1]
    if(world[x][y]==1):
        world[x][y]=0 #already counted
        area=area+1
                
        n=len(world)-1
        #calculating indices of neighbours
        if(x==0):
            x_values=[x,x+1]
        elif(x==n):
            x_values=[x-1,x]
        else:
            x_values=[x-1,x,x+1]
            
        if(y==0):
            y_values=[y,y+1]
        elif(y==n):
            y_values=[y-1,y]
        else:
            y_values=[y-1,y,y+1]
        
        for i in x_values:
            for j in y_values:
                area += continent_counter(world,(i,j))
        
    return area
    
def find_land(world):
    """
    Checks if there is any land in the world; if there is a 1 in the 2d list
    
    Arguments:
    world -- 2d list containing 1s and 0s  
    
    Returns:
    ans -- (-1,-1) if no land, position of land if there is land
    """
    ans=(-1,-1)
    for i,row in enumerate(world):
        if(1 in row):
            j=row.index(1)
            ans=(i,j)
            break
    return ans

def continents_counter(world,coordinates=None):
    """
    If coordinates given, finds area of corresponding continent else finds areas of all continents
    
    Arguments:
    world -- 2d list containing 1s and 0s  
    coordinates [Optional] - coordinates of land inside the continent whose area is to be found
    
    Returns:
    area -- size of continent(s); integer or dictionary
    """
    if(coordinates is None):
        count=1
        position = find_land(world)
        area={}
        while(position[0]>=0): #while there is still land
            current_area = continent_counter(world,position) #area of current continent
            current_name = 'continent'+str(count)
            count+=1
            area[current_name]=current_area           
            position=find_land(world) #find starting point for next continent
    else:
        area=continent_counter(world,coordinates)
        
    return area
    
def benchmarking(n):
    """
    Find average time taken to find area of all continents in a world of size nxn
    """
    sum=0
    for i in range(100):
        current_world=random_world_generator(n)
        
        time_before=time.time()
        for j in range(10):
            continents_counter(current_world)
        time_after=time.time()
        time_diff=time_after - time_before
        
        sum=sum+(time_diff/10)
        
    avg=sum/100
    return avg
    
#__________________________________MAIN_________________________________
print('Finding areas in a model 11x11 world.')
print('World:')
my_world=[[0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0],
          [0,0,0,0,0,0,1,0,0,0,0],
          [0,0,0,1,0,0,1,0,0,0,0],
          [0,0,0,1,1,1,1,0,0,0,0],
          [0,0,0,1,1,1,1,1,0,0,1],
          [0,0,1,1,1,0,0,0,0,0,1],
          [0,0,0,0,0,0,0,1,1,1,1],
          [1,1,0,0,0,0,0,1,1,1,0],
          [1,1,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,0]]
print_world(my_world) 
print(continents_counter(my_world))
print()

size=int(input('Enter size of new world: '))
print('Finding areas in a random ' + str(size)+'x'+str(size)+ ' world.')
print('World:')
world_random = random_world_generator(size)
print_world(world_random)
print(continents_counter(world_random))
print()

print('Average time taken to find areas =')
print(benchmarking(11),'seconds')
