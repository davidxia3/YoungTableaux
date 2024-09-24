from random_shape import find_shape_distribution, random_shape
from random_tableau import random_tableau, recalculate_shape
from tableaux import empty_tableau, is_corner, select_random_cell, hook_walk, tableau_to_string
from schensted_insertion import schensted_insertion, find_shape, insertion, recording, generate_permutation
from has_interesting import has_interesting

import matplotlib.pyplot as plt


permutation = generate_permutation(5)

print(permutation)
print(has_interesting(permutation))