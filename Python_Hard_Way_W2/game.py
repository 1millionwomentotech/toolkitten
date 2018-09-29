from sys import exit
from random import randint
from textwrap import dedent



class Room(object)

	def enter(self):
		print("This room is not yet configured.")
		print("Subclass it and implement enter.")
		exit(1)


class Engine(object):

	def __init__(self, room_map):
		pass

	def play(self):


class Library(Room):

	def enter(self):
		pass


class StartRoom(Room):

	def enter(self):
		pass

class WallsHaveEyes(Room):

	def enter(self):
		pass

class BoobyTrapPast(Room):

	def enter(self):
		pass

class Manticore Lair(Room):

	def enter(self):
		pass

class Map(object):

	def __init__(self, start_room):
		pass

	def next_room(self, room_name):
		pass

	def opening_room(self):
		pass

real_map = Map('start_room')
real_game = Engine(real_map)
real_game.play()





	