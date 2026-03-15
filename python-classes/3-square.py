#!/usr/bin/python3
""" Define a Square class"""


class Square:
    """Defines Area of a square"""

    def __init__(self, size=0):
        """Initialize the square with a private size attribute."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
