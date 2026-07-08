"""Module to determine the state of a 'Tic Tac Toe' game."""
def gamestate(board: list):
    """Function returns the state of a given 'Tic Tac Toe' board.

    args:
        board (list): 'Tic Tac Toe' game board

    return:
        str: the state of the game
    """
    amount_of_o, amount_of_x = 0, 0
    for row in board:
        amount_of_o += row.count("O")
        amount_of_x += row.count("X")

    if amount_of_o > amount_of_x:
        raise ValueError("Wrong turn order: O started")
    if amount_of_x == amount_of_o + 2:
        raise ValueError("Wrong turn order: X went twice")

    x_won, o_won = False, False

    for row in board:
        x_won, o_won = check_for_win(row, x_won, o_won)

    for index in range(3):
        x_won, o_won = check_for_win(board[0][index] + board[1][index] + board[2][index], x_won, o_won)

    x_won, o_won = check_for_win(board[0][0] + board[1][1] + board[2][2], x_won, o_won)
    x_won, o_won = check_for_win(board[0][2] + board[1][1] + board[2][0], x_won, o_won)

    if x_won and o_won:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if x_won or o_won:
        return "win"
    if " " in "".join(board):
        return "ongoing"
    return "draw"


def check_for_win(combination: str, x_won: bool, o_won: bool):
    """Function to determine whether a given combination is winning for one of the sides.

    args:
        combination (str): 'Tic Tac Toe' combination
        x_won (bool): x winning state
        o_won (bool): o winning state

    returns:
        bool: whether either of them have a winning combination
    """

    if combination == "XXX" and not x_won:
        x_won = True
    elif combination == "OOO" and not o_won:
        o_won = True

    return x_won, o_won

print(gamestate(["OOO","XX "," X "]))