"""
Module to create 'D&D' characters.
"""
import random

class Character:
    """Class to create D&D characters with 6 randomly valued stats and a modifier."""

    def __init__(self):
        self.hitpoints = 0
        ability_names = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

        for name in ability_names:
            setattr(self, name, self.ability())

        self.constitution = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Function to calculate every ability points.

        returns:
            int: the amount of points
        """
        points = [random.randint(1, 6) for _ in range(4)]
        return sum(points) - min(points)

def modifier(value):
    """Function to calculate the amount of HP using the character's constitution

    args:
        value (int): the amount of the character's constitution

    returns:
        int: the amount HP"""

    return (value - 10) // 2