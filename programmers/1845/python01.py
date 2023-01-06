# 접근
# nums를 dict으로 변환 -> {num: count}
# 키, 쌍의 개수가 겹치지 않는 최대의 수 == 가장 많은 종류의 포켓몬 -> len(nums)
# 답은 len(Counter(nums))거나 len(nums)/2거나?
from collections import Counter

def solution(nums):
    max_races = len(Counter(nums))
    n = len(nums) / 2
    return n if max_races > n else max_races
