from sys import argv

script, user_name, fav_ice = argv
prompt = '> '

print(f"Hi {user_name}, who likes {fav_ice} icecream. I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name} who likes {fav_ice} icecream?")
likes = input(prompt)

print(f"Where do you live {user_name} who likes {fav_ice} icecream?")
lives = input(prompt)

print(f"What computer do you have?")
computer = input(prompt)



print("""                     
Alright, so ignore this part because I'm practicing spacing here. you said blah blah blah about liking me.
You live in blah-no variables used here in this string. Not sure where that is. 
And you have a blah blah blah computer. Nice. Let's keep going here.
""")
#Note: I tried the exercise without the f-string to see if the empty string triple quote thing in line 17 would still keep lines 18-20 separate. It worked!

print(f"""
{user_name}, let me get this straight. You said {likes} about liking me.
You really like {fav_ice}.
You live in {lives}, which I don't know too much about.
You have a {computer}.
I think I'm starting to learn just a little bit about you.
""")
