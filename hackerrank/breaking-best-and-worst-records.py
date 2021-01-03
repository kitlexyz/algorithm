"""
source: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
explanation : https://kitle.xyz/post/145/
"""

# Complete the breakingRecords function below.
def breakingRecords(scores):
    h_score = None
    h_score_cnt = 0
    l_score = None
    l_score_cnt = 0
    for i in scores:
        if h_score is None:
            h_score = i
            l_score = i
        elif h_score < i:
            h_score = i
            h_score_cnt += 1
        elif l_score > i:
            l_score = i
            l_score_cnt += 1

    return str(h_score_cnt) + ' ' + str(l_score_cnt)

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
