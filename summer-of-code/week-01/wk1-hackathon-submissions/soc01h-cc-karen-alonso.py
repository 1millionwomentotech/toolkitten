#Hackaton 1
from random import randint

width = int(input('Tell me which WIDTH of continent do you want?'))
height = int(input('Tell me which HEIGHT of continent do you want?'))

continentSize = width * height

counterLand = 0
continent = []
subContinentSize = []
sizeContinent = 0


def CountContinents(continent, i, j):
	if continent[i][j] != 1:
		return 0

	size = 1
	aboveExist = True
	belowExist = True
	leftExist = True
	rightExist = True

	if i <= 0:
		aboveExist = False
	if i >= height - 1:
		belowExist = False
	if j <= 0:
		leftExist = False
	if j >= width - 1:
		rightExist = False

	continent[i][j] = 2

	#above
	size = size + (CountContinents(continent, i-1, j-1) if aboveExist and leftExist else 0)
	size = size + (CountContinents(continent, i-1, j) if aboveExist else 0)
	size = size + (CountContinents(continent, i-1, j+1) if aboveExist and rightExist else 0)

	#same row
	size = size + (CountContinents(continent, i, j-1) if leftExist else 0)
	size = size + (CountContinents(continent, i, j+1) if rightExist else 0)

	# #below
	size = size + (CountContinents(continent, i+1, j-1) if belowExist and leftExist else 0)
	size = size + (CountContinents(continent, i+1, j) if belowExist else 0)
	size = size + (CountContinents(continent, i+1, j+1) if belowExist and rightExist else 0)

	return size

print('My continent:')

for i in range (0, height):
	rowElements = []
	for j in range(0, width):
		value = randint(0, 1)
		rowElements.append(value)
		if value == 1:
			counterLand += 1

	print(rowElements)
	continent.append(rowElements)

for i in range (0, height):
	for j in range(0, width):
		sizeContinent = CountContinents(continent, i, j)
		if sizeContinent != 0:
			subContinentSize.append(sizeContinent)


print('Size of my world:')
print (continentSize)

print('Subcontinents and sizes')
for i in range (0, len(subContinentSize)):
	print('Subcontinent', i+1, ':', subContinentSize[i])

print('Total land size:')
print(counterLand)

print('Water size:')
print(continentSize - counterLand)
