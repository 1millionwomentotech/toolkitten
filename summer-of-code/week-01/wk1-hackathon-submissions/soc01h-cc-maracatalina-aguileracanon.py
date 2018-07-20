#Week1 Hackaton
from random import choice

# O for sea and x for land
choices = ['o','X']
num_of_continents = int(0)
size_continents = []
continen_counter=1
worldSize = input("How big do you want your world to be?")
worldSize = int(worldSize)
world = []
neighboorFound = True

for i in range (0,worldSize):
	world.append([" "] * worldSize)
	for j in range (0,worldSize):
		world[i][j] = choice(choices)
world[0][0] = '1'

def print_world(a_world):
	print("'X' represents land in the map")
	print("")
	for row in a_world:
		print (" ".join(row))
#world[1][8] = '♥' # es fila - columna
print_world(world)

#THis is a super nested method :( sorry

for num_of_continents in range(1,4):

	for amp in range (1,worldSize):


		for k in range(0,amp+1):
			if world[amp][k] =='X': 	 #Find if there are already identified nighbohrs 
					
					#Evaluate neiboohrs 
					for in_i in range (amp-1,amp+2):
						index_i = max(min(in_i,worldSize-1),0) #Clip value to prevent error in corners
						for in_j in range(k-1,k+2):
							index_j = max(min(in_j,worldSize-1),0)
							if world[index_i][index_j].isdigit():
								#print("Digit found")
								world[amp][k] = world[index_i][index_j]
								continen_counter=continen_counter+1
								#and then we fill the neighbors
								for in_i in range (amp-1,amp+2): #Range does not include maximum
									index_i = max(min(in_i,worldSize-1),0) #Clip value to prevent error in corners
									for in_j in range(k-1,k+2):
										index_j = max(min(in_j,worldSize-1),0)
										if  world[index_i][index_j] =='X': 
											world[index_i][index_j] = world[amp][k]
											continen_counter=continen_counter+1
								#neighboorFound=True
								break
							else :
								continue
						break
					if neighboorFound==False:
						if world[amp][k]=='X':
							world[amp][k]=str(num_of_continents)
							continen_counter=continen_counter+1
							for in_i in range (amp-1,amp+2): #Range does not include maximum
								index_i = max(min(in_i,worldSize-1),0) #Clip value to prevent error in corners
								for in_j in range(k-1,k+2):
									index_j = max(min(in_j,worldSize-1),0)
									if  world[index_i][index_j] =='X': 
										world[index_i][index_j] = world[amp][k]
										continen_counter=continen_counter+1
							neighboorFound=True	

			elif world[amp][k] == str(num_of_continents):
			#and then we fill the neighbors
				for in_i in range (amp-1,amp+2): #Range does not include maximum
					index_i = max(min(in_i,worldSize-1),0) #Clip value to prevent error in corners
					for in_j in range(k-1,k+2):
						index_j = max(min(in_j,worldSize-1),0)
						if  world[index_i][index_j] =='X': 
							world[index_i][index_j] = world[amp][k]
							continen_counter=continen_counter+1	


		for k in range(amp,-1,-1):
			if world[k][amp] =='X': 	 #Find if there are already identified nighbohrs 
					#Evaluate neiboohrs
					neighboorFound=False 
					for in_i in range (k-1,k+2):
						index_i = max(min(in_i,worldSize-1),0) #Clip value to prevent error in corners
						for in_j in range(amp-1,amp+2):
							index_j = max(min(in_j,worldSize-1),0)
							if world[index_i][index_j].isdigit():
								#print("Digit found")
								world[k][amp] = world[index_i][index_j]
								continen_counter=continen_counter+1
								for in_i in range (k-1,k+2): #Range does not include maximum
									index_i = max(min(in_i,worldSize-1),0) #Clip value to prevent error in corners
									for in_j in range(amp-1,amp+2):
										index_j = max(min(in_j,worldSize-1),0)
										if  world[index_i][index_j] =='X': 
											world[index_i][index_j] = world[k][amp]
											continen_counter=continen_counter+1
								#neighboorFound=True
								break
							else :
								continue
						break
					if neighboorFound==False:
						if world[k][amp] =='X':
							world[k][amp] = str(num_of_continents)
							continen_counter=continen_counter+1
							for in_i in range (k-1,k+2): #Range does not include maximum
								index_i = max(min(in_i,worldSize-1),0) #Clip value to prevent error in corners
								for in_j in range(amp-1,amp+2):
									index_j = max(min(in_j,worldSize-1),0)
									if  world[index_i][index_j] =='X': 
										world[index_i][index_j] = world[k][amp]
										continen_counter=continen_counter+1
							neighboorFound=True

			elif world[k][amp]==str(num_of_continents):
				for in_i in range (k-1,k+2): #Range does not include maximum
					index_i = max(min(in_i,worldSize-1),0) #Clip value to prevent error in corners
					for in_j in range(amp-1,amp+2):
						index_j = max(min(in_j,worldSize-1),0)
						if  world[index_i][index_j] =='X': 
							world[index_i][index_j] = world[k][amp]
							continen_counter=continen_counter+1
	neighboorFound=False
	size_continents.append(continen_counter)
	continen_counter=0
								





print_world(world)
#print(len(size_continents))
for z in range (0,len(size_continents)):
	print('Continent ' + str(z+1) + ' size: ' +str(size_continents[z]))
						











