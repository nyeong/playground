# 우리가 아는 귤은 감귤나무 열매로 영어로 tangerine이고,
# 흔히 얘기하는 orange는 당귤나무 열매로 말 그대로 오렌지라네요~
# 한라봉은 이 둘을 교배해 만든 것으로 품종으로는 만감류, 영어로는 tangor라고 부른다고 하네요~
from collections import Counter

def solution(k, tangerines):
    tangerines = sorted(Counter(tangerines).items(), key=lambda x: x[1], reverse=True)
    kind = 0
    for t, c in tangerines:
        if k <= 0:
            return kind
        else:
            kind += 1
            k -= c
    return kind
