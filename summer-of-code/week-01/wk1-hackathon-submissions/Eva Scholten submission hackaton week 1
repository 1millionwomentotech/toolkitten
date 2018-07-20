world = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#loop over each subarray and count all the 1s (land)
#check if the land tile has neighbours left, right and below and add +1 to cont1 if it does 

cont1 = 0
cont2 = 0

for i in range(len(world)):
  for j in range (len(world[i])):
    if world[i][j] ==1:
        if world[i][j] ==1 | world[i][(j+1)% len(world)] ==1 | world[i][j-1] ==1 | world[(i+1)% len(world)][j] ==1 | world[(i+1)% len(world)][j-1] ==1 | world[(i+1)% len(world)][(j+1)% len(world)] ==1:
            cont1 = cont1 + 1

print(cont1)
