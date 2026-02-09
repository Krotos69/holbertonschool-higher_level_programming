#!/usr/bin/python3
from abc import ABC, abstractmethod
"""Task 00 - Abstract Base Class"""

class Animal(ABC):
    """abstract base Class for Animals"""

    @abstractmethod
    def sound(self):
        """Method to be implemented by subclasses"""
        pass

class Dog(Animal):
    """Dog class inheriting from Animal"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat class inheriting from Animal"""
    def sound(self):
        return "Meow"
