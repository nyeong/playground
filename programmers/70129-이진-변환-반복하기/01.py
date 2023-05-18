def solution(s):
    removed_zero = 0
    count = 0
    while s != '1':
        (s, removed) = binary_transition(s)
        count += 1
        removed_zero += removed
    return [count, removed_zero]

def binary_transition(str):
    # count the number of 1
    cnt1 = 0
    for c in str:
        if c == '1':
            cnt1 += 1
    return (bin(cnt1)[2:], len(str) - cnt1)
