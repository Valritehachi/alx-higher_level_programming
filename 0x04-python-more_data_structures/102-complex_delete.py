#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return a_dictionary
    delete_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delete_keys.append(key)

    for key in delete_keys:
        del a_dictionary[key]

    return a_dictionary
