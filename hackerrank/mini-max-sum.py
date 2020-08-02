"""
source: https://www.hackerrank.com/challenges/mini-max-sum/problem
explanation : http://kitle.xyz/post/115/
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def minimaxsum(arr):
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    minimaxsum(arr)