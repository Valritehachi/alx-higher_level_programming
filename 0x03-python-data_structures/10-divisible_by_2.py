#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None:
        return None

    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i] % 2 == 0)

    return new_list
