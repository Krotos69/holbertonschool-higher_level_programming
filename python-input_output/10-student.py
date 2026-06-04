#!/usr/bin/python3
""" Write a class Student that defines a student"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        def  to_json(self, attrs=None):
            if type(attrs) is list and all(type(i) is str for i in attrs):
                new_dict = {}
                for i in attrs:
                    if i in self.__dict__:
                        new_dict[i] =self.__dict__[i]
                        return new_dict
            return self.__dict__
