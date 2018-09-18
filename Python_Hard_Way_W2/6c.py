#We want to contain the integer 10 which has a memory address. We created a variable called "types_of_people" to contain or point to the integer (or memory address).
types_of_people = 10
#We want to contain a string that includes a variable so we must format the string using "f-string". We create a variable called "x" which contains the string which contains the variable.
x = f"There are {types_of_people} types of people." 

#We want to store the string "binary" inside a variable. We call the variable "binary."
binary = "binary"
#We want to store a string "don't" inside a variable. We call the variable "don't."
do_not = "don't"
# We want to store a string with the two above variables inside it. (We must of course format it using "f-string"). We name the variable "y".



y = f"Those who know {binary} and those who {do_not}."  #1, #2  NOTE: y is NOW converted into a single string. **********



#We tell python to use its built-in function "print" to show us the information that x contains.
print(x)
#We tell python to use its built-in function "print" to show us the information that y contains.
print(y)


#...to show us the the string "I said: {except in between the curly braces instead of "x" itself please show me what's actually stored inside x}
print(f"I said: {x}")
#  ditto goes for the string with the variable y...


print(f"I also said: '{y}'") # 3 because y is converted but the quotes around the curly braces have not been yet. ******



#create a variable named "hilarious" and store inside it Boolean data type (false)
hilarious = False  #  While this is a Boolean here, in order for the .format() syntax to be applied to to an already-created string like in the instance below, 
#it must first be converted to a string internally.  What is the point of having Boolean data here if you are going to convert it to a string format? What is the point 
#of creating a variable to store here if it only needs to remember one short thing? When you have many, it makes it easier to remember what is in each?


#create a variable named "joke_evaluation" and store inside it the string "Isn't that joke so funny?!"" with one set of quotes as part of the string.



joke_evaluation = "Isn't that joke so funny?! {}" 

print(joke_evaluation.format("no"))

#..to show us the information contained in the variable joke_evaluation and when the user inputs ????????????
#print(joke_evaluation.format(hilarious))
#"Isn't that joke so funny?! False"

# We set a variable that is a string with quotes around it equal to w (or name it w).
w = "This is the left side of..." #3) This is a string inside of a string.
#...ditto for the string here, but we name it e.
e = "a string with a right side." #4) This is a string inside of a string.

print(w+e)



#No = "Not at all"
#print(joke_evaluation.format(No))
#"Isn't that joke so funny?! no



