#!/usr/bin/python3
"""
Module: 1-rectangle

This module defines a rectangle based on 0-rectangle.py.
It contains a class name Rectangle which represents a square.
"""


class Rectangle:
    """
    This is a class that represents a rectangle.
    It includes a private instance 'width'
    that determines the computations of a rectangle.

    The width attribute is kept private to control
    the type and value of its attribute.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with a given width

        Args:
            width (int): width of a rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        This retrieves the given width of a rectangle

        Returns:
            width (int): the given width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This sets the value of the width of the rectangle

        Args:
            value (int): The new given width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        This retrieves the given height of a rectangle

        Returns:
            height (int): the given height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This sets the value of the height of a rectangle

        Args:
            value (int): the new given height of a rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
