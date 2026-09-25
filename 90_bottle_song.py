"""
Module to recite the lyrics to that popular children's repetitive song: 'Ten Green Bottles'.
"""

NUMBERS = ["No green bottles",
           "One green bottle",
           "Two green bottles",
           "Three green bottles",
           "Four green bottles",
           "Five green bottles",
           "Six green bottles",
           "Seven green bottles",
           "Eight green bottles",
           "Nine green bottles",
           "Ten green bottles"]

def recite(start, take=1):
    """Function returns specific verses from the childrens song 'Tne Green Bottles'.

    Args:
        start (int): The index of the starting verse
        take (int): How many verses to return from the starting verse

    Returns:
        list: The lyrics of the song
    """
    result = []

    for count in range(take):
        bottles = start - count

        if count:
            result.append("")

        result.append(f"{NUMBERS[bottles]} hanging on the wall,")
        result.append(f"{NUMBERS[bottles]} hanging on the wall,")
        result.append(f"And if one green bottle should accidentally fall,")
        result.append(f"There'll be {NUMBERS[bottles-1][0].lower() + NUMBERS[bottles-1][1:]} hanging on the wall.")

    return result