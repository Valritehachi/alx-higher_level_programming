#!/usr/bin/python3
"""function definition."""


def append_write(filename="", text=""):
    """Appends function"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
