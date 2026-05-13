#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """search and replace all occurrences of an element by another in a new line list"""
    new_list =[]
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
