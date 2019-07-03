

##########################
# code contributor: Yucian Hong   (Jul 19 2018)
#
# algorithm: at standing point, check all 8 surronding tiles.  After checking all tiles, mark them as visited to avoid revisit. 
#			 Then visit each surrounding land tiles recursively.  At the next standing point, repeat the same checking, marking, and 
#            visiting all surrounding land tiles.  The recursion branches out in depth first manner.
#
# code features: 1. calculate size of all continents in the world
#				 2. random world generator
#	 			 3. extension to n x n size worlds (max n~450.  n>=500 cause segmentation fault)
#
# program speed benchmarking          (1 algorithm)
#
#   n    vs.   execute time(s)        (average of 2 runs):
#
#   5            2.9
#	11			 1.6
#	40			 3.9
#	80			 2.4
#	100			 3
#	150			 8.1
#	200			 16.7
#	250			 25.1
#	300			 25.7
#	350			 46.2
#	400			 85.63
#	450			 114
#
#   execution time resembles exponential curve exp(n/100)
##########################

import sys
sys.setrecursionlimit(1000000) 

import time
start_time = time.time()

#initialize worlds
import numpy
size=input('input grid size in integer:')
#size=100
size=int(size)
world=numpy.zeros((size,size),dtype=int)
visited=numpy.zeros((size,size),dtype=int)


#randomly generate continents for 11 x 11 world
import random
random.seed(1)
for x in range (0,size-1):
    for y in range (0,size-1):
    	k=random.randrange(0,2,1)
    	world[x,y]=int(k)	
print('world')
print(world)
print('')


## recursive function to move to next tile
def mvnext(r,c):
	r=int(r)
	c=int(c)

	visited[r,c]=1

	#array to store land tiles
	arr=numpy.zeros(0,dtype=int)

	# check 8 surrounding tiles
	for i in range (r-1,r+2,1):
		for j in range (c-1,c+2): 

			if not (i==r and j==c):
				if ( 0<=i<size and 0<=j<size ):

					if (world[i,j]==1 and visited[i,j]==0):
						global counter
						counter=counter+1
						arr=numpy.append(arr,[i*size+j])
						visited[i,j]=1
					else:
						visited[i,j]=1

    # recursively visit surrounding land tiles
	for k in range(0,len(arr)):
		i = arr[k]/size
		j = arr[k]%size
		mvnext(i,j)




global counter

##check if any tile hasn't been visited in the worlds
visits_left=True
continent=1
trip=0

#initialize starting point at (0,0)
i=0
j=0
x_start=i
y_start=j

# if any tiles are unvisited in the world, move to next starting point and start visit recursively
while(visits_left==True):
	trip+=1
	#if new start point is unvisited, perform visit recursively
	if(visited[x_start,y_start]!=1):
			counter=int(0)
			print('')
			print('')
			print('trip ',trip,' at starting point = (',x_start,',',y_start,')')
			mvnext(x_start,y_start)
			if counter > 0:
				print('continent',continent,' size = ',counter)
				continent+=1
			else:
				print('no continent')
			print('visit record (visited=1, unvisited=0)')
			print(visited)
	#check if there's any unvisited tiles in the world
	visits_left=False
	for o in range (0,size):
		for p in range(0,size):
			if (visited[o,p]== 0):
				visits_left=True
				x_start=o
				y_start=p

	
print('')
print("execution time = %s seconds " % (time.time() - start_time))
print('')
