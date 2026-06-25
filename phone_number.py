"""
Module to return 'cleaned' version of a given phone number and point their errors
"""
class PhoneNumber:
    """Class to return 'cleaned '.

    Attributes:
        number (str): phone number
    """
    def __init__(self, number):
        """Initialize the phone number"""
        self.number = number
        self.check_for_invalid_characters()
        self.number = "".join(char for char in self.number if char.isdigit())
        self.check_for_invalid_length()
        self.check_for_invalid_numbers()
        self.area_code = self.number[:3]

    def check_for_invalid_characters(self):
        """Function to check for unexepted characters.

        raises:
            ValueError: if there is punctuation or letters
        """
        if any(char.isalpha() for char in self.number):
            raise ValueError("letters not permitted")
        if any(char in """!"#$%&'*,/:;<=>?@[\]^_{|}~`""" for char in self.number):
            raise ValueError("punctuations not permitted")

    def check_for_invalid_length(self):
        """Function to check for phone number too short or too long.

        raises:
            ValueError: if the length of the phone number is less than 10 or more than 11
        """
        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")

    def check_for_invalid_numbers(self):
        """Function for 'cleaning' the phone number.

        raises:
            ValueError: if the phone number contains a country code that's not 1 or area code under 2
            or exchange code under 2
        """
        if len(self.number) == 11:
            if self.number[0] != "1":
                raise ValueError("11 digits must start with 1")
            self.number = self.number[1:]
        if self.number[-7] == "0":
            raise ValueError("exchange code cannot start with zero")
        if self.number[-7] == "1":
            raise ValueError("exchange code cannot start with one")
        if self.number[-10] == "0":
            raise ValueError("area code cannot start with zero")
        if self.number[-10] == "1":
            raise ValueError("area code cannot start with one")

    def pretty(self):
        """Function for making the phone number 'pretty' by adding '()-' symbols in the right places.

        returns:
            str: the 'pretty' version of the phone number
        """

        return "".join(["(", self.area_code, ")-", self.number[3:6], "-", self.number[6:]])