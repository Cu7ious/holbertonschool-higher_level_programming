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

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of the instance"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"

        return json.dumps(list_dictionaries)
