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

    result = []
    matrix_columns = list(zip(*matrix))

    for row in range(0, len(matrix)):
        row_max = max(matrix[row])
        for column in range(0,len(matrix_columns)):
            if matrix_columns[column][row] == min(matrix_columns[column]) and matrix[row][column] == row_max:
                result.append((row,column))

    return [{"row": coordinate[0] + 1, "column": coordinate[1] + 1} for coordinate in result]