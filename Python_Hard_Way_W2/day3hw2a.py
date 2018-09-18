fav_num = int(input("What's your favorite number? ")) #stored user input and immediately converted it into an integer.

bet_num = fav_num + 1 #stored user input that has been converted to integer form and change it (in this case, added 1 to it.) #note: bet_num is an int by default
#and fav_num is an int thanks to line 1.

print(f"I can see the appeal of {fav_num}, but have you considered the even more attractive " + str(bet_num) + "? ") #print out something to show how user input changed,
#in this case, the number increases by 1. Also, learned to convert data types to concatenate. Also, practiced f-string formatting and using variables inside strings for fun.


#Note: In line 6, Ilona mentions, you can just do str(fav_num+1) and not store the variable for the changed user input (ie; better number) if it isn't needed for later. By order of operations, fav_num + 1 will execute before being converted into a string and then it can concatenate.