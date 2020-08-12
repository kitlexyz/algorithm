"""
source: https://www.hackerrank.com/challenges/the-time-in-words/problem
explanation: http://kitle.xyz/post/121/
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.



def timeInWords(h, m):
    dict = {
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'quarter',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        30:'half',
    }

    if m == 00:
        return dict[h]+" o' clock"
    elif int(m) == 1:
        return dict[int(m)]+' minute past '+dict[h]
    elif int(m) in (15, 30):
        return dict[int(m)]+' past '+dict[h]
    elif int(m) <= 20:
        return dict[int(m)]+' minutes past '+dict[h]
    elif 20 < int(m) < 30:
        return dict[20]+' '+dict[int(m)-20]+' minutes past '+dict[h]
    elif int(m) == 45:
        return dict[15] + ' to ' + dict[h+1]
    elif int(m) < 60:
        conv_m = 60 - int(m)
        if 20 < conv_m < 30:
            return dict[20] + ' ' + dict[conv_m-20] + ' minutes to ' + dict[h+1]
        else:
            return dict[conv_m] + ' minutes to ' + dict[h+1]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
