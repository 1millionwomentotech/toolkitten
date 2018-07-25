def continent_counter(world,x,y):
    if x<0 | y<0 | x>=n | y>=n :
        return 0

    if​ world[y][x] != ​'land'​
 ​   # Either it's water or we already counted it,​
 ​   # but either way, we don't want to count it now.​
 ​   return​ 0
  
    # So first we count this tile...​
    size = 1
    world[y][x] = ​'counted land'​
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    size = size + continent_counter(world, x-1, y-1)
    size = size + continent_counter(world, x , y-1)
    size = size + continent_counter(world, x+1, y-1)
    size = size + continent_counter(world, x-1, y )
    size = size + continent_counter(world, x+1, y )
    size = size + continent_counter(world, x-1, y+1)
    size = size + continent_counter(world, x , y+1)
    size = size + continent_counter(world, x+1, y+1)
    return size

​#sizeof world is n
n=5
world=[[0]*n for i in range n]
print(continent_counter(world, 5, 5))