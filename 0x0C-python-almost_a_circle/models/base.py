#!/usr/bin/python3
import json
""" Module contains the `Base` class
"""


class Base:
    """ The `Base` class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor of the `Base` class

        Args:
            id: the uniqe id
        """
        if id is None:
            Base.__nb_objects += 1
            id = self.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of the instance"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file"""
        content = []

        if list_objs is not None:
            for i in list_objs:
                content.append(cls.to_dictionary(i))

        with open(cls.__name__ + ".json", 'w') as a_file:
            a_file.write(cls.to_json_string(content))

