from tableaux import empty_tableau, is_corner, select_random_cell, hook_walk, tableau_to_string
from random_shape import find_shape_distribution, random_shape

def recalculate_shape(empty, corner):
    row = corner[0]
    if len(empty[row]) == 1:
        empty.pop(row)
    else:
        empty[row].pop()
    return empty



def random_tableau(n):
    shape = random_shape(n)
    empty = empty_tableau(shape)

    tableau = empty_tableau(shape)

    for i in range(n, 0, -1):
        position = select_random_cell(empty)

        while not is_corner(empty, position):
            position = hook_walk(empty, position)
    
        tableau[position[0]][position[1]] = i
        empty = recalculate_shape(empty, position)

    return tableau



