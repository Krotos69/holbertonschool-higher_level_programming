#!/usr/bin/python3
""" Module that defines is_kind_of_class funtion. """


def inherits_from(obj, a_class):
    """ Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.
    Args:
        obj: The object to be checked.
        a_class: The class to be compared against.
    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise. """
    return isinstance(obj, a_class) and type(obj) is not a_class
