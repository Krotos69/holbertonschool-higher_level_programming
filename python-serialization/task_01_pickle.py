#!/usr/bin/env python3
"""
Module for serializing and deserializing a custom Python object
using the pickle module.
"""

import pickle


class CustomObject:
    """
    A simple custom class representing a person with attributes
    that can be serialized using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Parameters:
            name (str): Person's name.
            age (int): Person's age.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file.

        Parameters:
            filename (str): The file where the object will be saved.

        Returns:
            None if an error occurs, otherwise nothing.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file.

        Parameters:
            filename (str): The file to load the object from.

        Returns:
            CustomObject: The loaded object.
            None: If the file does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except Exception:
            return None
