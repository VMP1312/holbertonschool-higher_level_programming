#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for num in dic:
        dic[num] *= 2
    return dic
