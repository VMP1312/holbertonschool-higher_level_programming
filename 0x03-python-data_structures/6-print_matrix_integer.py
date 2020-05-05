#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        y = 1
        for cnt in x:
            print("{:d}".format(cnt), end="")
            if len(x) > y:
                print(end=" ")
            y += 1
        print(end="\n")
