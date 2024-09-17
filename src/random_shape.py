from schensted_insertion import generate_permutation, insertion, recording, schensted_insertion, find_shape
import itertools
import random


def find_shape_distribution(n):
    shapes = {}
    for permutation in itertools.permutations(range(n)):
        shape = find_shape(permutation)
        if shape not in shapes:
            shapes[shape] = 1
        else:
            shapes[shape] = shapes[shape] + 1
    return shapes


def random_shape(n):
    shapes = find_shape_distribution(n)
    elements = list(shapes.keys())
    weights = list(shapes.values())
    return random.choices(elements, weights=weights, k=1)[0]

