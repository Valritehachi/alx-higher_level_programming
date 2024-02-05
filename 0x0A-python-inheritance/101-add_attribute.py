#!/usr/bin/python3

def add_attribute(mc, name, value):
    if not '__dict__' in dir(mc):
        raise TypeError("can't add new attribute")
    setattr(mc, name, value)
    
