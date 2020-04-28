#!/usr/bin/python3
def uppercase(str):
    for count in str:
        letter = ord(count)
        if letter >= 97 and letter <= 122:
            letter = letter - 32
        print("{:c}".format(letter), end='')
    print(end='\n')
