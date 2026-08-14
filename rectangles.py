"""
Module to count the rectangles in an ASCII diagram.
"""
def rectangles(strings):
    """Function returns the amount of rectangles in an ASCII diagram.

    Args:
        strings (list): The ASCII diagram.

    Returns:
        int: The amount of rectangles.
    """

    result = 0
    for row in range(len(strings)):
        for column in range(len(strings[row])):
            if strings[row][column] == "+":
                result += check_for_rects(strings, row, column)

    return result

def check_for_rects(strings, row, column):
    """Function to find all the possible rectangles for a given point.

    Args:
        strings (list): The ASCII diagram of the rectangles.
        row (int): The index of the row.
        column (int): The index of the column.

    Returns:
        int: The amount of rectangles found.
    """
    result = 0
    for target_column in range(column + 1, len(strings[row])):
        target = strings[row][target_column]
        if target == " ":
            break
        elif target == "+":
            for target_row in range(row + 1, len(strings)):
                target = strings[target_row][target_column]
                if target == " " or target == "-":
                    break
                elif target == "+":
                    column_list = [strings[r][column] for r in range(row + 1, target_row)]
                    result += int(" " not in strings[target_row][column:target_column + 1] and
                                  all(token == "|" or token == "+" for token in column_list) and
                                  "+" == strings[target_row][column])

    return result