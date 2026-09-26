"""
Module to add flower counts to empty squares in a completed Flower Field garden.
"""
def annotate(garden):
    """Function returns the field of the garden filled with numbers that repretent the amount of flowers around them.

    Args:
        garden (list): The field of the garden.

    Returns:
        list: The garden with numbers added.

    Raises:
        ValueError: When field isn't a rectangle or contains values that are not '*' or ' '.
    """
    if not garden:
        return []

    result = []

    estimated_row_length = len(garden[0])

    for row_index, row in enumerate(garden):
        result.append("")
        if len(row) != estimated_row_length:
            raise ValueError("The board is invalid with current input.")
        for square_index, square in enumerate(row):
            if square == " ":
                result[row_index] += find_surrounding(row_index, square_index, garden)
            elif square == "*":
                result[row_index] += "*"
            else:
                raise ValueError("The board is invalid with current input.")

    return result

def find_surrounding(row, column, matrix):
    """Function to find the values of the surrounding cells of any cell in the matrix.

    Args:
        row (int): index of the row
        column (int): index of the column
        matrix (list): matrix of the whole cell system

    Returns:
        str: Amount of surrounding cells with flowers ('*')
    """
    flower_amount = 0

    for target_row in range(-1, 2):
        target_row_index = row + target_row
        if 0 <= target_row_index < len(matrix):
            for target_column in range(-1, 2):
                target_column_index = column + target_column
                if 0 <= target_column_index < len(matrix[0]) and not (target_row == 0 and target_column == 0):
                    if matrix[target_row_index][target_column_index] == "*":
                        flower_amount += 1

    if not flower_amount:
        return " "
    return str(flower_amount)