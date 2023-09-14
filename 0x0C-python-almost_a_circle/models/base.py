#!/usr/bin/python3
"""
Module: models.base

This module contains a class Base which will be the "base"
of all the classes within this project.
The goal is to manage 'id' attribute in future classes to
avoid duplicating the same code(by extension. same bugs)
"""


class Base:
    """
    This class is created to act as the base for the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This function initializes the is attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
