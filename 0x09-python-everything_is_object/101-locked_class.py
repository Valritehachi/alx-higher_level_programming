#!/usr/bin/python3
"""locked class."""


class LockedClass:
    """
    donot allow user to create new attributes
    for anything but 'first_name'.
    """

    __slots__ = ["first_name"]
