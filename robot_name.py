"""
Module to set and reset factory robots names.
"""
import random
from string import ascii_uppercase as alphabet
class Robot:
    """Class to store robots and their names."""
    names = []
    def __init__(self):
        self.name = ""
        self.reset()

    def reset(self):
        """Function to create a new random name that was never used before."""
        self.name = random.choice(alphabet) + random.choice(alphabet) + \
                    "".join(str(random.randint(1,10)) for _ in range(3))
        if not self.name in Robot.names:
            Robot.names.append(self.name)
        else:
            self.reset()