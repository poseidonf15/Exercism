"""
Module to calculate the amount of eggs in a coop.
"""

def egg_count(display_value: int):
    """Function to calculate the amount of eggs in a coop using their bianry representation.

    args:
        display_value (int): binary represantation of a given coop.

    returns:
        int: amount of eggs in the coop.
    """
    binary = ""

    if display_value == 0:
        binary = "0"
    else:
        while display_value > 0:
            remainder = display_value % 2
            binary = str(remainder) + binary
            display_value = display_value // 2

    return len(binary.replace("0",""))