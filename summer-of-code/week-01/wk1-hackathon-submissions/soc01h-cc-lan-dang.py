import random
import datetime

size = 1

class NotPositiveError(UserWarning):
	pass
def check_positive_int(number):
	try:
		number = int(number)
		if number <= 0:
			raise NotPositiveError
		return True
	except ValueError:
		return False
	except NotPositiveError:
		return False
def get_right_input (inp, function):
	processed_input = inp
	while True:
		if function(processed_input):
			break
		processed_input = input("Error! Type again: ")
	return processed_input
def input_world():
	x = get_right_input(input("What's the x-length of this land? - "), check_positive_int)
	y = get_right_input(input("What's the y-length of this land? - "), check_positive_int)
	return {'x': int(x), 'y':int(y)}
def process_world (size):
	x_length = size['x']
	y_length = size['y']
	world_size = x_length*y_length
	coordinate = {'x': random.randint(0, x_length-1), 'y': random.randint(0, y_length-1)}
	world = []  
	for m in range(0, y_length):
		line = []
		for n in range(0, x_length):
			if random.randint(1, 2) is 1:
				line.append('#')
			else:
				line.append('.')
		world.append(line)
	world[coordinate['y']][coordinate['x']] = 'O'
	return {'world': world, 'coordinate': coordinate, 'size': world_size}

def compute_continent_size(world, x, y):
	if world[y][x] is "#" or world[y][x] is "O":
		global size
		if world[y][x] is "#":
			size +=1
		world[y][x] = "X" if world[y][x] is "#" else "O"
		if y > 0:
			compute_continent_size(world, x, y-1)
		if y < len(world) -1:
			compute_continent_size(world, x, y+1)
		if x > 0:
			compute_continent_size(world, x-1, y)
		if x < len(world[0]) -1:
			compute_continent_size(world, x+1, y)
		if y >0 and x>0:
			compute_continent_size(world, x-1, y-1)
		if y > 0 and x < len(world[0])-1:
			compute_continent_size(world, x+1, y-1)
		if y < len(world)-1 and x >0:
			compute_continent_size(world, x-1, y+1)
		if y < len(world)-1 and x < len(world[0])-1:
			compute_continent_size(world, x+1, y+1)

def app_manual_version():
	input_size = input_world()
	world_dict = process_world(input_size) 
	compute_continent_size(world_dict['world'],world_dict['coordinate']['x'], world_dict['coordinate']['y'])
	print('='*60)
	print(' '*5 + "WORLD MAP")
	print('='*60)
	print(' '*5 + "Symbols used")
	print(' '*5 + ".: water")
	print(' '*5 + "#: land")
	print(' '*5 + "X: land of continent I'm standing on")
	print(' '*5 + "O: where I'm standing")
	print('='*60)
	for line_of_world in world_dict['world']:
		print(' '*5, end="")
		for tile in line_of_world:
			print(tile, end="")
		print()
	print('='*60)
	print('Size of world: ', world_dict['size'])
	print('Current Coordinate: (',world_dict['coordinate']['x']+1,',',world_dict['coordinate']['y']+1,')')
	print('Size of standing continent: ', size)

def app_automatic_version(x_length, y_length):
	start_time = datetime.datetime.now()
	global size
	world_dict = process_world({'x': x_length, 'y': y_length})
	compute_continent_size(world_dict['world'],world_dict['coordinate']['x'], world_dict['coordinate']['y'])
	print('='*60)
	print(' '*5 + "WORLD MAP")
	print('='*60)
	print(' '*5 + "Symbols used")
	print(' '*5 + ".: water")
	print(' '*5 + "#: land")
	print(' '*5 + "X: land of continent I'm standing on")
	print(' '*5 + "O: where I'm standing")
	print('='*60)
	for line_of_world in world_dict['world']:
		print(' '*5, end="")
		for tile in line_of_world:
			print(tile, end="")
		print()
	print('='*60)
	print('Size of world: ', world_dict['size'], '(', len(world_dict['world'][0]), 'x', len(world_dict['world']), ')')
	print('Current Coordinate: (',world_dict['coordinate']['x']+1,',',world_dict['coordinate']['y']+1,')')
	print('Size of standing continent: ', size)
	size = 1
	elapsed = datetime.datetime.now() - start_time
	print("--- %s ms ---" % (int(elapsed.total_seconds()*1000)))

def final():
	app_automatic_version(11, 11)
	while True:
		print("Do you want to test further?")
		answer = input("Enter 1 for Automatic Test; 2 for Manual Test; 0 to quit - ")
		if answer is "1":
			app_automatic_version(random.randint(5, 60), random.randint(5, 60))
		elif answer is "2":
			app_manual_version()
		elif answer is "0":
			break
		else:
			print("The input is invalid. Try again.")
		print('\n\n')
final()