#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    sum = 0
    dups = set()
    for item in my_list:
        if item not in dups:
            sum = sum + item
            dups.add(item)
    return sum
