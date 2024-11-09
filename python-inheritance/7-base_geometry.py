#!/usr/bin/python3
"""This defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """To reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """To vaalidate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): To validate the parameter.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} should be an integer".format(name))
        if value <= 0:
            raise ValueError("{} should be greater than 0".format(name))
