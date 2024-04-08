#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" class definition"""


class Square(Rectangle):
    """shape definition"""
    def __init__(self, size):
        """ innitializer"""
        super().__init__(size, size)
