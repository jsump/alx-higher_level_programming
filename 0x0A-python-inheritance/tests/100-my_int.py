#!/usr/bin/python3
"""
Module: my_int

This module contains a xlass MyInt that inherits from int
"""


class MyInt(int):
    """
    this class inherits from int
    """

    def __eq__(self, other):
        """
        This function checks the behaviour of the == operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        This function checks to inequality and returns
        the opposite result
        """
        return super().__eq__(other)
