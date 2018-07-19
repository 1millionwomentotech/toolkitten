#1st-hackathon-civilisation

# create a random World generator

import numpy as np
import random
import matplotlib.pyplot as plt

matrix = np.random.randint(2, size=(11,11))

matrix
array([[0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
       [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
       [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
       [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
       [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
       [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
       [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
       [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]])

# identify the continents when you can travel diagonally

import scipy
from scipy.ndimage import measurements


s = [[1,1,1], [1,1,1], [1,1,1]] # this generates a structuring element that will consider features connected even if they touch diagonally

labeled_array, num_features = measurements.label(matrix, structure=s)

print(num_features) # this prints a number of randomly generated continents
5 

print(labeled_array) # this labels and prints clusters that connects diagonally. For instance, we can see that Continent No 5 is actually an island.
[[0 0 0 0 1 0 1 1 0 1 0]
 [1 1 1 1 0 1 1 1 1 1 0]
 [0 1 1 0 1 1 1 1 0 0 1]
 [1 1 0 1 1 0 0 0 1 1 1]
 [0 0 0 1 1 1 1 0 0 1 1]
 [0 0 1 0 0 0 1 1 0 0 0]
 [1 1 1 0 0 0 0 1 0 0 2]
 [1 1 1 0 0 3 0 1 1 0 0]
 [1 1 1 0 0 0 0 0 0 0 4]
 [0 1 0 1 1 0 1 0 5 0 4]
 [1 1 0 0 0 1 1 0 0 0 4]]


 # finally I created a loop which calculates the size of each continent

 continent = 1
 while continent < (num_features+1):
    result = (labeled_array == continent).sum()
    print(result)
    continent += 1

56
1
1
3
1