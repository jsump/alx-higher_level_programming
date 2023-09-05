#!/usr/bin/python3
"""
Module: 9-rectangle

This module defines a rectangle based on 8-rectangle.py.
It contains a class name Rectangle which represents a square.
"""


class Rectangle:
    """
    This is a class that represents a rectangle.
    It includes a private instance 'width'
    that determines the computations of a rectangle.

    The width attribute is kept private to control
    the type and value of its attribute.

    Count the number of instances which whill be initialized
    to 0. There will be an inc during each new instance
    instantiation and dec during each instance deletion.

    Print a symbol used for string repesentation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with a given width and height

        Args:
            width (int): width of a rectangle
            height (int): height of rectangle
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        This calculates the area of a rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        This calculates the perimeter of a rectangle

        If width and height is equal to 0, perimeter = 0

        Returns:
            int : the aperimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        This is to print the rectabgle with the character '#'.
        If width or height = 0, perimeter = 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        This is to returb a string representation of the rectangle
        to be able to create a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.__height})"

    def __del__(self):
        """
        This is to print the message Bye rectangle...
        (... being 3 dots not ellipsis) when an instance of
        Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This returns the biggest rectangle based on the area.

        Raises:
            TypeError: if rect_1 is not an instance of Rectangle,
            with the message rect_1 must be an instance of Rectangle.
            TypeError: if rect_2 is not an instance pf Rectangle,
            with the message rect_2 must be an instance of Rectangle.

        Returns rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        This returns a new Rectangle instance with
        width == height == size.
        """
        return cls(size, size)