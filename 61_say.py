"""
Module to translate number from 0 to 999_999_999_999 to plain english.
"""

ONES = ["one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"]
TEENS = ["ten",
         "eleven",
         "twelve",
         "thirteen",
         "fourteen",
         "fifteen",
         "sixteen",
         "seventeen",
         "eighteen",
         "nineteen"]
TENS = ["twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"]


def say(number: int):
    """Function to translate number into their name in english.

    args:
        number (int): number from 0 to 999_999_999_999

    returns:
        str: number's english pronunciation

    raises:
        ValueError: if the given number in negative or exceeds 999_999_999_999
    """

    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    number = str(number)
    result = []

    for index, char in enumerate(number):
        digit = int(char)

        if char != "0":

            if (len(number) - index) % 3 == 0:
                result.append(ONES[digit - 1] + " hundred")
            elif (len(number) - index) % 3 == 2:
                if 9 < int(number[index:index + 2]) < 20:
                    result.append(TEENS[int(number[index + 1])])
                elif 20 <= int(number[index:index + 2]):
                    result.append(TENS[digit - 2])
                    if number[index + 1] != "0":
                        result[-1] = result[-1] + "-" + ONES[int(number[index + 1]) - 1]
            elif (len(number) - index) % 3 == 1:
                if index == 0:
                    result.append(ONES[digit - 1])
                elif number[index - 1] == "0":
                    result.append(ONES[digit - 1])
                    if result[-2] and "hundred" in result[-2]:
                        result[-1] = "and " + result[-1]

            if len(number) - index == 4:
                result.append("thousand")
            elif len(number) - index == 7:
                result.append("million")
            elif len(number) - index == 10:
                result.append("billion")

    return " ".join(result)