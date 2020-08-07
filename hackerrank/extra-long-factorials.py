"""
source: https://www.hackerrank.com/challenges/extra-long-factorials/problem
explanation: http://kitle.xyz/post/120
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n > 1:
        return n * extraLongFactorials(n-1)
    else:
        return 1

    # or
    # return n * extraLongFactorials(n-1) if n > 1 else 1


if __name__ == '__main__':
    n = int(input())
    print(extraLongFactorials(n))
