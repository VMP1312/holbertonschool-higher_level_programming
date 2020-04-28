#!/usr/bin/python3
for f in range(10):
    for s in range((f + 1), 10):
        if f != 8 and s > f:
            print("{:d}{:d}, ".format(f, s), end="")
        elif f == 8 and s == 9:
            print("{1:d}{0:d}".format(s, f))
