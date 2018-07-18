#Hackaton 1
from random import randint

width = int(input('Tell me which WIDTH of continent do you want?'))
height = int(input('Tell me which HEIGHT of continent do you want?'))

continentSize = width * height

counterLand = 0
continent = []

print('My continent:')

for i in range (0, height):
	rowElements = []
	for j in range(0, width):
		value = (randint(0, 1))
		rowElements.append(value)
		if value == 1:
			counterLand += 1

	print(rowElements)
	continent.append(rowElements)

print('Size of my continent:')
print (continentSize)

print('Land size:')
print(counterLand)


print('Water size:')
print(continentSize - counterLand)