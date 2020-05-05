#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = []
    for cnt in range(len(my_list)):
        div.append(my_list[cnt] % 2 == 0)
    return (div)
