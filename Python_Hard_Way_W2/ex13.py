from sys import argv

script, cats, dogs, fish = argv #Ok, so these need to match up with the below (, script)..(, cats)..  but what does this have to do with the actual arguments you pass in? I passed in apple orange grape and it ran.

print("The script is called:", script) #are these in white saying basically--take input from user in the run command and let them pass in whatever argument names they want and store them in these white variable names in order? 

print("Your first variable is:", cats) #So For instance, I ran python3.6 ex13.py apple orange grape, so ex13.py gets stored under "script", apple gets stored under "cats", orange gets stored under "second", and grape gets stored under "third"?
print("Your second variable is:", dogs) #So far, do these parameters just give back the parameters (which are now stored)
print("Your third variable is:", fish)



#Experiments...

Favorite_tree = input("What's your favorite tree? ")
print(f"Your favorite tree is a {Favorite_tree}, right? ", cats)

#script, filename = argv
#print("Script:", script)  # Prints script name
#print("Filename:", filename)  # Prints the first argument

#filename = argv
#print("Filname:", filename)  # Prints something like ["my-script.py", "my-file.txt"]

#Here, argv is a list that is expected to contain two values: the script name and an argument. Using Python's unpacking notation, you can write

#script = argv[0]
#filename = argv[1]

#as

#script, filename = argv   argv is the data, the value (two values), which are being stored in 2 variables respectively called "script" and "filename"

# >>> a,b = ('Hello','World')
# >>> a
# 'Hello'
# >>> b
# 'World'
