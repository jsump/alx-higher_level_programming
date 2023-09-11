#!/usr/bin/python3
"""
Module: 7-base_geometry

This module contains a class BaseGeometry
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
        raise Exception("area() is not implemented")

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
