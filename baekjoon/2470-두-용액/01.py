from sys import stdin

n = int(stdin.readline())
nums = sorted(map(int, stdin.readline().split()))

bound = [0, len(nums) - 1]

last_close = None

while bound[0] <= bound[1]:
    sum = nums[bound[0]] = nums[bound[1]]

    if sum == 0:
        last_close = sum
        break
    elif abs(last_close) < abs(sum):
        pass
    elif abs(last_close) > abs(sum):
        pass
