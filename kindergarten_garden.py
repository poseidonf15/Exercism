"""
Module to determine which plants each child in the kindergarten is responsible for by the diagram.
"""

FLOWER_TYPES = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets"
}

DEFAULT_STUDENTS = ["Alice",
                    "Bob",
                    "Charlie",
                    "David",
                    "Eve",
                    "Fred",
                    "Ginny",
                    "Harriet",
                    "Ileana",
                    "Joseph",
                    "Kincaid",
                    "Larry"]

class Garden:
    """Class to store students and their plants.

    Attributes:
        garden_dict (dict): Contains all the students and their flowers
    """

    def __init__(self, diagram, students=None):
        """Initializes the Garden with a lists of students and flowers."""

        if students is None:
            students=DEFAULT_STUDENTS

        students = sorted(students)
        rows = diagram.split("\n")
        length = len(rows[0]) // 2
        plant_codes = ["" for _ in range(length)]
        for index in range(length):
            for row in rows:
                plant_codes[index] += row[index*2:index*2+2]

        flowers = [[FLOWER_TYPES[char] for char in sequence] for sequence in plant_codes]

        self.garden_dict = dict(zip(students, flowers))

    def plants(self, student):
        """Function returns students list of flowers.

        Args:
            student (str): The name of the student

        Returns:
            list: The flowers that the student is responsible for
        """
        return self.garden_dict[student]