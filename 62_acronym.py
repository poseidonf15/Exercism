"""
Module converts a phrase to its acronym.
"""

def abbreviate(words: str):
    """Function returns the acronyms of a given phrase.

    args:
        words (str): phrase

    returns:
        str: acronym ot the given phrase
    """

    result = ""

    words = words.replace("-", " ")

    for word in words.split():
        for char in word:
            if char.isalpha():
                result += char
                break

    return result.upper()