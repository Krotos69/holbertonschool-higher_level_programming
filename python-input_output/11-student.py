#!/usr/bin/python3
"""
Docstring for 11-student
"""
class Student:
    """define student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation in Student instance"""
        if isinstance(attrs, list) and \
                all(isinstance(attr, str) for attr in attrs):
            return {
                    key: value for key, value in self.__dict__.items()
                    if key in attrs
                    }
        return self.__dict__
    
    def reload_from_json(self, json):
        """Load student data from a dictionary """
        for key, value in json.items():
            setattr(self, key, value)
