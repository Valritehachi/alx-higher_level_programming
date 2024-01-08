#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    my_max = None
    for n in my_list:
        if my_max is None or n > my_max:
            my_max = n
    return my_max
