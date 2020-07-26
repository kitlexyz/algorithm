"""
source : https://programmers.co.kr/learn/courses/30/lessons/42888
explanation : http://kitle.xyz/post/110/
"""


def solution(record):
    answer = []
    dict = {}
    for item in record:
        now_record = item.split(" ")
        if now_record[0] == 'Enter' or now_record[0] == 'Change':
            dict[now_record[1]] = now_record[2]

    for now in record:
        new_record = now.split(" ")
        if new_record[0] == 'Enter':
            answer.append(str(dict[new_record[1]])+"님이 들어왔습니다.")
        if new_record[0] == 'Leave':
            answer.append(str(dict[new_record[1]])+"님이 나갔습니다.")
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)