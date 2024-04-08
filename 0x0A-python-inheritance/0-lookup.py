#!/usr/bin/python3
"object definition"


def lookup(obj):
    """results"""
    if obj is None:
        return None
    return dir(obj)
