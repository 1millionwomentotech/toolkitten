amount = 7
weekday = "Monday"
name = "jamey"
locomotion = "walks"
preposition = "on"
animal = "dogs"

def main():
    print("I am a working main function!")
    print("A whole lot of unnecessary lines of code and args to learn how functions call functions and what not but that's ok!")
    duty = walk_cart(name, locomotion, amount, animal, preposition, weekday)
    return duty


def walk_cart(name, locomotion, amount, animal, preposition, weekday):
    change = conversion(name, locomotion, amount, animal, preposition, weekday)
    return change
    

def conversion(name, locomotion, amount, animal, preposition, weekday):
    result = str(name) + str(locomotion) + str(amount) + str(animal) + str(preposition) + str(weekday)
    return result


print(main())
