import random

def generate_permutation(n):
    return random.sample(range(n), n)

def insertion(insertion_tableau, number):
    row = 0
    while True:
        if len(insertion_tableau) <= row:
            insertion_tableau.append([number])
            return insertion_tableau, (row, 0)
        
        column = len(insertion_tableau[row])

        while column > 0 and number < insertion_tableau[row][column-1]:
            column = column - 1

        if column == len(insertion_tableau[row]):
            insertion_tableau[row].append(number)
            return insertion_tableau, (row, column)
        
        temp = insertion_tableau[row][column]
        insertion_tableau[row][column] = number
        number = temp

        row = row + 1


def recording(recording_tableau, index, position):
    if len(recording_tableau) <= position[0]:
        recording_tableau.append([index])
        return recording_tableau
    
    if len(recording_tableau[position[0]]) <= position[1]:
        recording_tableau[position[0]].append(index)
        return recording_tableau
    
    recording_tableau[position[0]][position[1]] = index



def schensted_insertion(permutation):
    insertion_tableau = []
    recording_tableau = []

    for i in range(len(permutation)):
        insertion_tableau, record = insertion(insertion_tableau, permutation[i])
        recording_tableau = recording(recording_tableau, i + 1, record)

    return insertion_tableau, recording_tableau


def find_shape(permutation):
    insertion_tableau = []
    recording_tableau = []

    for i in range(len(permutation)):
        insertion_tableau, record = insertion(insertion_tableau, permutation[i])
        recording_tableau = recording(recording_tableau, i + 1, record)


    s = ""
    for i in range(len(insertion_tableau)):
        s = s + str(len(insertion_tableau[i])) + "-"
    return s








