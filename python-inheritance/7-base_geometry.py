#!/usr/bin/python3
""" Module that defines BaseGeometry class, which provides basic 
validation tools for geometric objects."""


class BaseGeometry:
    """ BaseGeometry provides methods for validating geometry values
    and defien a placeholder for area computation. """

    def area(self):
        """ Raises an Exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the variable.
            value (any): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
