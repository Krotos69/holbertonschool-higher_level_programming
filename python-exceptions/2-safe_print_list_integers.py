#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.
    Returns the number of integers printed.
    """
    count = 0
    try:
        for i in range(x):
            try:
                # We use a temporary variable to hold the formatted string
                # so we can print them on the same line.
                # Since we must print them on the same line,
                # we use end=' ' or similar, but the prompt says
                # "on the same line followed by a new line".
                    # The most robust way is to use print(..., end=' ')
                    # and then a final print() for the new line.
                print("{:d}".format(my_list[i]), end=' ')
                count += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        pass
    print("") # Print the final new line
    return count
