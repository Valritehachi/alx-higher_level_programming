#!/usr/bin/python3
"""function definition."""


class Student:
    """class representation."""

    def __init__(self, first_name, last_name, age):
        """Initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """json representation."""
        return self.__dict__
