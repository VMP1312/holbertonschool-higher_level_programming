#!/usr/bin/python3
def no_c(my_string):
    translation = {ord('C'): None, ord('c'): None}
    return (my_string.translate(translation))
