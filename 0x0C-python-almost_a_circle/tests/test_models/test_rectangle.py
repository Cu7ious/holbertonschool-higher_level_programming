#!/usr/bin/python3
""" Tests for the `Rectangle` class"""
import unittest
import json
import sys

from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Unit tests for the `Rectangle` class"""

    def test_docstring(self):
        """ Docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_is_instance(self):
        """ Is instance"""
        self.assertTrue(isinstance(Rectangle(1, 1), Rectangle))
        Base._Base__nb_objects = 0

    def test_is_subclass(self):
        """ Is subclass"""
        self.assertTrue(issubclass(type(Rectangle(1, 1)), Base))
        Base._Base__nb_objects = 0

    def test_empty_init(self):
        """ Empty init"""
        self.assertRaises(TypeError, Rectangle, ())
        self.assertRaises(TypeError, Rectangle, (1))

    def test_init_with_width_less_or_equal_0(self):
        """ Init with width <= 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)
        Base._Base__nb_objects = 0

    def test_init_with_height_less_or_equal_0(self):
        """ Init with height <= 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)
        Base._Base__nb_objects = 0

    def test_width_is_not_int(self):
        """ Width is not int"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 1)
        Base._Base__nb_objects = 0

    def test_height_is_not_int(self):
        """ Height is not int"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "1")
        Base._Base__nb_objects = 0

    def test_x_is_not_int(self):
        """ x is not int"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "1", -1)
        Base._Base__nb_objects = 0

    def test_x_is_less_than_0(self):
        """ x is < 0"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, -1)
        Base._Base__nb_objects = 0

    def test_y_is_not_int(self):
        """ y is not int"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, "1")
        Base._Base__nb_objects = 0

    def test_y_is_less_than_0(self):
        """ x is < 0"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 0, -1)
        Base._Base__nb_objects = 0

    def test__str__(self):
        """ __str__"""
        self.assertEqual(Rectangle(1, 1, 0, 0).__str__(),
                         "[Rectangle] (1) 0/0 - 1/1")
        Base._Base__nb_objects = 0

    def test_area(self):
        """ Area"""
        self.assertEqual(Rectangle(2, 2, 0, 0).area(), 4)
        Base._Base__nb_objects = 0

    def test_update_args(self):
        """ Update with args"""
        r = Rectangle(1, 1, 0, 0)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        Base._Base__nb_objects = 0

    def test_update_kwargs(self):
        """ Update with kwargs"""
        r = Rectangle(1, 1, 0, 0)
        r.update(id=2, width=2, height=2, x=2, y=2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        """ to_dictionary"""
        temp = Rectangle(1, 1, 1, 1)
        r1 = temp.to_dictionary()
        r2 = {"id": 1,  "height": 1, "width": 1, "x": 1, "y": 1}
        self.assertEqual(r1, r2)
        Base._Base__nb_objects = 0

    def test_to_json_string(self):
        """ JSON string"""
        temp = Rectangle(1, 1, 1, 1, 1)
        r1 = temp.to_dictionary()
        r2 = temp.to_json_string(r1)
        self.assertEqual(r2, json.dumps(r1))
        Base._Base__nb_objects = 0

    def test_json_string_to_file(self):
        """ From json file"""
        temp1 = Rectangle(1, 1, 1, 1, 1)
        temp2 = Rectangle(5, 6, 7, 8, 9)
        Rectangle.save_to_file([temp1, temp2])
        with open("Rectangle.json") as file:
            r1 = file.read()
            r2 = [temp1.to_dictionary(), temp2.to_dictionary()]
            self.assertEqual(json.dumps(r2), r1)
        Base._Base__nb_objects = 0

    def test_from_json(self):
        """ From json"""
        temp1 = Rectangle(1, 1, 1, 1, 1)
        temp2 = Rectangle(5, 6, 7, 8, 9)
        r1 = [temp1.to_dictionary(), temp2.to_dictionary()]
        self.assertTrue(isinstance(r1, list))
        r2 = Rectangle.to_json_string(r1)
        self.assertTrue(isinstance(r2, str))
        r3 = Rectangle.from_json_string(r2)
        self.assertTrue(isinstance(r3, list))
        Base._Base__nb_objects = 0

    def test_create(self):
        """ Create method"""
        r1 = Rectangle(1, 1, 1)
        dict1 = r1.to_dictionary()
        r2 = Rectangle.create(**dict1)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)
        Base._Base__nb_objects = 0

    def test_load_from_file(self):
        """ Loading from json file"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(5, 6, 7, 8, 2)
        lists = [r1, r2]
        Rectangle.save_to_file(lists)

        out = Rectangle.load_from_file()
        self.assertTrue(isinstance(out, list))

        self.assertTrue(isinstance(out[0], Rectangle))
        self.assertTrue(isinstance(out[1], Rectangle))
        self.assertEqual(str(r1), str(out[0]))
        self.assertEqual(str(r2), str(out[1]))
        Base._Base__nb_objects = 0

    def test_return_empty(self):
        """ json_to_string returns none"""
        output = Rectangle.to_json_string(None)
        self.assertEqual(output, "[]")
        output = Rectangle.to_json_string([])
        self.assertEqual(output, "[]")

    def test_save_empty(self):
        """ Empty list input"""
        lists = []
        Rectangle.save_to_file(lists)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_None(self):
        """ Input is none"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_no_file(self):
        """ File doesnt exist"""
        try:
            Rectangle.save_to_file(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass

        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_empty_file(self):
        """ File is empty"""
        try:
            Rectangle.save_to_file(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass

        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_class_basic_init(self):
        """ Ids"""
        self.assertEqual(Rectangle(1, 1).id, 1)
        Base._Base__nb_objects = 0
