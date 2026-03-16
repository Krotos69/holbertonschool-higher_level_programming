#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer."""

    def test_ordered_list(self):
        """Test a list where the max is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list where the max is in the middle."""
        self.assertEqual(max_integer([1, 3, 2, 4, 3]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max is at the beginning."""
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def test_one_element_list(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9, -1]), -1)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers."""
        self.assertEqual(max_integer([-10, 5, 3, -1]), 5)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 3.2, 2.8]), 3.2)

    def test_mixed_ints_floats(self):
        """Test a list with ints and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """Test a string (iterable of chars)."""
        self.assertEqual(max_integer("hello"), "o")

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_none_argument(self):
        """Test passing None as argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        """Test passing a non-iterable."""
        with self.assertRaises(TypeError):
            max_integer(123)


if __name__ == '__main__':
    unittest.main()
