#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(max_integer.__doc__)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_basic1(self):
        self.assertEqual(max_integer([1]), 1)

    def test_basic2(self):
        self.assertEqual(max_integer([1,2]), 2)

    def test_basic3(self):
        self.assertEqual(max_integer([-2, -1]), -1)

    def test_basic4(self):
        self.assertEqual(max_integer([-1, 0]), 0)

    def test_weird(self):
        self.assertEqual(max_integer(["Hel", "Wor", "str", "a"]), "str")

    def test_weird1(self):
        self.assertEqual(max_integer(["a", "b"]), "b")

    def test_weird2(self):
        self.assertRaises(TypeError, max_integer, ["a", "b", 1])

if __name__ == '__main__':
    unittest.main()
