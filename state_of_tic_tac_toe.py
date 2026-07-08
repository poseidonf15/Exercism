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
    combinations = board.copy()

    for index in range(3):
        combinations.append(board[0][index] + board[1][index] + board[2][index])

    combinations.append(board[0][0] + board[1][1] + board[2][2])
    combinations.append(board[0][2] + board[1][1] + board[2][0])

    for combination in combinations:
        if combination == "XXX":
            x_won = True
        elif combination == "OOO":
            o_won = True

    if x_won and o_won:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if x_won or o_won:
        return "win"
    if " " in "".join(board):
        return "ongoing"
    return "draw"