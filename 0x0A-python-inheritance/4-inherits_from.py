#!/usr/bin/python3
"""
Module: 4-inherits_from

This module contains a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object
    is an instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
