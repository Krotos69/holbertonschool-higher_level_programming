#!/usr/bin/python3
""" Module defines a list subclass than can display its elements in sorted order. """
class MyList(list):
    """ this class inherits from list type by adding a method to print sorted list """
    def print_sorted(self):
        """ method that prints the elements of the list in sorted order """
        print(sorted(self))
