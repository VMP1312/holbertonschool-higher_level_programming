#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for idx in range(len(my_list)):
        if new[idx] == search:
            new[idx] = replace
    return new
