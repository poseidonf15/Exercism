"""
Module to find all posibble combinations for a given killer sudoku cage.
"""
def combinations(target, size, exclude):
    """Function return all possible number combinations for a given killer sudoku cage.

    Args:
        target (int): The sum of the cage.
        size (int): The amount of cells in the cage.
        exclude (list): Numbers that can't be used for the combination.

    Returns:
        list: nested ordered list with the possible combination.
    """
    exclude = set(exclude)

    if size <=  1:
        if target not in exclude and target > 0:
            return [[target]]
        else:
            return [None]

    result = []

    for possible_cell_value in range(1, 10):
        if possible_cell_value in exclude:
            continue
        if possible_cell_value > target:
            break
        for combination in combinations(target - possible_cell_value, size - 1, exclude | {possible_cell_value}):
            if combination is not None:
                result.append([possible_cell_value] + combination)
                exclude |= set(combination)

    return result