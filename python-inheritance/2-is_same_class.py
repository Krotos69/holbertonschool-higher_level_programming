#!/usr/bin/python3
""" Module that defines is_same_class funtion. """
def is_same_class(obj, a_class):
    """ Function that returns True if the object is exactly an instance of the specified class ; otherwise False.
    Args:
        obj: The object to be checked.
        a_class: The class to be compared against.
    Returns:
        True if obj is exactly an instance of a_class, False otherwise. """
    return type(obj) is a_class
