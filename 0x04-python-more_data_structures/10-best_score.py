#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = next(iter(a_dictionary))
    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[max_key]:
            max_key = key
    return max_key
