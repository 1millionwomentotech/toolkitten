import numpy as np
import random

from pylab import *
from scipy.ndimage import measurements


row = 20;
col = 40;
#row =random.randint(0,100)  #row number
#col =random.randint(0,100)   #col number

matrix =np.random.randint(2, size=(row,col))

print(matrix)

#show matrix
import numpy as np
import matplotlib.pyplot as plt

plt.imshow(matrix);
plt.colorbar()
plt.show()

#earth area
earth = [];
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (matrix[i][j] ==1):
             earth.append(matrix[i][j])
             
print("earth area", len(earth))  

lw, num = measurements.label(matrix)

print('continents and its size, sorted')
area = measurements.sum(matrix, lw, index=arange(lw.max() + 1))
print(area)


#count continents
print("count continents",len(area)-1) 

#max continent
print("max continent area", area.max())

#two biggest continents
area.sort()
print("two biggest continents:", area[-1], area[-2])


#all continents area
print("all continents area", area.sum())
