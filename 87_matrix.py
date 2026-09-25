"""
Module to find the rows and columns of a matrix.
"""
class Matrix:
    """Class to store matrix of numbers and return their rows and columns by index.

    Attributes:
        matrix (list): The matrix represented via nested list of rows and columns
        transposed_matrix (list): The matrix represented in reverse nested list of columns and rows
    """
    def __init__(self, matrix_string):
        """Function to Initialize the matrix."""
        self.matrix = [[int(number) for number in row.split()] for row in matrix_string.split("\n")]
        self.transposed_matrix = [list(column) for column in zip(*self.matrix)]

    def row(self, index):
        """Function returns a row from the matrix.

        Args:
            index (int): The index of the row

        Returns:
             list: The numbers store in the row
        """
        return self.matrix[index - 1]

    def column(self, index):
        """Function returns a column from the matrix.

        Args:
            index (int): The index of the column

        Returns:
             list: The numbers store in the column
        """
        return self.transposed_matrix[index - 1]