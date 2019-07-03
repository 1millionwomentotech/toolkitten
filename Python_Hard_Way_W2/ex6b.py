types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary type thingies"
do_not = "don't know binary type thingies"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: '{y}'")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) 
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

print(f"Isn't that joke so funny?! {hilarious}")

#Below are experiments:

print(joke_evaluation) #This worked. It printed the literal string that was stored in this variable name. (ie, Isn't that joke so funny?! {})
print(joke_evaluation()) #I got this error: "TypeError: 'str' object is not callable" Can I infer that pg. 27 line 27--".format" is needed to convert joke_evaluation
# into a CALLABLE function and also tell it to grab the data stored in the variable name "hilarious"? Follow up question: Do the parentheses around hilarious tell
# it that or does the .format tell it that?


