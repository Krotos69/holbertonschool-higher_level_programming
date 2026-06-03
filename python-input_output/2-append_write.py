#!/usr/bin/python3
"""define a function that appends text to a file"""


def append_write(filename="", text=""):
    """Append a string to text file and return the number of cha added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
