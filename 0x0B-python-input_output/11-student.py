#!/usr/bin/python3
""" Defines a `Student` class
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """ Constructor of the `Student` class

        Attrs:
            first_name (str): first name of Student
            last_name (str): last name of Student
            age (int): age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Prepers the instance for JSON serialization
        """
        return self.__dict__
