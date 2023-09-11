#!/usr/bin/python3
"""
Module: 3-is_kind_of_class

This module contains a function that returns a status if the onject
is an instance of or if the obj is an instance of a class inherited from
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object is an instance of,
    or if the object is an instance of a class inherited from
    the specified class; otherwise False
    """
    return isinstance(obj, a_class)
