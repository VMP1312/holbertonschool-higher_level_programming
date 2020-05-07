#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = dict.fromkeys(my_list)
    add = sum(num)
    return add
