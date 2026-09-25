"""Module to convert 'images' of digits into digits."""
def convert(input_grid):
    """Function given a grid of characters representing some digits, converts the grid into a string of digits.

    args:
        input_grid (list): grid of characters representing digits

    returns:
        (str): string of converted digits

    raises:
            ValueError: if number of rows aren't multiples of 4 or the number of columns aren't multiples of 3"""

    if not input_grid:
        return ""
    row_length = len(input_grid[0])

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if row_length % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    numbers = {""" _ | ||_|""": "0",
               """     |  |""": "1",
               """ _  _||_ """: "2",
               """ _  _| _|""": "3",
               """   |_|  |""": "4",
               """ _ |_  _|""": "5",
               """ _ |_ |_|""": "6",
               """ _   |  |""": "7",
               """ _ |_||_|""": "8",
               """ _ |_| _|""": "9"}

    result = []
    for row_index in range(0,len(input_grid),4):
        row_result = []
        for column_index in range(0,row_length,3):
            number = "".join(input_grid[row_index + i][column_index:column_index+3] for i in range(3))
            row_result.append(numbers.get(number, "?"))
        result.append("".join(row_result))

    return ",".join(result)