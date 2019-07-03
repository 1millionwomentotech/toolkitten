types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who [do_not]."

print(x)
print(y)

print(f"I said: '{y}'")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" #Do the curly braces say that the input from the user must be of data type var? Meaning a variable name must go 

print(joke_evaluation.format(hilarious)) #What is this in human language? I don't truly get the syntax here. I don't get this way of doing it yet!!!

#update: I think this is the format command from pre-Python3.6. The user passes in the argument

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

#try an alternative to line 17 that might work

print(f"Isn't that joke so funny?! {hilarious}") #oh yeah, small joys, this way worked, which makes sense to me as opposed to line 17!!!! (update: after our 
#conversation today, I think I'm understanding line 17 but I'm still trying to study line 14, 15, 17.)