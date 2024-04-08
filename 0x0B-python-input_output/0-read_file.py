#!/usr/bin/python3
"""function definition."""


def read_file(filename=""):
    """Printing file contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
