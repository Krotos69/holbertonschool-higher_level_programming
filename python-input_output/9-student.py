#!/usr/bin/python3
"""
Docstring for 9-student
"""

from typing import Self


class Student:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrive a dictionary representation of student instance"""
        return self.__dict__
