"""
source: https://www.hackerrank.com/challenges/time-conversion/problem
explanation: http://kitle.xyz/post/119/
"""

#!/bin/python3

import os
import sys


def timeConversion(s):
    twelve_hour = s[:2]
    if twelve_hour == '12' and s[-2:] == 'AM':
        return str('00')+s[2:-2]
    elif twelve_hour == '12' and s[-2:] == 'PM':
        return s[:-2]
    else:
        if s[-2:] == 'AM':
            return s[:-2]
        else:
            twelve_hour = s[:2]
            twenty_four_hour = int(twelve_hour) + 12
            return str(twenty_four_hour)+s[2:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
