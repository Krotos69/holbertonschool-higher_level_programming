#!/usr/bin/python3
""" Module that defines Rectangle class, which inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry and defines a rectangle
    with width and height. """

    def __init__(self, width, height):
        """ Validates using inherited integer_validator and initializes
        width and height."""
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        """ Atribute initialization after validation."""
        self.__width = width
        self.__height = height

    def area(self):
        """ Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string representation of the rectangle.

        Returns:
            str: A string in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
