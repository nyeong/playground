# Counter는 산술 연산이 가능하다.
# 문제 정의에 따라 completion은 participant의 부분집합이므로
# Counter(participant) - Counter(completion) 하면 한 놈 남는데 그게 범인이다.
from collections import Counter

def solution(participant, completion):
    c = Counter(completion)
    p = Counter(participant)
    return list((p - c).keys())[0]