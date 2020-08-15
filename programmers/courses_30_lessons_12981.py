"""
source : https://programmers.co.kr/learn/courses/30/lessons/12981
explanation : http://kitle.xyz/post/124/
"""


def solution(n, words):
    spoken_words = []
    for item in range(len(words)):
        if not spoken_words:
            spoken_words.append(words[item])
        else:
            if words[item] in spoken_words:
                return [item % n + 1, item // n + 1]
            elif spoken_words[item-1][-1:] != words[item][:1]:
                return [item % n + 1, item // n + 1]
            else:
                spoken_words.append(words[item])
    return [0, 0]
