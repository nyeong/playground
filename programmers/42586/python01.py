# 접근
# progresses와 speeds를 "개발 완료까지 필요한 날의 수"로 바꾼다
#   각 원소는 ceil((100 - p) / s)가 된다.
# 값을 하나 잡고 리스트를 순회한다.
#   지금 순회한 값이 잡고 있는 값보다 크다면 앞의 것은 개발 완료된 것으로 간주한다.
#   작다면 방금 순회한 개발 일정은 지금 잡고있는 값에 귀속된다.
from math import ceil

def solution(progresses, speeds):
    required_days = \
        [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    answer = [1]
    holding = required_days[0]
    for day in required_days[1:]:
        if holding >= day:
            answer[-1] += 1
        else:
            holding = day
            answer.append(1)
    return answer
