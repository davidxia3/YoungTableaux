from random_shape import find_shape_distribution, random_shape
from random_tableau import random_tableau, recalculate_shape
from tableaux import empty_tableau, is_corner, select_random_cell, hook_walk, tableau_to_string
from schensted_insertion import schensted_insertion, find_shape, insertion, recording, generate_permutation
from has_interesting import has_interesting

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

n = 60
trials = 100000
start = 2

ns = np.arange(start, n + 1)
counts = []

for i in range(start, n + 1):
    count = 0
    for j in range(trials):
        permutation = generate_permutation(i)
        if any(t[1] == 0 for t in has_interesting(permutation)):
            count += 1
    counts.append((trials - count) / trials)

counts = np.array(counts)


log_counts = np.log(counts)
log_ns = np.log(ns)

a, b = np.polyfit(log_ns, log_counts, 1)
print(a)
print(b)
print(np.e**b)

y_intercept = b 

x_min = 0  
x_max = np.max(log_ns) 
y_min = a * x_min + b 
y_max = a * x_max + b  

plt.figure(figsize=(10, 6))
plt.plot([x_min, x_max], [y_min, y_max], color="red", label=f'Slope: {a:.4f}, Intercept: {b:.4f}')
plt.scatter(log_ns, log_counts, label='log(Counts)', color='blue', marker='o') 

plt.title(f'Linear Fit of log(P_boring) vs. log(n)')
plt.xlabel('log(n)')
plt.ylabel('log(Counts)')

plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')

ax = plt.gca()
ax.spines['left'].set_position('zero') 
ax.spines['bottom'].set_position('zero') 
ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')

plt.legend()
plt.grid()
plt.savefig('figures/boring_first_column.png')
plt.show()
