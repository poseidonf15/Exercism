"""
Module to store and check card validation using the 'Luhn formula'.
"""
class Luhn:
    """Class to store card numbers and check their validation.

    Attributes:
        card_num (str): card number
    """

    def __init__(self, card_num):
        """Initialize the card with it's number"""
        self.card_num = card_num

    def valid(self):
        """check for card number validation

        returns:
            bool: the card validation
        """
        checked_card_num = self.card_num.replace(" ", "")

        if len(checked_card_num) <= 1 or not checked_card_num.isdigit():
            return False

        checked_card_num = [int(num) for num in checked_card_num[::-1]]

        for index, num in enumerate(checked_card_num):
            if (index + 1) % 2 == 0:
                num *= 2
                if num > 9:
                    num -= 9
                checked_card_num[index] = num

        return sum(checked_card_num) % 10 == 0