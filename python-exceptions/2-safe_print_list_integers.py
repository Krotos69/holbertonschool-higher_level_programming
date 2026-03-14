#!/usr/bin/python3
"""Write a function that prints the first x elements of a list and only integers"""
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Try to access the element (may raise IndexError)
            value = my_list[i]

            # Try to print as integer (may raise TypeError or ValueError)
            print("{:d}".format(value), end="")
            count += 1

        except (TypeError, ValueError):
            # Not an integer → skip silently
            continue

    print()  # New line after printing
    return count
