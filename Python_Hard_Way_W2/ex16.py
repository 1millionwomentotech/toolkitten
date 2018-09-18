from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (>C).")
print("If you do want that, hit RETURN.") #print statement doesn't ask for input. Only to hit the return key, which is what you would normally hit after entering user input. (or quit python--already built in--ctrl c)

input("?")

print("Opening the file...")
target = open(filename, 'w')  #calls open and passes in the parameter filename and write mode and stores the opened file in write mode in the variable "target".

print("Truncating the file. Goodbye!")
target.truncate() #erased my whole file (no parameters) which said "This is a test file" or something like that

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") #stores user input under these variable names: line1, line2, line3. Uses prompt: line 1:, line 2:, line 3::
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1) #write to the file, pass in the parameter line1--writes line 1 to the file.
target.write("\n")  #write to the file, pass in the parameter new line, goes to next line
target.write(line2) #...etc
target.write("\n") 
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() #closes opened file which is in write mode

