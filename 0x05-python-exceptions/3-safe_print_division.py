#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        return div
    finally:
        print("Inside result: {:d}".format(div))
        return div
