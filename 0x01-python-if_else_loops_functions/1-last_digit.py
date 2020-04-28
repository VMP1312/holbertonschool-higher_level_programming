#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = number
if lastnum < 0:
    lastnum = number % -10
else:
    lastnum = number % 10

if lastnum > 5:
    print("Last digit of {:d} is {:d}".format(number, lastnum) +
          " and is greater than 5")
elif lastnum == 0:
    print("Last digit of {:d} is {:d}".format(number, lastnum) +
          " and is 0")
elif lastnum < 6 and lastnum is not 0:
    print("Last digit of {:d} is {:d}".format(number, lastnum) +
          " and is less than 6 and not 0")
