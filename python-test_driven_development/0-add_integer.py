#!/usr/bin/python3
"""
Function that adds two integers.
"""


def add_integer(a, b=98):
    """Adds two integers or floats.

    Args:
        a: first number
        b: second number (default 98)

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: if a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for infinity BEFORE converting to int
    if a == float('inf') or a == float('-inf'):
        raise OverflowError("Cannot convert float infinity to int")
    if b == float('inf') or b == float('-inf'):
        raise OverflowError("Cannot convert float infinity to int")

    return int(a) + int(b)
