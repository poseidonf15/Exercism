"""Module to calculate calls changes using 'Conway's game of life'."""
def tick(matrix: list):
    """Function to calculate every generation.

    args:
        matrix (list): the cells with represented in 1's and 0's

    returns:
        list: representation of how the next gen will look.
    """
    result = [row[:] for row in matrix]
    for row_index, row in enumerate(matrix):
        for column_index, cell in enumerate(row):
            amount_of_alive_cells_around = find_surrounding(row_index, column_index, matrix)

            if cell == 0 and amount_of_alive_cells_around == 3:
                result[row_index][column_index] = 1
            elif cell == 1 and not 2 <= amount_of_alive_cells_around <= 3:
                result[row_index][column_index] = 0

    return result

def find_surrounding(row, column, matrix):
    """Function to find the values of the surrounding cells of any cell in the matrix.

    args:
        row (int): index of the row
        column (int): index of the column
        matrix (list): matrix of the whole cell system
    """
    cells = []

    for target_row in range(-1, 2):
        target_row_index = row + target_row
        if 0 <= target_row_index < len(matrix):
            for target_column in range(-1, 2):
                target_column_index = column + target_column
                if 0 <= target_column_index < len(matrix[0]) and not (target_row == 0 and target_column == 0):
                    cells.append(matrix[target_row_index][target_column_index])
    return cells.count(1)