"""
Module to find all Pythagorean triplets for which a + b + c = N and a < b < c.
"""
def triplets_with_sum(number):
    """Function returns all Pythagorean triplets for which a + b + c = the given number and a < b < c.

    Args:
        number (int): Number

    Returns:
        list: List of all the Pythagorean triplets for which a + b + c = the given number and a < b < c
    """
    if not number:
        return []

    result = []

    for a in range(1, number // 3):
        numerator = a ** 2 + (number - a) ** 2
        denominator = 2 * (number - a)

        if numerator % denominator != 0:
            continue

        c = numerator // denominator
        b = number - a - c

        if a < b < c:
            result.append([a, b, c])

    return result