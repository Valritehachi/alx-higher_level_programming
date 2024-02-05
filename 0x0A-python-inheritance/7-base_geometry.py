#!/usr/bin/python3
"""class definition"""


class BaseGeometry:
    """class definition"""
    def area(self):
        """area definition"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """interger validator"""
        if not type(value) == int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
