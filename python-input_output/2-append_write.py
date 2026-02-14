#!/usr/bin/python3
""" Write a function that appends a string at the end of a text """


def append_write(filename="", text=""):
    """ Appends a string at the end of a UTF-* txt file
    and returns the # of chars added."""
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
