"""Module for simulating a robot direction and movement."""
EAST = (1,0)
NORTH = (0,1)
WEST = (-1,0)
SOUTH = (0,-1)

DIRECTIONS = [EAST, NORTH, WEST, SOUTH]

class Robot:
    """Class representing a robot that can turn and move.

    Attributes:
        direction (tuple): Current direction.
        coordinates (tuple): Current (x, y) position.
    """
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """Initialize the robot with its direction and coordinates"""
        self.direction = direction
        self.direction_index = DIRECTIONS.index(self.direction)
        self.coordinates = (x_pos,y_pos)

    def move(self, command_string):
        """Function for changing the direction via string of commands.

        Args:
            command_string (str): string of commands represented via letters
        """

        for command in command_string:
            if command == "R":
                self.direction_index = (self.direction_index - 1) % 4
                self.direction = DIRECTIONS[self.direction_index]
            elif command == "L":
                self.direction_index = (self.direction_index + 1) % 4
                self.direction = DIRECTIONS[self.direction_index]
            elif command == "A":
                self.coordinates = tuple(x + y for x, y in zip(self.coordinates, self.direction))