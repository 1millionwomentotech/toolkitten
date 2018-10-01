print("""You enter a dark room with two doors.
Do you go through door #1 which leads to a castle or door #2 that leads to an underwater mission?""")

door = input("> ")

if door == "1":

	print("There's a drawbridge that isn't open. What will you do to get across?")
	print("What will you do to get across?")
	print("1. Jump and hope you land in a window.")
	print("2. Throw throwing stars and hope you land on them to get to an open window.")
	print("3. Call for help and run back out the door.")

	drawbridge = input("> ")

	if drawbridge == "1":
		print("You land in the water. You find a secret passage.")
		print("Do you go through it or not?")
		print("1. Yes.")
		print("2. No.")

		secret = input("> ")

		if secret == "1":
			print("You see something light in the darkness. What would you like it to be?")
			print("1. Someone ready to pull you into the castle and help you.")
			print("2. An octopus ready to put tentacles on you so you can survive.")
			print("3. A glowing potion that give you the ability to turn you into a mermaid or merman and back whenever you want and still know how to swim like a mermaid or merman.")

			light = input("> ")

			if light == "1":
				print("A guard finds you and saves you by pulling you into the castle.")
				print("You become loyal and you win your family to the castle and you live happily ever after. The End!")
			elif light == "2":
				print("An octopus puts tentacles on you, brings you to Ursula, the wicked sea witch.")
				print("King Trident appears out of nowhere. You ask him for the Trident and he gives it to you.") 
				print("You blast Ursula and all of of your tentacles fall off and you swim home before you run out of oxygen.")
				print("You live happily ever after. The End!")

			else:
				print("You turn into a mermaid or merman. You swim to the castle.")
				print("You say to the guards,\'I have powers that can help you fight off bad guys!\'")
				print("You live at the castle and help protect the village and live happily ever after. The End!")

		else:
				print("You keep swimming and make the transition of human to mid fish. The End!")

	elif drawbridge == "2":
		   print("Good news! You land safely on a throwing star and whiz straight through an open window into a bedroom.")
		   print("On the pillow at the head of the bed, there is note. It reads:")
		   print("\'Enjoy your vacation! The castle is yours for the week. Ring the bell for service. Stanley, your personal butler, will be happy to help you with anything you need. The End!\'")

	else:
		print("An eagle hears your cry and carries you home. The eagle drops you safely in your bed. The End!")







else:

	print("You see a pufferfish. You puff up and explode and reform as a fish and get eaten by a shark and live happily ever after in the shark's belly.")
	print("The End!")



