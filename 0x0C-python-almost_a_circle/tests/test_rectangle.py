#!/usr/bin/python3
"""
Tests for the `Class` class
"""
import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import contextmanager
import json
import sys


class TestRectangleClass(unittest.TestCase):
    """
    Class contains the test functions
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up test cases for general tests
        """
        Base._Base__nb_objects = 0
        cls.test = Rectangle(10, 2)
        cls.test1 = Rectangle(1, 2, 5, 5)
        cls.test2 = Rectangle(5, 9, 8, 7, 9)
        cls.test3 = Rectangle(3, 8, 3, 4)

    def setup(self):
        """
        resets variables
        """
        r1 = r2 = temp = temp1 = output = 0

    def test_pep8_model(self):
        """
        Tests for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        pepp = style.check_files(['models/base.py'])
        self.assertEqual(pepp.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        pepp = style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(pepp.total_errors, 0, "fix pep8")

    def test_doctest(self):
        """
        tests for docstring
        """
        self.assertIsNotNone(Base.__doc__)

    def test_class(self):
        """
        check for class
        """
        self.assertTrue(isinstance(self.test, Rectangle))

    def test_class_inheritance(self):
        """
        check for inheritence
        """
        self.assertTrue(issubclass(type(self.test), Base))

    def test_class_init(self):
        """
        check for ids
        """
        self.assertEqual(self.test.id, 1)
        self.assertEqual(self.test1.id, 2)
        self.assertEqual(self.test2.id, 9)
        self.assertEqual(self.test3.id, 3)

    def test_class_variables(self):
        """
        test for variables
        """
        self.assertEqual(self.test.width, 10)
        self.assertEqual(self.test1.width, 1)
        self.assertEqual(self.test2.width, 5)
        self.assertEqual(self.test3.width, 3)
        self.assertEqual(self.test.height, 2)
        self.assertEqual(self.test1.height, 2)
        self.assertEqual(self.test2.height, 9)
        self.assertEqual(self.test3.height, 8)
        self.assertEqual(self.test1.x, 5)
        self.assertEqual(self.test2.x, 8)
        self.assertEqual(self.test3.x, 3)
        self.assertEqual(self.test1.y, 5)
        self.assertEqual(self.test2.y, 7)
        self.assertEqual(self.test3.y, 4)

    def test_input_errors(self):
        """
        test for empty inputsor incorrect inputs
        """
        self.assertRaises(TypeError, Rectangle, ())
        self.assertRaises(TypeError, Rectangle, (1))

    def test_integer_validator(self):
        """
        tests theinteger validator
        """
        with self.assertRaises(TypeError, msg="width must be an integer"):
            temp = Rectangle("a", "b")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            temp = Rectangle(1, "b")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            temp = Rectangle(-1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            temp = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            temp = Rectangle(1, 1, -1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            temp = Rectangle(1, 2, 0, -1)

    def test_area(self):
        """
        check area
        """
        self.assertEqual(self.test.area(), 20)
        self.assertEqual(self.test1.area(), 2)
        self.assertEqual(self.test2.area(), 45)
        self.assertEqual(self.test3.area(), 24)

    def test_str(self):
        """
        tests str rep of the instance
        """
        self.assertEqual(str(self.test), "[Rectangle] (1) 0/0 - 10/2")
        self.assertEqual(str(self.test1), "[Rectangle] (2) 5/5 - 1/2")
        self.assertEqual(str(self.test2), "[Rectangle] (9) 8/7 - 5/9")
        self.assertEqual(str(self.test3), "[Rectangle] (3) 3/4 - 3/8")

    def test_update_0(self):
        """
        simple update test
        """
        temp = Rectangle(5, 6)
        self.assertEqual(temp.width, 5)
        self.assertEqual(temp.height, 6)
        temp.update(3, 4)
        self.assertEqual(temp.id, 3)
        self.assertEqual(temp.width, 4)
        temp.update(9, 8, 7, 6, 5)
        self.assertEqual(temp.id, 9)
        self.assertEqual(temp.width, 8)
        self.assertEqual(temp.height, 7)
        self.assertEqual(temp.x, 6)
        self.assertEqual(temp.y, 5)

    def test_update_1(self):
        """
        update using keys
        """
        temp = Rectangle(9, 8, 7, 6, 5)
        self.assertEqual(str(temp), "[Rectangle] (5) 7/6 - 9/8")
        temp.update(id=1)
        self.assertEqual(temp.id, 1)
        temp.update(height=2)
        self.assertEqual(temp.height, 2)
        temp.update(width=3)
        self.assertEqual(temp.width, 3)
        temp.update(x=4)
        self.assertEqual(temp.x, 4)
        temp.update(y=12)
        self.assertEqual(temp.y, 12)

    def test_to_dictionary(self):
        """
        test dictionary output
        """
        temp = Rectangle(10, 21, 1, 9, 5)
        r1 = temp.to_dictionary()
        r2 = {'x': 1, 'y': 9, 'id': 5, 'height': 21, 'width': 10}
        self.assertEqual(r1, r2)

    def test_to_json_string(self):
        """
        test json string
        """
        temp = Rectangle(10, 7, 2, 8, 1)
        r1 = temp.to_dictionary()
        r2 = temp.to_json_string(r1)
        self.assertEqual(r2, json.dumps(r1))

    def test_json_string_to_file(self):
        """
        test from json file
        """
        temp1 = Rectangle(5, 6, 2, 9, 4)
        temp2 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([temp1, temp2])
        with open("Rectangle.json") as file:
            r1 = file.read()
            r2 = [temp1.to_dictionary(), temp2.to_dictionary()]
            self.assertEqual(json.dumps(r2), r1)

    def test_from_json(self):
        """
        test from json
        """
        temp1 = Rectangle(5, 6, 2, 9, 4)
        temp2 = Rectangle(1, 2, 3, 4, 5)
        r1 = [temp1.to_dictionary(), temp2.to_dictionary()]
        self.assertTrue(isinstance(r1, list))
        r2 = Rectangle.to_json_string(r1)
        self.assertTrue(isinstance(r2, str))
        r3 = Rectangle.from_json_string(r2)
        self.assertTrue(isinstance(r3, list))

    def test_create(self):
        """
        test for created independant instances
        """
        r1 = Rectangle(4, 8, 9)
        dict1 = r1.to_dictionary()
        r2 = Rectangle.create(**dict1)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """
        test for loading from json file
        """
        r1 = Rectangle(1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2)
        lists = [r1, r2]
        Rectangle.save_to_file(lists)
        output = Rectangle.load_from_file()
        self.assertTrue(isinstance(output, list))
        o1 = output[0]
        o2 = output[1]
        self.assertTrue(isinstance(o1, Rectangle))
        self.assertTrue(isinstance(o2, Rectangle))
        self.assertEqual(str(r1), str(o1))
        self.assertEqual(str(r2), str(o2))

    def test_return_empty(self):
        """
        test when input is none
        """
        output = Rectangle.to_json_string(None)
        self.assertEqual(output, "[]")
        output = Rectangle.to_json_string([])
        self.assertEqual(output, "[]")

    def test_save_empty(self):
        """
        test for empty list input
        """
        lists = []
        Rectangle.save_to_file(lists)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_None(self):
        """
        test when input is none
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_no_file(self):
        """
        test when file doesnt exist
        """
        try:
            Rectangle.save_to_file(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_empty_file(self):
        """
        test when file is empty
        """
        try:
            Rectangle.save_to_file(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])
