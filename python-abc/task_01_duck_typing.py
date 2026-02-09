#!/usr/bin/python3
from abc import ABC, abstractmethod

"""Task 01 - Duck Typing"""

class Shape(ABC):
	"""Base class for shapes"""

@abstractmethod
def area(self):
    """Return the area of the shape"""
    pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape"""
	
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159265 *self.radius

class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
def shape_info(shape):
	"""Print the area and perimeter of a shape"""
	print(f"Area: {shape.area()}")
	print(f"Perimeter: {shape.perimeter()}")
