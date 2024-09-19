from random_shape import find_shape_distribution, random_shape
from random_tableau import random_tableau, recalculate_shape
from tableaux import empty_tableau, is_corner, select_random_cell, hook_walk, tableau_to_string
from schensted_insertion import schensted_insertion, find_shape, insertion, recording, generate_permutation

import matplotlib.pyplot as plt


counts = {}

shape_dist = find_shape_distribution(4)
for i in range(100000):
    tableu = random_tableau(4, shape_dist)
    s = tableau_to_string(tableu)
    if s not in counts:
        counts[s] = 1
    else:
        counts[s] = counts[s] + 1

print(counts)

categories = list(counts.keys())
frequencies = list(counts.values())

plt.figure(figsize=(10, 6))
plt.bar(categories, frequencies, color='skyblue')

plt.title('Frequency of Each Category')
plt.xlabel('Categories')
plt.ylabel('Frequency')

plt.show()


