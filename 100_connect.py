"""
Module to determine the outcome of a given game of 'Hex'.
"""
class ConnectGame:
    """Class to store a board of a game of 'Hex' and determine the winner.

    Attributes:
        board (list): The game board.
    """
    def __init__(self, board):
        """Initialize the game with its board."""
        self.board = [row.strip().split() for row in board.split("\n")]
        self.amount_of_rows = len(self.board)
        self.amount_of_columns = len(self.board[0])

    def get_winner(self):
        """Function to determine who is the winner of the match, if there is one.

        Returns:
            str: The symbol of the player that won the game (X/O) or '' if there is no winner.
        """
        # Checks for one tile board.
        if self.amount_of_rows == self.amount_of_columns == 1:
            return self.board[0][0]

        # Checks if player X is the winner.
        x_starting_points = [(0, row) for row in range(self.amount_of_rows) if self.board[row][0] == "X"]

        self.checked_points = []
        for starting_point in x_starting_points:
            if self.has_winning_route(starting_point, "X", {"point index": 0, "condition": self.amount_of_columns - 1}):
                return "X"

        # Checks if player O is the winner.
        o_starting_points = [(column, 0) for column in range(self.amount_of_columns) if self.board[0][column] == "O"]

        self.checked_points = []
        for starting_point in o_starting_points:
            if self.has_winning_route(starting_point, "O", {"point index": 1, "condition": self.amount_of_rows - 1}):
                return "O"

        return ""

    def has_winning_route(self, point, symbol, target):
        """Recursive Function that tries to find a winning route.

        Args:
            point (tuple): The current point on the playing board.
            symbol (str): The symbol of the player we are checking for.
            target (dict): The condition that the player's route needs to reach to be determined the winner of the match.

        Returns:
            bool: Whether the player won or not.
        """
        # Turns the list of the neighbors into a filtered list that contains only the points with the target symbol (X/O).
        neighbors = [neighbor for neighbor in self.get_neighbors(*point)
                     if self.board[neighbor[1]][neighbor[0]] == symbol]

        for neighbor in neighbors:
            # Checks that we didn't go through this point already so the function wouldn't loop itself.
            if neighbor not in self.checked_points:
                self.checked_points.append(neighbor)
                # Checks if the point matches the targets condition.
                if neighbor[target["point index"]] == target["condition"]:
                    return True
                # Recurse itself.
                result = self.has_winning_route(neighbor, symbol, {"point index": target["point index"], "condition": target["condition"]})
                if result:
                    return True
        # If the recurse is done and there is no point found it means this player is not the winner.
        return False

    def get_neighbors(self, column, row):
        """Function that gets the neighbor points of a given point on the 'HEX' board.

        Args:
            column (int): The column of the given point.
            row (int): The row of the given point.

        Returns:
            list: List of all the neighbors of the point that exist on the board.
        """
        neighbors = [(column + 1, row), (column, row - 1), (column + 1, row - 1), (column, row + 1), (column - 1, row + 1), (column - 1, row)]
        result = [neighbor for neighbor in neighbors
                  if 0 <= neighbor[0] < self.amount_of_columns
                  and 0 <= neighbor[1] < self.amount_of_rows]
        return result