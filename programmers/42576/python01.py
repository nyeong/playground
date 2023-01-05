# 접근
# 완주자를 hash로 만든다.
#   동명이인이 있으니 {이름: 명수}
# 참가자 리스트를 순회하며 완주자에 질의한다.
#   완주자 hash에 키가 없는 놈이 범인이다
#     동명이인 중 완주 못한 놈을 찾아야한다.
#       조회에 성공하면 명수 - 1 한다.
#       명수가 0이 아닌 놈이 범인이다.
from collections import Counter

def solution(participant, completion):
    c = Counter(completion)
    for p in participant:
        if p not in c:
            return p
        c[p] -= 1
        
    for name, value in c.items():
        if value != 0:
            return name
        