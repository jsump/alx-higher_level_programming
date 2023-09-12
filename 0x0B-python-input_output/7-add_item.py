#!/usr/bin/python3
"""
Module: 7-add_item

This module contains a script that adds all arguments
to a Python list, and then save them to a file.
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to text file,
    using a JSON representation.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”.
    """
    with open(filename, "r") as file:
        return json.load(file)


try:
    existing_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_data = []

new_data = existing_data + sys.argv[1:]

save_to_json_file(new_data, "add_item.json")
