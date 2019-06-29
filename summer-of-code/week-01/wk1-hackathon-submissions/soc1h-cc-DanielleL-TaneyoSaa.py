def count_world_size(n):
    ''' 
    Calculate the size of a continent 
    having n x n world in Civilization III.
    '''
    import random
    # x is for land, and o is for water
    
    L = [random.choice('XO') for _ in range(n)]
    L1 = [L for _ in range(n)]
    #print(L1)
    findx = len([i for lst in L1 for i in lst if i =='X'])
    return 'The size of all continents is: ' +  str(findx)
    
 print(count_world_size(11))   
