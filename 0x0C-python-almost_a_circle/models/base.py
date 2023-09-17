#!/usr/bin/python3
"""
Module: models.base

This module contains a class Base which will be the "base"
of all the classes within this project.
The goal is to manage 'id' attribute in future classes to
avoid duplicating the same code(by extension. same bugs)
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This returns the JSON string representaion of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function writes the JSON string representaion of list_objs
        to a file.
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list of JSON string representing the
        list of dictionaries.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)
