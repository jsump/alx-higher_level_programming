#!/usr/bin/python3
"""
Module: 4-square
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
        size (int, optional): size of square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        """
        This retieves the given size of the square

        Returns:
            int: The given size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This sets the given size of square

        Args:
            value (int): The new given suare size.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        This can answer to the '<' comparator
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        This can answer to the '<=' comparator
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __eq__(self, other):
        """
        This can answer to the '==' comparator
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        This can answer to the '!=' comparator
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other):
        """
        This can answer to the '>' comparator
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        This can answer to the '>=' comparator
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
