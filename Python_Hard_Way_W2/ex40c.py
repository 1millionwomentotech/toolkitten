class Song(object):

	def __init__(self, lyrics, genre, artist):
	   self.lyrics = lyrics
	   self.genre = genre
	   self.artist = artist

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

to_the_dogs_or_whoever = Song(["The stain of the sepia the butcher Crimea",
							   "Through the wreck of a brass band I thought I could see her",
							   "In a cakewalk she came through the dead and the lame",
							   "Just another bird floating on a hurricane",

							   "I was flat on my back, my feet in the thorns",
							   "I was in between the apples and the chloroform",
							   "She came to me often, I was sure I was dying",
							   "It was always hard to tell if she was laughing or crying",

							   "I thought I heard somebody calling",
							   "In the dark I thought I heard somebody call",

							   "Joan never cared about the in-betweens",
							   "Combed her hair with a blade did the Maid of Orleans",
							   "Said Christ walked on water, we can wade through the war",
							   "You don't need to tell me who the fire is for"], "folk", "josh_ritter")

to_the_dogs_or_whoever.sing_me_a_song()

print(to_the_dogs_or_whoever.genre)

print(to_the_dogs_or_whoever.artist)
