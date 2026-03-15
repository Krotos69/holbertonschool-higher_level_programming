#!/usr/bin/python3
""" Define a Square class"""


class Square:
    """Defines Area of a square"""

    def __init__(self, size=0):
        """Initialize the square with a private size attribute."""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
