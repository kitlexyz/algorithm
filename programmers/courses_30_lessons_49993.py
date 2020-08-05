'''
source: https://programmers.co.kr/learn/courses/30/lessons/49993
explanation: https://kitle.xyz/post/96
'''


def solution(skill, skill_trees):
    answer = 0
    seq = []
    for item in skill:
        seq.append(item)

    for skill_tree in skill_trees:
        checker = True
        temp_seq = seq.copy()
        for letter in skill_tree:
            if letter in temp_seq and temp_seq[0] == letter:
                temp_seq.remove(letter)
            elif letter in temp_seq and temp_seq[0] != letter:
                checker = False
                break
        if checker is True:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))
