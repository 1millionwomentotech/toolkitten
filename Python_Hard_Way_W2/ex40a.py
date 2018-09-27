class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

temptation_of_adam = Song(["Oh, I think about the \"Big One,\" W-W-I-I-I",
						   "Would we ever really care the world had ended?",
						   "You could hold me here forever like you’re holding me tonight",
						   "I think about that great big button and I’m tempted"])

temptation_of_adam.sing_me_a_song()



