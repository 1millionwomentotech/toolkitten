def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

def divide(a,b):
	print(f"DIVIDING {a} / {b}")
	return a / b

	#We just defined 4 commands. They each take 2 arguments: a and b. 

print("Let's do some math with just functions!")

#Below, we call the functions we just defined and pass in 2 specific arguments. At the same time, we name them or label them.

age = add(30, 5)  # We call the function add with 30 passed in for the a parameter and 5 passed in for the b parameter. As such, we name this specific instance of adding these specific numbers "age."
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}") 


print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")




