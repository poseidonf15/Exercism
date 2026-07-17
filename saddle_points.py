"""Module to determine the best trees in a given matrix."""
def saddle_points(matrix):
    """Function takes a matrix of trees heights and
    returns the location of the best trees (the trees who are the largest in the row and shortest in the column)

    args:
        matrix (list): matrix of trees heights

    returns:
        list: list of trees coordinates
    """
    if not matrix:
        return []

    row_length = len(matrix[0])
    for row in matrix[1:]:
        if row_length != len(row):
            raise ValueError("irregular matrix")

    column_mins = []
    for column_index in range(0, row_length):
        column = []
        for row in matrix:
            column.append(row[column_index])
        column_mins.append(min(column))

    result = []

    for row_index, row in enumerate(matrix):
        row_max = max(row)
        for column_index in range(row_length):
            if matrix[row_index][column_index] == column_mins[column_index] == row_max:
                result.append((row_index,column_index))

    return [{"row": coordinate[0] + 1, "column": coordinate[1] + 1} for coordinate in result]