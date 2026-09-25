"""
Module to convert a sequence of digits in one base, representing a number,
into a sequence of digits in another base, representing the same number.
"""
import math

def rebase(input_base, digits, output_base):
    """Function to get a base and a list of digits, convert it into a number and return it converted into the other base.

    Args:
        input_base (int): The base to get the original number.
        digits (list): The digits to convert.
        output_base (int): The base to convert into.

    Returns:
        list: Listed representation of the result number in the set base.

    Except:
        ValueError: input base or output base are under 2 and all digits should be 0 or greater and lower than the input base.
    """

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all([0 <= d < input_base for d in digits]):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    digits = digits[::-1]
    number = sum([input_base**index * digits[index] for index in range(len(digits))])

    if number == 0:
        return [0]

    power = math.floor(math.log(number, output_base))
    result = []

    while power >= 0:
        bit, number = divmod(number, output_base ** power)
        result.append(bit)
        power -= 1

    return result