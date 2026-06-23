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

    result = "".join([char.lower() if char.isalpha() else char if char.isdigit() or char == "'" else " "
                      for char in sentence])
    for index, char in enumerate(result):
        if char == "'" and not(result[index - 1].isalpha() and result[index + 1].isalpha()):
            result = result[:index] + " " + result[index + 1:]
    result = result.split()

    final_result = {}
    for word in result:
        if word in final_result:
            final_result[word] += 1
        else:
            final_result[word] = 1

    return final_result