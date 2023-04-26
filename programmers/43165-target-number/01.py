# 다 해보면 방법이 몇 개일까?
#   +이거나 -이거나가 n개 만큼 => 2^n
#   최악의 경우는 2^20 = 1,048,576
#   할만할지도?
# 계산을 더 줄이려면
#   앞선 계산을 활용해야함
#     (+1+1+1)-1
#     (+1+1+1)+1
#     DFS, DP
def solution(numbers, target):
    count = 0
    def iteration(numbers, num):
        """
        numbers는 아직 계산하지 않은 값. num은 앞에서 이미 계산한 값.
        """
        if len(numbers) < 1:
            raise TypeError
        elif len(numbers) == 1:
            if num - numbers[0] == target: return 1 
            elif num + numbers[0] == target: return 1
            else: return 0
        else:
            return iteration(numbers[1:], num - numbers[0]) + iteration(numbers[1:], num + numbers[0])
    return iteration(numbers, 0)