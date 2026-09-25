"""
Module to store a school roster.
"""
class School:
    """Class to store students in the school by grade and name.

    Attributes:
        students (dict): Student's names and grades
        added_list (list): Successfull and failed attempts to add students to the school
    """
    def __init__(self):
        """Function to initialize the school's lists to store student's information."""
        self.students = {}
        self.added_list = []

    def add_student(self, name, grade):
        """Function to add students to the school."""
        if name not in self.students:
            self.students[name] = grade
            self.added_list.append(True)
        else:
            self.added_list.append(False)

    def roster(self):
        """Function returns school's students list sorted by grades and names in alphabetical order.

        Returns:
            list: List of student sorted by grade and names
        """
        return [pair[0] for pair in (sorted(self.students.items(), key = lambda item: (item[1], item[0])))]

    def grade(self, grade_number):
        """Function returns spesific grade's list of students sorted by alphabetical order.

        Args
            grade_number (int): The number of the desired grade list

        Returns:
            list: Spesific grade's list of students sorted by alphabetical order
        """
        return sorted([student for student, grade in self.students.items() if grade == grade_number])

    def added(self):
        """Function returns list with indication whether different students added successfully or not.

        Returns:
            list: List with indication whether different students added successfully or not
        """
        return self.added_list