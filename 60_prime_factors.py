"""
Module to compute the factors of a given natural number.
"""

def factors(value: int):
    """Function returns the factors of a given natural number.

    args:
        value (int): natural number

    returns:
        list: the factors of the given number
    """

    devider = 2
    factors_list = []

    while value > 1:
        if value % devider == 0:
            value //= devider
            factors_list.append(devider)
        else:
            devider += 1

    return factors_list