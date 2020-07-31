"""
source: https://www.hackerrank.com/challenges/staircase/problem
explanation: http://kitle.xyz/post/113/
"""
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(num):
    for i in range(num):
        print(' '*(num-i-1) + '#'*(i+1))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
