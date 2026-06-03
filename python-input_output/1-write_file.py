#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the characters written."""

    with open(filename, "w", encoding="utf-8") as file:
        # Open the file in write mode with UTF-8 encoding
        return file.write(text)
