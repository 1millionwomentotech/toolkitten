from sys import argv

script, first, second, third = argv #these 4 things with commas are argv broken down into 4 variables or placeholders
#names or labels have been given to portions of the data (argv--argument variable which gets assigned to 4 variables instead of 1 holding all)




print("The script is called:", script) # second argument (words in white) are the names of the variable or placeholders (when run at command line, python will print 
#your actual arguments passed in at the command line and you are the user with input. Your input are your arguments put in at command line, whatever they are named)
#pens, paper, erasers; apple, orange, banana, --User SPECIFIC arguments put in AT THE COMMAND LINE before the script runs. Use 

#input("put prompt question here")

# when you want to grab specific
#user input while the scripts is running vs before

print("Your first variable is:", first) 
print("Your second variable is:", second) 
print("Your third variable is:", third)



Name = (input("What's your name? "))
print(Name)
