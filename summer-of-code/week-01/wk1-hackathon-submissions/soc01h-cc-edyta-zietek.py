civilization_world = [
    #0 1 2 3 4 5 6 7 8 9 10
    [0,0,0,0,0,0,0,0,0,1,0], #0
    [0,0,0,0,1,0,0,0,0,0,0], #1
    [0,0,0,0,1,0,0,0,1,0,0], #2
    [0,0,0,0,1,1,0,1,1,0,0], #3
    [0,0,0,1,1,1,0,1,0,0,0], #4
    [1,1,1,1,1,1,1,1,0,0,0], #5
    [0,0,0,0,1,0,0,0,0,1,0], #6
    [0,0,0,0,1,0,0,0,0,1,0], #7
    [0,0,0,0,1,0,0,1,1,1,0], #8
    [0,1,0,0,0,0,0,0,1,1,1], #9
    [0,0,0,0,0,0,0,0,0,0,0], #10
]
visitted = [[0 for x in range(11)] for y in range(11)] 
queue = [(5,5)]
continent_counter = 0

def civilization(x,y):
    global continent_counter, queue, visitted

    if visitted[x][y] == 1:
        return
    if civilization_world[x][y] == 0:
        return
    visitted[x][y] = 1

    continent_counter +=1

    if x<10:
        queue.append((x+1, y))
    if x>0:    
        queue.append((x-1, y))
    if y <10:
        queue.append((x, y+1))
    if y>0:
        queue.append((x, y-1))

while len(queue) > 0:
    x, y = queue.pop(0)
    civilization(x,y)

print(continent_counter)
