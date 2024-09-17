import random

def empty_tableau(shape):
    tableau = []
    rows = shape.split("-")
    for i in range(len(rows) - 1):
        tableau.append([-1] * int(rows[i]))
    return tableau


def is_corner(tableau, position):
    row = position[0]
    column = position[1]
    if row >= len(tableau):
        return False
    
    if column >= len(tableau[row]):
        return False
    
    if column + 1 >= len(tableau[row]):
        if row + 1 >= len(tableau):
            return True
        elif column >= len(tableau[row+1]):
            return True
    return False

def select_random_cell(tableau):
    total_cells = 0
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            total_cells += 1 
    
    if total_cells == 0:
        return None
    
    random_cell = random.randint(0, total_cells - 1)

    count = 0
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if count == random_cell:
                return (i, j)
            count += 1


def hook_walk(tableau, position):
    row = position[0]
    column = position[1]

    if row >= len(tableau) or column >= len(tableau[row]):
        return None

    row_cells = len(tableau[row]) - column - 1
    
    column_cells = 0
    for i in range(row + 1, len(tableau)):
        if len(tableau[i]) > column: 
            column_cells += 1

    random_cell = random.randint(0, row_cells + column_cells - 1)

    if random_cell < row_cells:
        return (row, column + random_cell + 1)
    
    return (row + (random_cell - row_cells + 1), column)

def tableau_to_string(tableau):
    s = ""
    max_width = max(len(str(num)) for row in tableau for num in row)

    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            s += f"{str(tableau[i][j]).rjust(max_width)} "
        s += "\n"
    return s

