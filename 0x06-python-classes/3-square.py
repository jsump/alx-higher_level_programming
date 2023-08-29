#!/usr/bin/python3
"""
Module: 3-square
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

    def __init__(self, size=0):
        """
        Initialize a sqaure with a given size.

        'size' must be an integer, otherwise raise a TypeError exception
        with the message 'size must be an integer'.
        If 'size' is less than 0, raise a ValueError exception message
        'size must be >= 0'

        Args:
        size (int): size of square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
