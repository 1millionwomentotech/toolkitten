fav_num = (input("What is your favorite number?"))
print("But have you considered the ever more illustrious " + str(int(fav_num) + 1) + "?!? You won't be disappointed! ")


 #Note1: in this version, fav_num is still being stored as a string. To store as an int, you would convert to int on line 1 when you create the variable. ie; var1=int(input("prompt: ")) not var1=(input("prompt: "))

 #Note2: Ilona mentioned noting that to achieve this goal no second variable is needed. If I wanted to use the better number later, then it would be necessary to create a second variable to store the changed user input. Here, I don't bother creating a variable. I just print it out and play with converting it using execution of operations, making sure I can do that well. (no f'strings here as in day3hw2a.py)