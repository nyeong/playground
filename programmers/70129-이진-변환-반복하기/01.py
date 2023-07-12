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
    # 내장함수 bin 쓰면 쉽게 구할 수 있음
    return (to_bin(cnt1), len(str) - cnt1)

def to_bin(number):
    def bin_to_char(num):
        return '1' if num else '0'
    result = ''
    while number > 1:
        result += bin_to_char(number % 2)
        number //= 2
    result += bin_to_char(number)
    return result[::-1]
