"""
Module to decode and encode atbash cipher
"""
from string import ascii_lowercase as ALPHABET


def encode(plain_text: str):
    """Function returns the encoded version of a given phrase using atbash cipher.

    args:
        plain_text (str): a phrase to encode

    returns:
        str: the encoded version of the phrase
    """
    encoded_text_no_spaces = decode(plain_text)
    encoded_text = encoded_text_no_spaces[:5]

    for index in range(5, len(encoded_text_no_spaces) - 1, 5):
        encoded_text += " " + encoded_text_no_spaces[index:index + 5]
    return encoded_text


def decode(ciphered_text: str):
    """Function returns the decoded version of a given phrase using atbash cipher.

    args:
        plain_text (str): a phrase to encode

    returns:
        str: the decoded version of the phrase
    """
    return "".join(
        ALPHABET[(ALPHABET.find(char) + 1) * -1] if char.isalpha() else char if char.isnumeric() else "" for char in
        ciphered_text.lower())