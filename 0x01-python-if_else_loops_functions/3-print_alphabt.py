#!/usr/bin/python3
for alphabet in range(97, 123):
    if (alphabet is not 101 and alphabet is not 113):
        print("{:c}".format(alphabet), end='')
