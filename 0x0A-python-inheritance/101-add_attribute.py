#!/usr/bin/python3
"""
Module: 101-add_attribute

This module adds a new attribute to an object if possible
"""


def add_attribute(obj, attr_name, attr_value):
    """
    This function adds a new attribute to an object if possible

    Raises:
        TypeError: if objects can't have new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
