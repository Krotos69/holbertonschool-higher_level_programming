#!/usr/bin/python3
""" Module that defines Square class, which inherits from Rectangle. """

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Square class that inherits from Rectangle and defines a square
    with size. """

    def __init__(self, size):
        """ Validates using inherited integer_validator and initializes
        size as both width and height."""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of the square.	"""
        return self.__size * self.__size

    def __str__(self):
        """ Returns a string representation of the square.

        Returns:
            str: A string in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
