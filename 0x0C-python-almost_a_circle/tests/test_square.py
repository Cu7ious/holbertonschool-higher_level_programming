#!/usr/bin/python3
"""
This module contains the test cases for Square
"""
import unittest
from contextlib import contextmanager
import json
import sys
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquareClass(unittest.TestCase):
    """
    This class contains the test methods
    """
    @classmethod
    def setUpClass(cls):
        """
        sets up at beginning of class
        """
        Base._Base__nb_objects = 0
        cls.test = Square(10)
        cls.test1 = Square(1, 2, 5)
        cls.test2 = Square(5, 9, 8, 9)
        cls.test3 = Square(3, 8, 3, 4)

    def setUp(self):
        """
        resets variables
        """
        r1 = r2 = output = temp = 0

    def test_doctest(self):
        """
        test for docstring
        """
        self.assertIsNotNone(Base.__doc__)

    def test_class(self):
        """
        tests for class
        """
        self.assertTrue(isinstance(self.test, Square))

    def test_class_inheritance(self):
        """
        test for base inheritence
        """
        self.assertTrue(issubclass(type(self.test), Base))

    def test_class_init(self):
        """
        tests for id
        """
        self.assertEqual(self.test.id, 1)
        self.assertEqual(self.test1.id, 2)
        self.assertEqual(self.test2.id, 9)
        self.assertEqual(self.test3.id, 4)

    def test_class_variables(self):
        """
        tests for normal operation
        """
        self.assertEqual(self.test.size, 10)
        self.assertEqual(self.test1.size, 1)
        self.assertEqual(self.test2.size, 5)
        self.assertEqual(self.test3.size, 3)
        self.assertEqual(self.test1.x, 2)
        self.assertEqual(self.test2.x, 9)
        self.assertEqual(self.test3.x, 8)
        self.assertEqual(self.test1.y, 5)
        self.assertEqual(self.test2.y, 8)
        self.assertEqual(self.test3.y, 3)

    def test_input_errors(self):
        """
        tests for improper use
        """
        self.assertRaises(TypeError, Square, ())

    def test_integer_validator(self):
        """
        tests for integer validator
        """
        with self.assertRaises(TypeError, msg="width must be an integer"):
            temp = Square("a", "b")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            temp = Square(1, "b")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            temp = Square(1, 1, "b")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            temp = Square(-1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            temp = Square(1, -1, -1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            temp = Square(1, 2, -1, -1)

    def test_area(self):
        """
        tests for area
        """
        self.assertEqual(self.test.area(), 100)
        self.assertEqual(self.test1.area(), 1)
        self.assertEqual(self.test2.area(), 25)
        self.assertEqual(self.test3.area(), 9)

    def test_str(self):
        """
        tests for string rep of instances
        """
        self.assertEqual(str(self.test), "[Square] (1) 0/0 - 10")
        self.assertEqual(str(self.test1), "[Square] (2) 2/5 - 1")
        self.assertEqual(str(self.test2), "[Square] (9) 9/8 - 5")
        self.assertEqual(str(self.test3), "[Square] (4) 8/3 - 3")

    def test_update_0(self):
        """
        tests for update via args
        """
        temp = Square(5)
        self.assertEqual(temp.size, 5)
        temp.update(3, 4)
        self.assertEqual(temp.id, 3)
        self.assertEqual(temp.size, 4)
        temp.update(9, 8, 7, 6)
        self.assertEqual(temp.id, 9)
        self.assertEqual(temp.size, 8)
        self.assertEqual(temp.x, 7)
        self.assertEqual(temp.y, 6)

    def test_update_1(self):
        """
        test for kwargs
        """
        temp = Square(9, 8, 7, 6)
        self.assertEqual(str(temp), "[Square] (6) 8/7 - 9")
        temp.update(id=1)
        self.assertEqual(temp.id, 1)
        temp.update(size=3)
        self.assertEqual(temp.size, 3)
        temp.update(x=4)
        self.assertEqual(temp.x, 4)
        temp.update(y=12)
        self.assertEqual(temp.y, 12)

    def test_getter_setter(self):
        """
        test for setter / getter
        """
        temp = Square(5)
        self.assertEqual(temp.size, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            temp.size = "9"

    def test_to_dictionary(self):
        """
        test for dictionary output
        """
        temp = Square(10, 2, 1, 9)
        r1 = temp.to_dictionary()
        self.assertEqual(r1, {'id': 9, 'x': 2, 'size': 10, 'y': 1})

    def test_to_json_string(self):
        """
        tests for converting to json
        """
        temp = Square(10, 2, 1, 9)
        s1 = temp.to_dictionary()
        s2 = temp.to_json_string(s1)
        self.assertEqual(s2, json.dumps(s1))

    def test_json_string_to_file(self):
        """
        tests for saving to file
        """
        temp1 = Square(5, 6, 2, 9)
        temp2 = Square(1, 2, 3, 4)
        Square.save_to_file([temp1, temp2])
        with open("Square.json") as file:
            r1 = file.read()
            r2 = [temp1.to_dictionary(), temp2.to_dictionary()]
            self.assertEqual(json.dumps(r2), r1)

    def test_from_json(self):
        """
        tests for converting from json string
        """
        temp1 = Square(5, 6, 2, 9)
        temp2 = Square(1, 2, 3, 4)
        r1 = [temp1.to_dictionary(), temp2.to_dictionary()]
        self.assertTrue(isinstance(r1, list))
        r2 = Square.to_json_string(r1)
        self.assertTrue(isinstance(r2, str))
        r3 = Square.from_json_string(r2)
        self.assertTrue(isinstance(r3, list))

    def test_create(self):
        """
        tests new instance is independant
        """
        r1 = Square(4, 8, 9)
        dict1 = r1.to_dictionary()
        r2 = Square.create(**dict1)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """
        tests data ca be loaded
        """
        r1 = Square(1, 1, 1)
        r2 = Square(2, 2, 2)
        lists = [r1, r2]
        Square.save_to_file(lists)
        output = Square.load_from_file()
        self.assertTrue(isinstance(output, list))
        o1 = output[0]
        o2 = output[1]
        self.assertTrue(isinstance(o1, Square))
        self.assertTrue(isinstance(o2, Square))
        self.assertEqual(str(r1), str(o1))
        self.assertEqual(str(r2), str(o2))

    def test_return_empty(self):
        """
        tests when passing none
        """
        output = Square.to_json_string(None)
        self.assertEqual(output, "[]")
        output = Square.to_json_string([])
        self.assertEqual(output, "[]")

    def test_save_empty(self):
        """
        tests when list is empty
        """
        lists = []
        Square.save_to_file(lists)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_None(self):
        """
        testwhen input is None
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_no_file(self):
        """
        tests when there is no file
        """
        try:
            Square.save_to_file(None)
            os.remove("Square.json")
        except BaseException:
            pass
        self.assertEqual(Square.load_from_file(), [])

