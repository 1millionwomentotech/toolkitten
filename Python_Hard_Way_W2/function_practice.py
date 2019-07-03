from sys import argv

script, user_name = argv

print(f"Hi {user_name}, I'm the {script} script.")

prompt1 = 'name the friend you would like to be reminded to call: '

prompt2 = 'name the next friend you would like to call: '









#friends = ['sally on jan'+ str(1), 'marge on feb' + str(1), 'karen on mar' + str(1), 'audrey on apr' + str(1), 'delia on may' + str(1)]

friend1 = input(prompt1)

next_friend = input(prompt2)

friends = [friend1, next_friend, next_friend]


next_friend = input(prompt2) # at this point, why doesn't friend2 point to the new value input when input(prompt2) function is called for the second time and variable is reassigned?

def reminder(friends):
	print("I'd like to help you remember to stay in touch with your friends by creating a reminder schedule of whom to call when.")
	for friend in friends:
		print(f"call {friend}")
		
reminder(friends)






	

