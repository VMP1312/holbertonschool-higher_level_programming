#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) - 1 > 0:
        sum = 0
        for count in range(1, len(argv)):
            num = int(argv[count])
            sum += num
        print("{:d}".format(sum))
    else:
        print("0")
