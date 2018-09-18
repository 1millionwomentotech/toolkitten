types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who [do_not]." #interesting mistake--used brackets accidentally--they printed out--meaning only one 

print(x)
print(y)

print(f"I said: '{y}'")
print(f"I also said: '{y}'")

hilarious = cats #checking to see if a non-Boolean data type would work here, and nope! it doesn't, so the value FALSE functions as a Boolean!
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) 
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

print(f"Isn't that joke so funny?! {hilarious}") 