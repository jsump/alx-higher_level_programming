#!/usr/bin/python3
"""
Module: Rectangle

This module contains a class inherits from Base.
"""


from models.base import Base


class Rectangle(Base):
    """
    This class inherits from Base with private attributes,
    each with their own public getter and setter.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This function initializes the attributes of a rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        This function retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This function sets the value of the width
        """
        self.__width = value

    @property
    def height(self):
        """
        This function retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This sets the value of the height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """
        This retrives the var x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This sets the value of x.
        """
        self.__x = value

    @property
    def y(self):
        """
        This retrives the var y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This sets the value of y.
        """
        self.__y = value

    def area(self):
        """
        This function calculates the area of a rectangle.
        """
        pass
