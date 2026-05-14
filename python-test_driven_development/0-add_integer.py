#!/usr/bin/python3
"""
Function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to int).

    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98

    Returns:
        int: the sum of a and b after casting to int

    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
