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
        self.__validate_integer("width", value)
        self.__validate_non_negative("width", value)
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
        self.__validate_integer("height", value)
        self.__validate_non_negative("height", value)
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
        self.__validate_integer("x", value)
        self.__validate_non_negative("x", value)
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
        self.__validate_integer("y", value)
        self.__validate_non_negative("y", value)
        self.__y = value

    def area(self):
        """
        This function calculates the area of a rectangle.
        """
        return self.__width * self.__height

    def __validate_integer(self, attribute_name, value):
        """
        This function checks if input is an interger.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
            return value

    def __validate_non_negative(self, attribute_name, value):
        """
        This function checks if input is a negative.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be > 0")
        return value

    def display(self):
        """
        This prints out REctangle instance with the character '#'
        in stdout.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " *self.x + "#" * self.width)

    def __str__(self):
        """
        This returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """
        This function assigns an argument to each attribute.
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
