#!/usr/bin/python3

def lookup(obj):
    if obj is None:
        return None
    return dir(obj)
