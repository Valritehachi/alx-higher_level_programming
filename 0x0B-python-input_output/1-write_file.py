#!/usr/bin/python3
"""function definition."""


def write_file(filename="", text=""):
    """Write function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
