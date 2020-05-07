#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    val = list(map((lambda x: x * number), my_list))
    return val
