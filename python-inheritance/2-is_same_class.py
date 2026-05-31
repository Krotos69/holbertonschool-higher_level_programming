#!/usr/bin/python3
""" Defines a function that checks if an object is an instance of a class that"""


def is_same_class(obj, a_class):
    """Returnd True if the object is exactly an instance of the specified class;
    ohterwise False."""
    return type(obj) is a_class
