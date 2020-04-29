#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 and n < len(str):
        return(str)
    else:
        return(str[0:n] + str[n + 1:])
