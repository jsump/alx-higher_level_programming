#!/usr/bin/python3
"""
Module: 1-square
This module contains a class name Sqaure which represents a square.

The Square class is defined in this module to provide information
for creating square-related functionality.
"""


class Square:
    """
    This is a class that represents a square.
    It includes a private instance attribute 'size'
    that determines many computaions for a square.

    The size attribute is kept private to control
    the type and value of it's attribute

    """
    pass

    def __init__(self, size):
        """
        Initialize a sqaure with a given size.

        Args:
        size (int): size of square
        """
        self.__size = size
        pass
