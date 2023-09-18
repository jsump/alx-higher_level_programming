#!/usr/bin/python3
"""
Module: Square

This module contains a class Square that inherits from the
class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a class that inherits from the class Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This function initiates the size of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This funtion returns [Square] (<id>) <x>/<y> - <size>.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        This function sets the isze of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        This sets the value of the size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        This function assigns a key/value argument to teach attribute.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This functionreturns the dictionary representation of a Square.
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
