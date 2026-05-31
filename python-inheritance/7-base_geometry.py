#!/usr/bin/python3
""" Defines BaseGeometry class used for geometry operations. """


class BaseGeometry:
    """ BaseGeometry class. """

    def area(self):
        """ Raises an Exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that value is a positive integer. """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
