#!/usr/bin/python3
"""
Module: 11-rectangle

This module contains a class that inherits from BaseGeometry
(9-base_geometry.py)
"""


class BaseGeometry():
    """
    This is a class that creates the base for geometry
    """

    def area(self):
        """
        This functioncalculates the area.

        Raises:
            Exception: with message 'area() is not implemented'
        """
        pass

    def integer_validator(self, name, value):
        """
        This function validates value.

        Assume name is always a string.

        Raises:
            TypeError: if value not an integer
            ValueError: if value less than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This is a class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initiates a rectangles height and width.
        width and height must be private. No getter or setter.
        width and height must be positive integers,
        validated by integer_validatorself.__width = 0
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This calculates the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        This function Should return the rectangle description.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    This is a class that inherits from Rectangle"
    """
    def __init__(self, size):
        """
        Initiates the size of a square
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        This calculates teh area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        This function Should return the square description.
        """
        return f"[Square] {self.__size}/{self.__size}"
