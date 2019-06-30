# Hackathon 1 the CIV 3 Problem
X = "Land"
W = "Water"

world = [
  [ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],
  [ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],
  [ W ],[ W ],[ W ],[ X ],[ W ],[ W ],[ W ],[ X ],[ W ],[ W ],[ W ],
  [ W ],[ W ],[ X ],[ X ],[ X ],[ W ],[ X ],[ X ],[ X ],[ W ],[ W ],
  [ W ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ W ],
  [ W ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ W ],
  [ W ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ X ],[ W ],
  [ W ],[ W ],[ W ],[ X ],[ X ],[ X ],[ X ],[ X ],[ W ],[ W ],[ W ],
  [ W ],[ W ],[ W ],[ W ],[ X ],[ X ],[ W ],[ W ],[ W ],[ W ],[ W ]
  [ W ],[ W ],[ W ],[ W ],[ W ],[ X ],[ W ],[ W ],[ W ],[ W ],[ W ],
  [ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ],[ W ]
]

sorted_world = sorted(world)
i = 0
landmass = 0
while (i<121):
  if (sorted_world[i]) == ["Land"]:
    landmass+=1
  i+=1

print("The land has " + str(landmass) + " pieces.")

