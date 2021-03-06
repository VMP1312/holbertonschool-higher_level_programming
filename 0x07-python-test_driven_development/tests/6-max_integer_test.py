#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer
    test max_integer
    Return: one"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer((1, 2, 3)), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer(), None)
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        lists = [A, B, C]
        self.assertEqual(max_integer(lists), [7, 8, 9])
    if __name__ == '__main__':
        unittest.main()
