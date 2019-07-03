def sent(craft_supply, clothing, travel_verb, place):
	print("I can make a silly sentence. See: \n")
	print(f"I put my {craft_supply} in my {clothing} and {travel_verb} to the {place} singing Skip-to-my-loo-My-Darling!\n")
	print(f"What a strange trip it's been!\n")

print("I'm calling my function for the first time.")
sent("glitter", "shoe", "flew", "laundromat")

confetti = "confetti and glitter bits"
pocket = "left shirt pocket"
chop = "choppered A-Team style"
ARS = "Antique Road Show"
miles = "miles"

print("I'm calling my function for the second time where I've now stored the value first in a global variable.")
sent(confetti, pocket, chop, ARS)

print("I'm calling my function for the third time and I'm going to use numbers as arguments instead of strings or variables.")
sent(20, 30, 40, 50)

print("I'm going to do some calculation within the arguments.\n")
sent(20 + 1, 30, 40 + 50, 50)

distance = 1000

print("I'm going to calculate using global variables and numbers, concatenate and convert int obj to str obj.")
sent(confetti, "shoe", chop  + " " + str(distance + 22) + " " + miles, ARS)

