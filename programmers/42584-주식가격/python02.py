# 문제가 직관이랑 조금 안 맞음
#   i초 시점의 주식 가격이 몇 초동안 유지하였냐?를 묻는 문제
# 접근
# prices를 index와 함께 순회한다.
#   하락장이 왔다면 비하락장스택에서 하나씩 꺼내어서 확인한다.
#     하락장인 것은 얼마간 버텼는지 계산하고 버린다.
#     버릴거 다 버렸으면 스택에 남아있는 것은 지금 시점에서 아직 하락하지 않은 가격이다.
#   지금값은 다시 비하락장 스택에 넣어서 다음에 계산한다.
# 끝까지 계산해서 상승장 스택에 남아있는 것들은 끝까지 하락하지 않은 것들이다.

def solution(prices):
    '''
    prices: prices[i]는 (i+1)초일 때의 주식의 가격
    '''
    etcstream = [] # (idx, price)
    downstream = [] # (idx, how_long)
    
    for i, v in enumerate(prices):
        # 전값과 비교하여 하락세인지 확인
        while etcstream and etcstream[-1][1] > v:
            (ei, ev) = etcstream.pop()
            downstream.append((ei, i - ei))
        etcstream.append((i, v))
            
    # etcstream에 남아있는 값들은 끝까지 값이 하락하지 않았으므로
    # 배열의 길이를 기준으로 초를 카운트
    etcstream = [(i, len(prices) - 1 - i) for (i, v) in etcstream]
    
    # 정렬하여 반환
    return [v for (_, v) in sorted(etcstream + downstream, key=lambda x: x[0])]
