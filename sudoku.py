puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def find_empty(data):   #returns table with positions of empty fields
    empty_fields = []
    for row in range(9):
        for col in range(9):
            if data[row][col] == 0:
                coords = [row, col]
                empty_fields.append(coords)
    return empty_fields


def give_row_and_col_values(coords, puzzle):    #returns existing values in the row, column and square for considered empty field
    existing_values = []
    for pos in puzzle[coords[0]]:
        existing_values.append(pos)             #adds values from the same row as considered field
    for pos in range(0, 9):
        existing_values.append(puzzle[pos][coords[1]])  #adds values from the same column as considered field
    row = coords[0]
    col = coords[1]
    if row in range(3):         #checks if considered field is in 1st three rows
        row = range(3)
    elif row in range(3,6):     #checks if considered field is in 2nd three rows
        row = range(3,6)
    else:                       #checks if considered field is in 3rd three rows
        row = range(6,9)

    if col in range(3):         #checks if considered field is in 1st three columns
        col = range(3)
    elif col in range(3,6):     #checks if considered field is in 2nd three columns
        col = range(3,6)
    else:                       #checks if considered field is in 3rd three columns
        col = range(6,9)
    for x in row:
        for y in col:
            existing_values.append(puzzle[x][y])        #adds values from the same square as considered field

    return existing_values


def sudoku(puzzle):
    empty_fields = find_empty(puzzle)
    i = 0
    while i<len(empty_fields):
        if i == len(empty_fields) or i <0:
            print(" ;(")

        position = empty_fields[i]
        row = position[0]
        col = position[1]

        existing_values = give_row_and_col_values(position, puzzle)
        inserted_value = puzzle[row][col] + 1
        while inserted_value in existing_values:
            inserted_value += 1
        if inserted_value > 9:
            i -= 1
            puzzle[row][col] = 0
        else:
            puzzle[row][col] = inserted_value
            i += 1

    return puzzle


solution = sudoku(puzzle)

for row in solution:
    print(row)