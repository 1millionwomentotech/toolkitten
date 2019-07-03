from sys import argv
script, user_name = argv
prompt = "Can't sleep? "







def get_sleep():
	
	if sleep == "no":
		print(f"Try this: Find a comfortable place to sit, {user_name}, that's not where you sleep. Imagine a place you feel safe, happy, and carefree. Take 2 deep breaths. Drink in the scenery with your mind's eye. What does it look like? Are you outside or inside? What smells and sounds do you notice? Are you alone? What time of day is it? What's the weather like? What makes this place so relaxing? Take 2 more slow, deep breaths. Now try to come back slowly to your surroundings. Go back to bed and see how you do.")

	else: print(f"Good for you, {user_name}!")

sleep = input(prompt)





get_sleep()


print(f"{user_name} said {sleep} to sleeping.")