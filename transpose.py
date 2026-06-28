"""Module to transpose a given text (switch the columns and the rows)."""
def transpose(text: str):
    """Function to trasnpose a given text.

    args:
        text (str): a given text

    return:
        str: its transposed version
    """
    text_into_rows = text.split("\n")

    length = len(max(text_into_rows, key=len))
    max_lengths = [0] * len(text_into_rows)
    result = ["" for _ in range(length)]

    current_max = 0
    for i in range(len(text_into_rows) - 1, -1, -1):
        current_max = max(current_max, len(text_into_rows[i]))
        max_lengths[i] = current_max

    for row_number, row in enumerate(text_into_rows):
        for index in range(0, length):
            if index < len(row):
                result[index] += row[index]
            elif index < max_lengths[row_number]:
                result[index] += " "

    return "\n".join(result)