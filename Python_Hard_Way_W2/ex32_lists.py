numbers = [4, 400, 5000]

print("Max Value Element: ", max(numbers))

animals = ["dogs", "crocodiles", "turtles"]

print(max(animals))

animals.append(["zebras"]) #adds the the list with one element "zebras" to the existing list as one object.

print(animals)

animals.extend("zebras")   #iterates through the string one character at a time and adds in this fashion

print(animals)

animals.append(["zebras, lions, tigers"]) #adds the list with three elements "zebras", "lions", "tigers" as one object to the existing list. Nested List.

print(animals)

animals.extend(["zebras, lions, tigers"])

print(animals)

animals.extend(["zebras", "lions", "tigers"])

print(animals)

print(animals.count(["zebras, lions, tigers"]))

animals.append(["crocodiles"])

print(animals)

animals.append("crocodiles")

print(animals)

print(animals.index("crocodiles"))

animals.insert(3, "penguins")

print(animals)

animals.pop(-1)

print(animals)

animals.reverse()

print(animals)

new_animals = [] 

for e in animals:
	if e not in ("z", "e", "b", "r", "a", "s"):
		new_animals.append(e)

animals = new_animals

print(animals)

animals = [e]

animals = [e for e in animals if e not in {"z", "e", "b", "r", "a", "s"}]







