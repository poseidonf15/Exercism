"""
Module parse and evaluate simple math word problems returning the answer as an integer.
"""

MATH_OPERATIONS = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "divided": lambda x, y: x // y,
    "multiplied": lambda x, y: x * y
}

def answer(question):
    """Function evaluates the given math word problem and returns the solution.

    Args:
        question (str): The math word problem.

    Returns:
        int: solution to the math problem.
    """

    equation = [object for object in question[8:-1].split(" ") if object != "by"]

    if not equation:
        raise ValueError("syntax error")

    numbers = []
    math_operations = []

    for index, token in enumerate(equation):
        if not index % 2:
            try:
                numbers.append(int(token))
            except:
                raise ValueError("syntax error")
        else:
            if token.isalpha():
                if token not in MATH_OPERATIONS:
                    raise ValueError("unknown operation")
                math_operations.append(token)
            else:
                raise ValueError("syntax error")

    if index % 2:
        raise ValueError("syntax error")

    result = int(numbers.pop(0))

    for index in range(len(numbers)):
        result =  MATH_OPERATIONS[math_operations[index]](result, numbers[index])

    return result