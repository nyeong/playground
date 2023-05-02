# 문제 분석
#   많이 나온 패턴 찾기
#   최소 2가지는 들어가야됨.
#   최소 2명의 손님으로부터는 주문을 받아야함
# 쉬우면서도 어려울 것 같은데...
#   orders 분석해서 각 손님이 주문한 메뉴 별로 조합 뽑기 (크기는 course에 따라서)
#   뽑은 조합 세기

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    menus = {count: defaultdict(int) for count in course}
    total_menus = []
    for order in orders:
        for count in course:
            combos = combinations(order, r=count)
            for menu in [''.join(sorted(list(combo))) for combo in combos]:
                menus[count][menu] += 1
    for n, n_menus in menus.items():
        menus = [(k, v) for k, v in n_menus.items() if v >= 2]
        menus.sort(key=lambda x: x[1])
        if menus:
            max_value = menus[-1][1]
            total_menus += [k for (k, v) in menus if v == max_value]
    return sorted(total_menus)
