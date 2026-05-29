#!/usr/bin/python3
""" Module that defines is_kind_of_class funtion. """


def is_kind_of_class(obj, a_class):
    """ Returns True if the objects is an isntance of a class
    that inheritance from the specified class; otherwise False."""
    return isinstance(obj, a_class)
