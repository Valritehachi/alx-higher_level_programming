#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_None_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_bad_list(self):
        self.assertEqual( max_integer(["a","a"]), "a")

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
             max_integer([5, None])

    def test_max_1(self):
        self.assertEqual( max_integer([1,3,5,7]), 7)

if __name__ == '__main__':
    unittest.main()
