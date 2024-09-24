

def has_interesting(permutation):
    insertion_tableau = []
    
    for number in permutation:
        previous_col = -1
        row = 0
        while True:
            if len(insertion_tableau) <= row:
                insertion_tableau.append([number])
                if previous_col == -1:
                    previous_col = 0
                elif previous_col > 0:
                    return True
                else:
                    previous_col = -2
                break
            
            column = len(insertion_tableau[row])

            while column > 0 and number < insertion_tableau[row][column-1]:
                column = column - 1

            if column == len(insertion_tableau[row]):
                insertion_tableau[row].append(number)
                if previous_col == -1:
                    previous_col = column
                elif previous_col > column:
                    return True
                else:
                    previous_col = -2
                break
            
            temp = insertion_tableau[row][column]
            insertion_tableau[row][column] = number
            number = temp
            if previous_col == -1:
                previous_col = column
            elif previous_col > column:
                return True
            else:
                previous_col = -2

            row = row + 1

    return False

