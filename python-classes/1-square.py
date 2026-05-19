#!/usr/bin/python3
"""defines a square class by priveat instance attribute size."""


class Square: # Define a class named Square
	"""A class that defines a square.""" 
    def __init__(self, size):
        """init method to initialize the size of the square."""
        self.__size = size # Private instance attribute to store the size of the square
