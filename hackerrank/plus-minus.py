"""
source: https://www.hackerrank.com/challenges/plus-minus/problem
explanation: http://kitle.xyz/post/112/
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    result = [0, 0, 0]
    for item in arr:
        if item > 0:
            result[0] += 1
        elif item < 0:
            result[1] += 1
        elif item == 0:
            result[2] += 1

    for item in result:
        print(format(item / len(arr), '.5f'))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
