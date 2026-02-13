#!/usr/bin/python3
""" Write a function that reads a text file (UTF8)
    and prints it to stdout """


def read_file(filename=""):
    """ print the contents of UTF8 text file"""
    
    with open(filename, encoding="UTF8") as file:
        print(file.read(), end="")
