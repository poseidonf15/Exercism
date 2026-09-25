"""
Module to return specific parts from the song 'The Twelve Days Of Christmas'.
"""

def recite(start_verse: int, end_verse: int):
    """Function returns part of the song from the detrmined starting and ending verse.

    args:
        start_verse (int): the number of the starting verse
        end_verse (int): the number of the ending verse

    returns:
        list: the part of the songs seperated into verses
    """

    result = []
    numeral_order = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth",
                     "tenth", "eleventh", "twelfth"]
    gifts = ["a Partridge in a Pear Tree", "two Turtle Doves", "three French Hens", "four Calling Birds",
             "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking",
             "nine Ladies Dancing", "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]

    for verse_index in range(start_verse - 1, end_verse):
        mini_result = []
        mini_result.append(f"On the {numeral_order[verse_index]} day of Christmas my true love gave to me: ")

        if verse_index == 0:
            mini_result.append(gifts[0] + ".")
        else:
            for index in range(verse_index, -1, -1):
                if index > 0:
                    mini_result.append(gifts[index] + ", ")
                else:
                    mini_result.append("and " + gifts[0] + ".")

        result.append("".join(mini_result))

    return result