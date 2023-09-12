#!/usr/bin/python3
"""
Module: 12-pascal_triangle

This module contains a function that returns a list of integers
representing the Pascal's triangle.
"""


def pascal_triangle(n):
    """
    This function returns a list of integers representing
    the Pascal's triangle of 'n'.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            if j-1 < len(triangle[i-1]) and j < len(triangle[i-1]):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            else:
                row.append(1)
        row.append(1)
        triangle.append(row)

    return triangle
