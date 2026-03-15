#!/usr/bin/python3
def add_integer(a, b=98):
    """ adds two integers or floats after casting to int."""
    if not isinstance(a, (int,float)):
        raise TypeError("a must be an ")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
