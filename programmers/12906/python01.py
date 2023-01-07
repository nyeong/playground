# 접근
# 그냥 순회하면서 전꺼랑 다르면 넣기
def solution(arr):
    new_arr = [arr[0]]
    prev_val = arr[0]
    for val in arr[1:]:
        if prev_val == val:
            continue
        new_arr.append(val)
        prev_val = val
    return new_arr
