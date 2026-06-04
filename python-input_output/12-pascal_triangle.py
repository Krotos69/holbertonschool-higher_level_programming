#!/usr/bin/python3
"""Module that defines Pascal's triangle funtion."""

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]  # first element

        # middle elements
        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])

        row.append(1)  # last element
        triangle.append(row)

    return triangle
