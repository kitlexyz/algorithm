"""
source: https://programmers.co.kr/learn/courses/30/lessons/12945?language=python3
explanation : http://kitle.xyz/post/123/
"""


def solution(n):
    fibo = []
    for num in range(0, n+1):
        if num == 0:
            fibo.append(0)
        elif num == 1:
            fibo.append(1)
        else:
            fibo.append(fibo[num - 2] + fibo[num - 1])

    return fibo[n] % 1234567
