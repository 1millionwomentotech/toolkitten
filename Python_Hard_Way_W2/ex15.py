from sys import argv

script, filename = argv

txt = open(filename) #the open command takes a parameter, in this case we passed in filename, and it can be set to our own variable.  Here, our own variable stores an open text file. Note to self: (filename) and not {filename} because filename is already a variable label created in line 3.

print(f"Here's your file {filename}:") 
print(txt.read()) #call a function on an opened text file named "txt" and that function we call is "read". We call "read" on an opened file. It returns a file and accepts commands.  ****You give a FILE a command using dot notation.

txt.close()

print("Type the filename again:")
file_again = input("> ") #sets user input received at prompt "> " equal to variable called "file_again" 

txt_again = open(file_again) #opens our sample txt file again and stores opened file in a variable called txt_again



print(txt_again.read())  #reads the file now stored under txt_again and prints it out again.

txt_again.close()

