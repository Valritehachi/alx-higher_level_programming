#!/usr/bin/python3

def inherits_from(obj, a_class):
    classes = [a_class] + a_class.__subclasses__()
    return any(issubclass(type(obj), cls) for cls in classes)
