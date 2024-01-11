#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return 0
    sum = 0
    tw = 0
    for item in my_list:
        n, w = item
        sum += n * w
        tw += w
    return sum / tw
