print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} years old, {height} feet tall, and {weight} pounds.")

# #experiments...

Age = (input("How old are you?"))
print(Age)

#It worked! (Finally!)

Name = input("What is your name, please? ") # Look! You don't need the parentheses on the outside of input.
State = (input("What state do you live in? "))
Specialty_Years_Worked = int(input("How many years of experience in this industry do you have? "))
Total_Years_Worked = int(input("How many total years of work experience do you have? "))
Number_of_Relocations = int(input("How many times have you relocated? "))

print (Name)
print(State)
print(Specialty_Years_Worked)
print(Total_Years_Worked)
print(Number_of_Relocations)
print(Total_Years_Worked - Specialty_Years_Worked)

print(f"So your name is {Name}; you are from {State}; you've got {Total_Years_Worked} total years of work experience, {Specialty_Years_Worked} years of specialty experience, and you've relocated {Number_of_Relocations} times. You are a hot ticket, {Name} from {State}!!")