x = 'land'
o = 'water'
World = [[o,o,o,o,x,x,x,o,o,x,o], [x,x,x,o,o,o,o,x,x,o,o], [o,o,o,o,o,o,o,o,o,o,o], [x,x,x,x,x,x,x,x,x,x,o], [o,o,o,o,o,o,o,o,o,o,x], [o,x,o,x,o,x,o,x,o,x,o], [x,o,x,o,x,o,x,o,x,o,x], [o,o,o,o,o,o,o,x,x,x,x], [x,x,x,x,o,o,o,x,o,x,o], [x,o,x,x,x,x,x,x,x,x,o], [x,x,x,x,x,x,x,x,x,x,x]]

def land_size(world, x, y):
  if world[x][y] != 'land':
    return 0
  else:
    size = 1
    world[x][y] = 'counted land'
    rows = len(world)   
    cols = len(world[0])
    if (x-1) >= 0 and (y-1) >= 0 and (x-1) < cols and (y-1) < rows:
      size += land_size(world, x-1, y-1)
    if (x) >= 0 and (y-1) >= 0 and (x) < cols and (y-1) < rows:
      size += land_size(world, x, y-1)
    if (x+1) >= 0 and (y-1) >= 0 and (x+1) < cols and (y-1) < rows:
      size += land_size(world, x+1, y-1)
    if (x-1) >= 0 and (y) >= 0 and (x-1) < cols and (y) < rows:
      size += land_size(world, x-1, y)
    if (x+1) >= 0 and (y) >= 0 and (x+1) < cols and (y) < rows:
      size += land_size(world, x+1, y)
    if (x-1) >= 0 and (y+1) >= 0 and (x-1) < cols and (y+1) < rows:
      size += land_size(world, x-1, y+1)
    if (x) >= 0 and (y+1) >= 0 and (x) < cols and (y+1) < rows:
      size += land_size(world, x, y+1)
    if (x+1) >= 0 and (y+1) >= 0 and (x+1) < cols and (y+1) < rows:
      size += land_size(world, x+1, y+1)
    return size
    
print(land_size(World, 0, 4))   
        