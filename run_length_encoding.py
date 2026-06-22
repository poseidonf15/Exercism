"""
Module to encode and decode the 'run length'
"""

def decode(string: str):
    """Function return the decoded version of a given string.

    args:
        string (str): of type of string

    return:
        str: decoded version of the given string
    """
    num = ""
    result = ""
    for char in string:
        if char.isdigit():
            num += char
        else:
            if num:
                result += char * int(num)
                num = ""
            else:
                result += char

    return result

def encode(string: str):
    """Function return the encoded version of a given string.

    args:
        string (str): of type of string

    return:
        str: encoded version of the given string
    """
    if not string:
        return ""

    result = ""
    count = 1

    for index in range(1,len(string)):
        if string[index] == string[index - 1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += string[index - 1]
            count = 1

    if count > 1:
        result += str(count)
    result += string[-1]

    return result