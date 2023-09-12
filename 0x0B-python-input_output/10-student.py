#!/usr/bin/python3
"""
Module: 9-student

This module contains a class Stdent that defines a student.
"""


def class_to_json(obj):
    """
    This function returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.
    """
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, (str, int, bool)):
        return obj
    else:
        return {attr: class_to_json(getattr(obj, attr))
                for attr in dir(obj) if not attr.startswith('__')}


class Student:
    """
    This class defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        This function initializes the public instane attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function retrieves a dictionary representation of
        a student.
        """
        attributes = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
        }
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
