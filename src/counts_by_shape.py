from random_shape import find_shape_distribution, random_shape
from random_tableau import random_tableau, recalculate_shape
from tableaux import empty_tableau, is_corner, select_random_cell, hook_walk, tableau_to_string
from schensted_insertion import schensted_insertion, find_shape, insertion, recording, generate_permutation
from has_interesting import has_interesting
from hook_length_formula import hook_length_product
from factorial import factorial

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sympy.utilities.iterables import partitions

n = 10
trials = 1000000
threshold = 0  


plot = np.zeros((n, n))

for j in range(trials):
    permutation = generate_permutation(n)
    if has_interesting(permutation):
        shape = find_shape(permutation)
        shapes = shape.split('-')
        for k in range(len(shapes)-1):
            length = int(shapes[k])
            for m in range(length):
                plot[n-k-1][m] = plot[n-k-1][m] + 1



right_most = 0
bottom_most = 0

for i in range(n):
    if plot[0][i] > threshold:
        right_most = i

for i in range(n):
    if plot[i][0] > threshold:
        bottom_most = i

furthest = max(right_most, bottom_most)

plot_subset = plot[:furthest, :furthest]

fig, ax = plt.subplots()
cax = ax.imshow(plot_subset, cmap='Blues', interpolation='nearest')

cbar = fig.colorbar(cax)

ax.set_xticks(np.arange(furthest))
ax.set_yticks(np.arange(furthest))

ax.grid(color='black', linestyle='-', linewidth=0.2)

ax.set_xlim(-0.5, furthest - 0.5)
ax.set_ylim(-0.5, furthest - 0.5)

plt.title(f'S_{n}')
plt.show()