#!/usr/bin/python3
"""
    Print the first x elements of a list that are integers.
    Return the number of integers printed.
"""


def safe_print_list_integers(my_list=[], x=0):

    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count
