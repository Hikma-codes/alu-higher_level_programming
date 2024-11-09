#!/usr/bin/python3
"""This is the module for MyList class."""


class MyList(list):
    """This os the custom list class."""

    def print_sorted(self):
        """This prints the list in ascending or minimum order."""
        print(sorted(self))
