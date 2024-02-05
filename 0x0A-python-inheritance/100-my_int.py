#!/usr/bin/python3
""" class definition"""


class MyInt(int):

    def __init__(self, value):
        """innitialize value"""
        self = value

    def __eq__(self, other):
        """equal to value"""
        return (self - other != 0)

    def __ne__(self, other):
        """not equal to value"""
        return (self - other == 0)
