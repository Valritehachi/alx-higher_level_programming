#!/usr/bin/python3
"""function definition."""


import json


def load_from_json_file(filename):
    """json load."""
    with open(filename) as f:
        return json.load(f)
