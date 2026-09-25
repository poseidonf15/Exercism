"""
Module to determine a persons allergies using their allergy score.
"""

ALLERGIES = ["eggs",
             "peanuts",
             "shellfish",
             "strawberries",
             "tomatoes",
             "chocolate",
             "pollen",
             "cats"]

class Allergies:
    """Class to store the score ot the allergy test and determine the result.

    Attributes:
        list_of_allergies (list): All the allergies that turned out positive
    """

    def __init__(self, score):
        """Initialize the Allergies test with its score and `results"""
        bits = [char for char in str(bin(score % 256))[2:]]
        self.list_of_allergies = [allergy
                                  for allergy, bit in zip(ALLERGIES, bits[::-1])
                                  if bit == "1"]

    def allergic_to(self, item):
        """Function returns if the checked person has a certain allergy.

        Args:
            item (str): The allergies

        Returns:
            bool: Whether the person has the allergy or not
        """
        return item in self.list_of_allergies

    @property
    def lst(self):
        """The list of allergies property"""
        return self.list_of_allergies