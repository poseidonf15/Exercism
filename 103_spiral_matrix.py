"""
Module to create a square matrix of a given size.
"""
def spiral_matrix(size):
    """Function return a square matrix of a given size.

    Args:
        size (int): The size of the matrix.

    Returns:
        list: The matrix.
    """

    if not size >= 1:
        return []

    x_dir = -1
    y_dir = 1
    x_pos = size - 1
    y_pos = 0
    current_number = size + 1
    movement_amount = size - 1

    result = [[None for _ in range(size)] for _ in range(movement_amount)]

    result.insert(0, [_ for _ in range(1,size + 1)])

    for _ in range(size - 1):
        for _ in range(movement_amount):
            y_pos += y_dir
            result[y_pos][x_pos] = current_number
            current_number += 1
        for _ in range(movement_amount):
            x_pos += x_dir
            result[y_pos][x_pos] = current_number
            current_number += 1
        movement_amount -= 1
        y_dir *= -1
        x_dir *= -1

    return result