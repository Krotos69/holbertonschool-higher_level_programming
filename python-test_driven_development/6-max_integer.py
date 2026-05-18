#!/usr/bin/python3
"""Function to find the max integer in a list."""


def max_integer(list=[]):
    """Return the max integer in a list of integers.
    If the list is empty, return None.
    """
    if len(list) == 0:
        return None
    max_value = list[0]
    for element in list:
        if element > max_value:
            max_value = element
    return max_value
