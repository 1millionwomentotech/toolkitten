# Civilisation

# 1)Building the world

# a)collecting input and calculating the size of the world

length = input("How long you want your world to be: ")
length = int(length)
size = length*length

print ("Your world will have "+ str(size) +" tiles. Congratulations! Now you can start playing!")

# b)calculating random land(1)/water(0)

import random    
world=[]    
for i in range (size):    
    world.append(random.randint(0,1))    
print (world)  

#Calculating land (1)

land=0

for i in world:
    if i == 1:
    	land += 1
print (land)
	#else: 
print("Your world has "+ str(land) + " tiles. Awesome job!")




