#!/usr/bin/python3
""" class definition"""


class MyList(list):

    def print_sorted(self):
        """ sorting"""
        print(sorted(self))
