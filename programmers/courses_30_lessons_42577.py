"""
출처 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/42577
solution : http://kitle.xyz/post/106/

전화번호 목록
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
"""


def solution(phone_book):
    answer = True
    for item in phone_book:
        for temp in phone_book:
            if item != temp and str(temp).startswith(str(item)):
                return False
    return answer


phone_book = [12, 123, 1235, 567, 88]
print(solution(phone_book))
