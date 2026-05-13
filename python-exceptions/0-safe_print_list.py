#!/usr/bin/python3
"""Prints x elements of a list.
    
    Args:
        my_list (list): The list to print from.
        x (int): The number of elements to print.

    Returns:
        int: The number of elements actually printed.
"""


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print(my_list[count], end=" ")
            count += 1
    except IndexError:
        pass
    print()
    return count
