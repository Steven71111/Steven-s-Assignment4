#!/usr/bin/env python

import sys

for num in sys.stdin:
    num = int(num.strip())
    if (num % 2) == 0:
        # num is even
        print("%s\t%s") % ("even", 1)
    else:
        # num is odd
        print("%s\t%s") % ("odd", 1)
