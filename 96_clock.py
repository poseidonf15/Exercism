"""
Module that handles clock times without dates.
"""
class Clock:
    """Class to store the clock and operate him.

    Attributes:
        hour (int): The amount of hours.
        minute (int): The amount of minutes.
    """
    def __init__(self, hour, minute):
        """Initialize the clock with its hours and minutes."""

        self.hour = (hour + (minute // 60)) % 24
        self.minute = minute % 60

    def __repr__(self):
        """Function returns a readeable represantation of the class object used for debugging."""

        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        """Function returns the human-readable representation of the clock."""

        return ":".join(time_part if len(time_part) == 2 else f"0{time_part}" for time_part in [str(self.hour), str(self.minute)])

    def __eq__(self, other):
        """Function compares clocks to determine if they are equal."""

        return other.hour == self.hour and other.minute == self.minute

    def __add__(self, minutes):
        """Function to advance the clock using minutes."""

        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        """Function to rewind the clock using minutes."""

        return Clock(self.hour, self.minute - minutes)