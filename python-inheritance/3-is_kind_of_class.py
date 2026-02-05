#!/usr/bin/python3
""" Module that defines is_kind_of_class funtion. """


def is_kind_of_class(obj, a_class):
    """ Function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise False.
    Args:
        obj: The object to be checked.
        a_class: The class to be compared against.
    Returns:
        True if obj is an instance of a_class or an instance of a class that
        inherited from a_class, False otherwise. """
    return isinstance(obj, a_class)
