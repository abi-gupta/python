#!/usr/bin/env python3

import sys

"""A module for demonstrating exceptions
"""

def converts(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}.".format(str(e)), file=sys.stderr)
        return -1


