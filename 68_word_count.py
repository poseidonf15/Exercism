"""
Module to count the amount of words in a given subtitle.
"""
def count_words(sentence: str):
    """Function returns the amount of times every simple words or number appears in a given string.

    args:
        sentence (str): subtitle

    returns:
        dict: dict of all the words and numbers as keys and the amount of time they occur is their value
    """
    sentence = " " + sentence + " "
    cleaned = []

    for index, char in enumerate(sentence):
        if char.isalpha():
            cleaned.append(char.lower())

        elif char.isdigit():
            cleaned.append(char)

        elif char == "'" and sentence[index - 1].isalpha() and sentence[index + 1].isalpha():
            cleaned.append(char)

        else:
            cleaned.append(" ")

    words = "".join(cleaned).split()

    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1

    return words_count