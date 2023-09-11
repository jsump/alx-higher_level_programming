#!/usr/bin/python3
"""
Module: 1-my_list

This module contains a class that inherits from a list.
"""


class MyList(list):
    """
    This class is used to inherit from "list"
    """


    def print_sorted(self):
        """
        This function prints the list in ascending sort.
        All elemtns will be of 'int' type.
        """
        sorted_list = sorted(self)
        print(sorted_list)
