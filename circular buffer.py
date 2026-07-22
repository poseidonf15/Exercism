"""
Module to create a circular buffer module and raise exeptions if needed.
"""
class CircularBuffer:
    """Class to store data using a circular data type.

    Attributes:
        capacity (int): The length of the buffer
        buffer (list): The buffer data
        read_index (int): The current index to read data in the buffer
        write_index (int): The current index to store data in the buffer
        size (int): The size of the current buffer
    """
    def __init__(self, capacity):
        """Function to initialize the buffer data structure and position."""
        self.capacity = capacity
        self.buffer = [None for _ in range(capacity)]
        self.read_index = 0
        self.write_index = 0
        self.size = 0


    def read(self):
        """Function returns the data in the current position of the buffer.

        Returns:
            any type: The data from the current position of the buffer
        """
        if self.size <= 0:
            raise BufferEmptyException("Circular buffer is empty")
        data = self.buffer[self.read_index]
        self.buffer[self.read_index] = None
        self.size -= 1
        self.read_index = (self.read_index + 1) % self.capacity
        return data

    def write(self, data):
        """Function adds additional data to the buffer.

        Args:
            data (any type): The additional data to add to the buffer
        """
        if self.size >= self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.write_index] = data
        self.size += 1
        self.write_index = (self.write_index + 1) % self.capacity

    def overwrite(self, data):
        """Function acts as the 'write' function when the buffer isn't full and
        overwrite the oldest item in the buffer if the buffer is full.

        Args:
            data (any type): The data to add to the buffer
        """
        self.buffer[self.write_index] = data
        self.write_index = (self.write_index + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1
        else:
            self.read_index = self.write_index

    def clear(self):
        """Function to clear all the data from the buffer."""
        self.buffer = [None for _ in range(self.capacity)]
        self.read_index = 0
        self.write_index = 0
        self.size = 0

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    Args:
        message (str): explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    Args:
        message (str): explanation of the error.
    """
    def __init__(self, message):
        self.message = message