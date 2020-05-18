#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        div = fct(*args)
    except BaseException as error:
        print("Exception: {:}".format(error), file=sys.stderr)
        div = None
    finally:
        return div
