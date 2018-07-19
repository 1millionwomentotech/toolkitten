import random

print ("Give a number of board size ")
n = int(input())

print("-------------------------------")

#make a board

a = [0] * n
for i in range(n):
    a[i] = ['+'] * n


#display a board as 2D_array, where + is a water, 0 is a land

density_of_land = random.randint(20,100)

for i in range(density_of_land):
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    a[x][y] = 0

print ('\n'.join(' '.join(map(str,each)) for each in a))

#sum lands
list_continents = []
area_continents = []

for i, e in enumerate(a):
    for j, ee in enumerate(e):
        if a[i][j] == 0:
            list_continents.append([i,j,0])

tmp_index = 1
for land in enumerate(list_continents):
    x = land[1][0]
    y = land[1][1]
    continent_index = land[1][2]
    i = land[0]
    #print(land)
    if continent_index == 0:
        list_continents[i][2] = tmp_index
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            newx = x+dx
            newy = y+dy
            if (dx == 0 and dy == 0):
                continue
            if (newx >= 0 and newx < n and newy >= 0 and newy < n):
                for j in range (i+1, len(list_continents)):
                    if newx == list_continents[j][0] and newy == list_continents[j][1]:
                        if list_continents[j][2] == 0:
                            list_continents[j][2] = list_continents[i][2]
                        else:
                            list_continents[i][2] = list_continents[j][2]
    tmp_index += 1

area_continents = [0]*len(list_continents)

for i in range(0, len(list_continents)-1):
    for land in enumerate(list_continents):
        if i == land[1][2]:
            area_continents[i] += 1

print("-------------------------------")

print("The largest land is: " + str(max(area_continents)))
