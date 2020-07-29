"""
source: https://www.hackerrank.com/challenges/compare-the-triplets/problem
explanation : http://kitle.xyz/post/111/
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


def compareTriplets(a, b):
    result_a = 0
    result_b = 0
    for pos in range(len(a)):
        if a[pos] > b[pos]:
            result_a += 1
        elif a[pos] < b[pos]:
            result_b += 1
    return [result_a, result_b]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
