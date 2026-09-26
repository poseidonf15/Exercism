"""
Module to encode and decode using the rail fence cipher.
"""
def encode(message, rails):
    """Function to encode a message using the rail fence cipher.

    Args:
        message (str): The message to encode.
        rails (int): The amount of rails.

    Returns:
        str: The encoded message.
    """
    result = []
    jump_size = rails * 2 - 2

    for start_index in range(rails):
        for index, char in enumerate(message):
            if not (index - start_index) % jump_size or not (index + start_index) % jump_size:
                result.append(char)

    return "".join(result)

def decode(encoded_message, rails):
    """Function to decode a message using the rail fence cipher.

    Args:
        encoded_message (str): The encoded message to decode.
        rails (int): The amount of rails.

    Returns:
        str: The decoded message.
    """
    result = []
    jump_size = rails * 2 - 2
    message_parts = []
    message_length = len(encoded_message)
    last_message_part_index = 0

    for starting_index in range(rails):
        if 0 < starting_index < rails - 1:
            message_part_index = int((message_length - (starting_index + 1)) / (jump_size // 2) + 1)
        else:
            message_part_index = int((message_length - (starting_index + 1)) / jump_size + 1)
        message_parts.append([char for char in encoded_message[last_message_part_index:last_message_part_index + message_part_index]])
        last_message_part_index += message_part_index

    index = 0
    direction = -1
    while any(message_parts):
        result.append(message_parts[index].pop(0))
        if not index % (jump_size // 2):
            direction *= -1
        index += direction

    return "".join(result)