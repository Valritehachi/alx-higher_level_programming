#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    if search is None or replace is None:
        return my_list
    new_list = []
    for item in my_list:
        if item == search:
           new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
