# numbers to letters
# for i in range(1,256):
#     print(i, " stands for ", chr(i))

# #fix the above so it prints only A-Z and a-z


# a = "Elle J"
# b = "Sarah Alkhateeb"
# c = "Paula Bernal"
# d = "Melinda Gates"
# students = [a, b, c, d]

# print(students)

# sisters = ["Christina Tarantino", "Jesse RS", "alteredco", "LamboFantastico"]

# print(sisters)

# members = [students, sisters]

# print(members)

# # "LamboFantastico"
# print(members[1][3])


# world

M = 'land'
o = 'water'
world = [
         [o,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,M,o,M,M,o,o,o,o],
         [o,o,o,o,M,M,M,M,o,o,o],
         [o,o,o,M,M,M,M,M,M,M,M],
         [o,o,o,M,M,o,M,M,M,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]
        ]

def continent_counter(world, x, y):
    if world[y][x] != 'land':
        return 0

    size = 1
    world[y][x] = 'counted land'
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    # row above
    size = size + continent_counter(world, x-1, y-1)
    #print('first recursion size: ' , size)
    size = size + continent_counter(world, x  , y-1)
    size = size + continent_counter(world, x+1, y-1)

    # same row
    size = size + continent_counter(world, x-1, y  )
    size = size + continent_counter(world, x+1, y  )

    # row below
    size = size + continent_counter(world, x-1, y+1)
    size = size + continent_counter(world, x  , y+1)
    size = size + continent_counter(world, x+1, y+1)
    return size

print(continent_counter(world, 5, 5))
