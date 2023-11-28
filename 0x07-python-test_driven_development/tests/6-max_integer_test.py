#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer([..])"""

    def test_positive_integers(self):
        """Test max_integer with lists of positive integers"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 4, 3, 8, 4, 2]), 8)
        self.assertEqual(max_integer([8, 3, 8, 3, 8, 4, 8]), 8)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([2, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)

    def test_zero(self):
        """Test max_integer with a list of 0s"""

        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)

    def test_negative_integers(self):
        """Test max_integer with a list of negative integers"""

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """
        Test max_integer with lists of integers
        of mixed signs
        """
        self.assertEqual(max_integer([-1, -2, 0, -3, -4]), 0)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_large_integers(self):
        """Test max_integer with lists of large integers"""

        self.assertEqual(max_integer([10 ** 10, 2, 3, 4]), 10 ** 10)
        self.assertEqual(max_integer([1000000, 5000000, 3000000]), 5000000)

    def test_large_list(self):
        """Test max_integer with a large list"""

        self.assertEqual(max_integer([-50, 0, 10, -20, 30, -40, 0, 5, 15,
                                      -25, 35, -45, 0, 25, -15, 20, -30, 40,
                                      -10, 50, 0, -5, 45, -35, 30, 0, -20, 10,
                                      -40, 50, -30, 0, 35, -25, 15, -5, 25, 0,
                                      -45, 20, -35, 45, 0, -15, 30, -10, 40,
                                      50, 0, 5, -40, 35, -45, 10, 0, -20, 50,
                                      30, 15, 20, 0, -25, -5, -35, -15, 25, 0,
                                      -50, -40, 5, 30, -20, 101, 35, -10, 20,
                                      45, 10, 0, -30, 15, -25, 25, -5, 0, 40,
                                      -35, 30, -20, 45, 0, -10, 50, -15, 5,
                                      -25, 0, 20, -30, -40, 35, -50, 0, -5,
                                      10, -45, 25, -15, 0, 30, -20, 40, -35,
                                      15]), 101)

    def test_empty_list(self):
        """Test with an empty list"""

        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
