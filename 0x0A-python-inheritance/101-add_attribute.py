#!/usr/bin/python3
""" defines an attribute"""


def add_attribute(mc, name, value):
    """adds to the attribute"""
    if not '__dict__' in dir(mc):
        raise TypeError("can't add new attribute")
    setattr(mc, name, value)
