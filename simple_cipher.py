"""
Module to decode and encode using the 'vigenere cipher'.
"""

import secrets

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Cipher:
    """Class to store a key for 'vigenere cipher' and then decode and encode with it.

    Attributes:
        key (str): The key to encode and decode the cipher
        key_length (int): The length of the key
    """
    def __init__(self, key=None):
        if not key:
            key = "".join(secrets.choice(ALPHABET) for _ in range(100))
        self.key = key
        self.key_length = len(key)

    def encode(self, text):
        result = []
        for index in range(len(text)):
            result.append(ALPHABET[(ALPHABET.index(text[index]) + ALPHABET.index(self.key[index % self.key_length])) % 26])

        return "".join(result)

    def decode(self, text):
        result = []
        for index in range(len(text)):
            result.append(ALPHABET[(ALPHABET.index(text[index]) - ALPHABET.index(self.key[index % self.key_length])) % 26])

        return "".join(result)