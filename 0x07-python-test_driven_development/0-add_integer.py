#!/usr/bin/python3
"""
Module: add_integer

This module contains a function that adds 2 integers.
"""


import doctest


def add_integer(a, b=98):
    """
    This function adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b


if __name__ == "__main__":
    doctest.testfile("tests/0-add_integer.txt")
