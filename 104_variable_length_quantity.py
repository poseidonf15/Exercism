"""
Module to implement VLQ encoding/decoding.
"""
def encode(numbers):
    """Function to encode numbers using VLQ.

    Args:
        numbers (list): The number to encode.

    Returns:
        list: VLQ representation of the given number.
    """

    result = []
    for number in numbers:
        if number == 0:
            result += [0]
            continue
        translation = []
        while number:
            translation.insert(0, 0b10000000 + (number & 0b1111111))
            number >>= 7
        translation[-1] -= 0b10000000
        result.extend(translation)

    return result

def decode(bytes_):
    """Function to decode VLQ number representations into.

    Args:
        bytes_ (list): The VLQ number representations to decode.

    Returns:
        list: List of decoded numbers.
    """

    if bytes_[-1] >> 7:
        raise ValueError("incomplete sequence")

    result = []
    number = 0

    for bit in bytes_:
        number = ((number << 7) | (bit & 0b1111111))
        if not bit >> 7:
            result.append(number)
            number = 0

    return result