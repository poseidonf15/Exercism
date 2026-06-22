"""
Module to output all the contiguous substrings of a certain length.
"""

def slices(series, length):
    """Function returns all the contiguous substrings of a given length.

    args:
        series (str): string of digits
        length (int): length of the slices

    returns:
        list: the slices of the given series with the given length

    raises:
        ValueError: if the length is less than 1, grater than the series or the series is empty
    """

    if length < 0:
        raise ValueError("slice length cannot be negative")
    elif length == 0:
        raise ValueError("slice length cannot be zero")
    elif not series:
        raise ValueError("series cannot be empty")
    elif len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    result = []
    for index in range(0, len(series) - length + 1):
        result.append(series[index:index + length])

    return result