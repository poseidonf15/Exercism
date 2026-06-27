"""
Module to determine whether two queens can attack each other or not.
"""
class Queen:
    """Class to define queens and check whether they can attack other queens.

    Attributes:
        row (int): row number
        column (int): column number
    """

    def __init__(self, row, column):
        """Initialize the queen with its position"""
        self.position = (row, column)
        check_position(self.position)

    def can_attack(self, another_queen):
        """check for the queen's abillity to attack other given queen

        args:
            another_queen (tuple): the other queens position

        returns:
            bool: whether the queen can attack the other queen

        raises:
            ValueError: if the queens are on the same square (the positions are equal)
        """
        check_position(another_queen.position)
        if another_queen.position == self.position:
            raise ValueError("Invalid queen position: both queens in the same square")

        return another_queen.position[0] == self.position[0] or another_queen.position[1] == self.position[1] or \
               sum(another_queen.position) == sum(self.position) or another_queen.position[0] - another_queen.position[1] == self.position[0] - self.position[1]

def check_position(position):
    """Function to check whether the given position is valid or not.

    args:
        position (tuple): the position of the queen to check

    raises:
        ValueError: if the position is no available (less than 0 or greater than 7)
    """
    if position[0] < 0:
        raise ValueError("row not positive")
    if position[0] > 7:
        raise ValueError("row not on board")
    if position[1] < 0:
        raise ValueError("column not positive")
    if position[1] > 7:
        raise ValueError("column not on board")