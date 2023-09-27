#!/usr/bin/python3
"""
Module: 0-add_integer.py

This module contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
        a (int): the first integer
        b (int): the second integer

    Returns:
        sum (int): addition of a and b
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
