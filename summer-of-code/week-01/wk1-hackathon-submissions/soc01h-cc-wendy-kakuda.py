import numpy as np
# random land generator
civ_arr = ['#', '.']
civ_cont = np.random.choice(civ_arr, size=(11,11))
print(civ_cont)

# area of land
unique, counts = np.unique(civ_cont, return_counts = True)
land_sea_count = dict(zip(unique, counts))
print(land_sea_count)
land_area = str(land_sea_count['#'])
print("Total area of land = "+land_area)