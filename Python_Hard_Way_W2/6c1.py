#create a variable named "hilarious" and store inside it the string "False" (I don't think this is Boolean, is it?)
hilarious = False
#create a variable named "joke_evaluation" and store inside it the string "Isn't that joke so funny?!"" with one set of quotes as part of the string.
joke_evaluation = "Isn't that joke so funny?! {}" # 2)  String inside of a string #2 because the string has quotes around it. How come you don't have to format this string?

#..to show us the information contained in the variable joke_evaluation and when the user inputs ????????????
print(joke_evaluation.format(hilarious)) #The format "f-string" is used here to print it rather than to create the string containing the variable. Why??

