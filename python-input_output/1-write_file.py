#!/usr/bin/python3
""" function that writes a string to a text file (UTF8) and returns
    the number of characters written """


def write_file(filename="", text=""):
    """writes UTF-8 text file and returns the numbers of characters written """
    with open(filename, "w", encoding="utf8") as file:
        return file.write(text)
