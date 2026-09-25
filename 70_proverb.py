"""
Module to generate the relevant proverb for a given list.
"""
def proverb(*words, qualifier=None):
    """Function returns a proverb for a given list of words.

    args:
        words (list): list of words
        qualifier (str): value to modify the final verse

    returns:
        list: the final proverb
    """

    result = []

    if words:
        for index, word in enumerate(words[:-1]):
            result.append(f"For want of a {word} the {words[index + 1]} was lost.")
        if qualifier:
            result.append(f"And all for the want of a {qualifier} {words[0]}.")
        else:
            result.append(f"And all for the want of a {words[0]}.")

    return result