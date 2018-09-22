print("""You enter a dark room with two doors.
Do you go through door #1, door #2, door #3""")

door = input(">")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")
	print("3. Jump up and down.")
	print("4. Offer him a bigger cheesecake.")

	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	elif bear == "3":
		print("The bear cocks his head to the side, amused for a moment. Then he eats your arms off. Good job!")
	elif bear == "4":
		print("The bear accepts your offering and let's you live. Good job! It pays to travel with cheesecake.")

elif door == "2":
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")
	print("4. Rocking yourself into the unsleep of sleeps.")

	insanity = input(">")

	if insanity == "1" or "2":
		print("Your body survives powered by a mind of jello.")


	elif insanity == "3":
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")
	else:
		print("Never fall asleep or wake up again!")

elif door == "3":
	print("There's a a giant hole with a dangling rope, a ladder leading into a boat in the sky, and a bridge over a body of water.")
	print("What do you do?")
	print("1. Descend down the hole.")
	print("2. Climb the ladder.")
	print("3. Cross the bridge.")

	travel = input("> ")

	if travel == "1" or "3":
		print("You discover a land of rubies, parsnips, and marmelade prized and guarded by a species of dark-wink gladiator dragons. They are short one parsnips farmhand. Will you sign on? 1. Yes. 2. No.")
		farmhand = input("> ")
		if farmhand == "1":
			print("You live.")
		else:
			print("You die.")
	else:
		print("You discover the pirates headquarters on high. They are not too friendly. They kill you.")

else:
	print("You stumble around and fall on a knife and die. Good job!")





