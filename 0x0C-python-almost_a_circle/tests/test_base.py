#!/usr/bin/python3

import unittest, os
from importlib.machinery import SourceFileLoader
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    # def test_module_docstring(self):

    def test_class_docstring(self):
        self.assertIsNotNone(Base.__doc__)

    # def test_methods_docstring(self):

    def test_initialization_with_empty_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

        Base._Base__nb_objects = 0

    def test_initialization_with_non_empty_id(self):
        self.assertTrue(Base(42), 42)

        Base._Base__nb_objects = 0

    def test_init_of_two_instances(self):
        b1 = Base(42)
        b2 = Base()
        self.assertTrue(b1.id == 42)
        self.assertTrue(b2.id == 1)

        Base._Base__nb_objects = 0

    def test_init_of_tree_instances(self):
        b1 = Base()
        b2 = Base(42)
        b3 = Base()
        self.assertTrue(b1.id == 1)
        self.assertTrue(b2.id == 42)
        self.assertTrue(b3.id == 2)

        Base._Base__nb_objects = 0

    def test_to_json_string(self):
        r = Rectangle(42, 42)
        print(Base.to_json_string(r.to_dictionary()))

if __name__ == '__main__':
    unittest.main()
