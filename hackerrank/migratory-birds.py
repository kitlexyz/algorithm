"""
source: https://www.hackerrank.com/challenges/migratory-birds/problem
explanation : http://kitle.xyz/post/126/
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    set_arr = list(set(arr))
    set_arr.sort()
    return max(set_arr, key=arr.count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

