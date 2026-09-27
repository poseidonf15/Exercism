"""
Module to detect palindrome products in a given range.
"""
def largest(min_factor, max_factor):
    """Function return the largest palindrome number which is the product of two numbers within the given range.

    Returns:
        min_factor (int): The smallest factor in the range (default 0)
        max_factor (int): The largest factor in the range

    Returns:
        tuple: Containing the polindrom and list of factor pairs within the range
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    value = 0

    for factor1 in range(max_factor, min_factor - 1, -1):
        if factor1 ** 2 < value:
            break
        for factor2 in range(factor1, min_factor - 1, -1):
            number = factor1 * factor2
            if str(number) == str(number)[::-1] and number > value:
                value = number
                break
            elif number < value:
                break

    if not value:
        return (None, [])

    factors = []
    used_factors = set()
    for factor in range(min_factor, max_factor + 1):
        if used_factors | {factor} == used_factors:
            break
        if value % factor == 0:
            second_factor = value // factor
            if min_factor <= second_factor <= max_factor:
                factors.insert(0, [factor, second_factor] if factor < second_factor else [second_factor, factor])
                used_factors |= {factor, second_factor}

    return (value, sorted(factors))

def smallest(min_factor, max_factor):
    """Function return the smallest palindrome number which is the product of two numbers within the given range.

    Args:
        min_factor (int): The smallest factor in the range (default 0)
        max_factor (int): The largest factor in the range

    Returns:
        tuple: Containing the polindrom and list of factor pairs within the range
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    value = max_factor ** 2

    for factor1 in range(min_factor, max_factor + 1):
        if factor1 ** 2 > value:
            break
        for factor2 in range(factor1, max_factor + 1):
            number = factor1 * factor2
            if str(number) == str(number)[::-1] and number < value:
                value = number
                break
            elif number > value:
                break

    if str(value) != str(value)[::-1]:
        return (None, [])

    factors = []
    used_factors = set()
    for factor in range(min_factor, max_factor + 1):
        if used_factors | {factor} == used_factors:
            break
        if value % factor == 0:
            second_factor = value // factor
            if min_factor <= second_factor <= max_factor:
                factors.insert(0, [factor, second_factor] if factor < second_factor else [second_factor, factor])
                used_factors |= {factor, second_factor}

    return (value, sorted(factors))