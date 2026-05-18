#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Suite de pruebas para max_integer."""

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-3, 10, -1, 5]), 10)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            max_integer([1, "hola", 3])

    def test_float_values(self):
        self.assertEqual(max_integer([1.5, 3.7, 2.2]), 3.7)

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["a", "z", "m"]), "z")

    def test_string_argument(self):
        self.assertEqual(max_integer("hola"), "o")  # max char


if __name__ == "__main__":
    unittest.main()
