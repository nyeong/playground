# clothes는 아래와 같이 생겼다:
#   [[value, key], ...]
# 이를 아래와 같은 dict에 넣는다:
#   {key: [value1, value2, ...], ...}
# 이 dict의 value인 list의 len을 len + 1해서 서로 곱한다
# 아예 안 입는 경우는 없으므로 1을 뺀다
from math import factorial

def solution(clothes):
    c = {}
    for [value, key] in clothes:
        if key in c:
            c[key].append(value)
        else:
            c[key] = [value]
    result = 1
    for key, value in c.items():
        print(f"key {key} has {value} items")
        result *= len(value) + 1
    return result - 1
    
