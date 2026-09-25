"""
Module to print out a diamond shape using alphabetic order letters.
"""
from string import ascii_lowercase as ALPHABET
ALPHABET = ALPHABET.upper()

def rows(letter: str):
    """Function returns a list containing a diamond shape figure with letters.

    args:
        letter (str): a letter that determines the middle row of the diamond.

    returns:
        list: the diamond shape figure.
    """
    main_index = ALPHABET.find(letter)
    diamond = []
    for index, item in enumerate(ALPHABET[0: main_index + 1]):
        half_row = " " * (main_index - index) + item + " " * index
        diamond.append(half_row + half_row[-2::-1])

    return diamond + diamond[-2::-1]