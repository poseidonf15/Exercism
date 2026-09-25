"""
Module to convert Arabic numerals into Roman.
"""
def roman(number: int):
    """Function return the equivalent Roman numeral of a given Arabic numeral.

    args:
        number (int): Arabic numeral

    return:
        str: Roman numeral
    """

    romans = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
              10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

    result = []

    for value, letter in romans.items():
        current_digit = number // value
        if current_digit >= 1:
            result.append(letter * current_digit)
        number = number % value

    return "".join(result)