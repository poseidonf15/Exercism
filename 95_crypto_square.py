"""
Module to implement the classic method for composing secret messages called a square code.
"""
def cipher_text(plain_text):
    """Function to implenet a squre code method on text.

     Args:
        plain_text (str): The text to code.

    Returns:
        str: The text coded
    """

    normalized_text = "".join([char.lower() for char in plain_text if char.isalnum()])
    if not normalized_text:
        return ""
    char_amount = len(normalized_text)

    # Gets the sizes of the 'text rectangle' columns and rows.
    r = round(char_amount ** 0.5)
    c = round(char_amount / r)

    normalized_text += " " * (r * c - char_amount)

    # Creates the 'text rectangle' using the columns and rows sizes.
    text_rect = [normalized_text[row * c: (row + 1) * c] for row in range(r)]

    # Reads the columns of the text rectangle left to right.
    columns_text = "".join([row[column] for column in range(c) for row in text_rect]).strip()

    white_spaces_index = len(text_rect[-1].strip())
    result = []

    # Saparates the columns_text string into chunks in order to space them later.
    for chunk in range(c):
        if chunk < white_spaces_index:
            result.append(columns_text[chunk * r: (chunk + 1) * r])
        else:
            result.append(columns_text[chunk * r: (chunk + 1) * r - 1] + " ")

    return " ".join(result)