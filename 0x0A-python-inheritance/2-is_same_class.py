#!/usr/bin/python3
"""
Module: 2-is_same_class

this module contains a function that return a tatus if the object
is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    This function returns True is the object is exactly and instance
    of the specified class; otherwise False
    """
    return type(obj) is a_class
