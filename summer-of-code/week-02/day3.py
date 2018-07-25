# Week 2 Day 3

import gc

# # dictionary Constructor

# anne_niekrenz = dict(name = "Anne anne_niekrenz", discord_id = "anne", fav_food = "ice cream")

# print(anne_niekrenz)

# my_dict = {
#     "a": 35000,
#     "b": 8000,
#     "z": 450
# }

# print(my_dict)

# # access
# print(my_dict["a"])

# # add
# my_dict["Rocio"] = "pretty"
# print(my_dict["Rocio"])
# print(my_dict)


# # modify
# my_dict["a"] = 50
# print(my_dict["a"])
# print(my_dict)

# # delete item
# print(len(my_dict))
# del(my_dict["a"])
# print(my_dict)
# print(len(my_dict))

# # delete dictionary
# del(my_dict)
# print(my_dict)

# CLASSES

# class Student():
#     discord_id = "yesvirginia [Gold] [Volunteer]"

# # instantiate using our shiny new Constructor function that we got for 'free' from the Class

# s1 = Student()
# s2 = Student()
# s3 = Student()
# # dot notation
# print(s1.discord_id)
# print(s2.discord_id)
# print(s3.discord_id)

# class Student():
#     def __init__(self, firstname, lastname, email, country_code, phone_number, github, country, discord_id, fav_food, dream):

class Student():
    def __init__(self, name, discord_id, fav_food, dream):
        self.name       = name
        self.discord_id = discord_id
        self.fav_food   = fav_food
        self.dream      = dream

    def my_print(self):
        print(self.name + " " + self.discord_id + " " + self.fav_food + " " + self.dream)

    #courtesy of Deb Cupitt's great question!
    def my_iter(self):
        for attr, value in self.__dict__.items():
            print(attr, value)

# instantiate using our shiny new Constructor function that we got for 'free' from the Class

s1 = Student("Virginia Balseiro", "yesvirginia [Gold] [Volunteer]", "pasta", "moving to Europe")

s2 = Student("Deb Cupitt", "deb[Gold]", "chocolate", "gender equity")

s3 = Student("Marta Bodojra", "marta [Gold] [Volunteer]", "dark chocolate", "become a developer and help all of you to do it together!😉")

# for attr, value in s1.__dict__.items():
#     print(attr, value)

# s1.my_iter()

for obj in gc.get_objects():
    if isinstance(obj, Student):
        obj.my_print()

# s2 = Student("Andreea[Gold]")

# s3 = Student("​CristyTarantino[Gold]")

# dot notation
# print(s1.name)

# s1.my_print()

# s1.fav_food = "ice cream"

# s1.my_print()

# delete properties

# del s1.fav_food
# s1.my_print()
# you will error out because my_print() will try to access a non-existant property/attribute

# del s1

# print(s1)
# s1.my_print()

# print(s2.discord_id)
# print(s3.dream)










