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
