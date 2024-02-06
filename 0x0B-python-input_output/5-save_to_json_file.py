#!/usr/bin/python3
"""function definition."""


import json


def save_to_json_file(my_obj, filename):
    """save to json."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
