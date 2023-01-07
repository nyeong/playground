# 접근
# 순회하면서 상승장이면 스택에 넣는다
#   하락장이 왔다면 상승장 스택에서 하나씩 꺼내어서 확인한다
#     하락장인 것은 얼마간 버텼는지 계산하고 버린다
#     버릴거 다 버렸으면 스택에 남아있는 것은 아직도 상승장이다.
# 끝까지 계산해서 상승장 스택에 남아있는 것들은 끝까지 상승장이었던 것들이다.
# TODO: 속도 개선

def solution(prices):
    prices = list(enumerate(prices))
    upstream = [] # (idx, price)
    downstream = [] # (idx, how_long)
    for i, v in prices[:-1]:
        upstream.append((i, v))
        next_v = prices[i + 1][1]
        
        if v > next_v:
            while upstream:
                if upstream[-1][1] <= next_v:
                    break
                (ui, uv) = upstream.pop()
                downstream.append((ui, i - ui + 1))
                
    upstream = [(i, len(prices) - 1 - i) for (i, v) in upstream]
    return [v for (_, v) in sorted(upstream + downstream, key=lambda x: x[0])] + [0]
