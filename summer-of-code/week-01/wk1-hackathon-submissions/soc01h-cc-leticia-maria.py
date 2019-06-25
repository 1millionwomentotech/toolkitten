import random


width = int(input("Width of the world: "))
height = int(input("Height of the world: "))
size = width * height

land_counter = 0

continent = []

for i in range(0, height):
	aux_list = []

	while len(aux_list) < width:
		random_int = random.randint(0,1)
		aux_list.append(random_int)
		if random_int == 1:
			land_counter += 1

	continent.append(aux_list)

print ''
print ('The size of the land is: {}'.format(land_counter))
print ''

for i in range(0, height):
	print continent[i]