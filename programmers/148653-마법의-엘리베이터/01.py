# 문제
#   +- 10^n을 최소로 조합하여 수 만들기
#   1 이상의 수만 주어짐
#   * 주의: 0층보다 밑으로 내려갈 순 없음
#   * 수를 만드는 건 맞는데... 문제 요건상 **내려가야함**
# 접근
#   그래프로 풀 수 있을듯? BFS?
#     -1, +1, -10, +10, ... 등의 노드가 있는 완전그래프라고 생각하기
#   1의 자리가 5보다 같거나 작으면 -1을 n번 누르는 게 빠름
#   1의 자리가 5보다 크면 +1을 (10-n)번 누르고 -10을 1번 누르는 게 빠름
#   층   1  2  3  4  5  6  7  8  9  10
#   최소  1  2  3  4  5  5  4  3  2  1
#   최소해가 딱 떨어지는 문제인듯??
#     최대 주어지는 수가 100,000,000로 좀 큰데 최소해가 정해져있는 문제 맞을듯?
#     반례가 있을까?
#       1의자리의 수를 맞추려면 1의 자리의 수를 더하거나 뺄 수 밖에 없음.
#       더 높은 자리의 수가 더 낮은 자리의 수에 이 이상 영향을 미칠 수가 없다.
#       따라서 가장 자리수가 낮은 수부터 차례로 최소해로 푸는 게 정석일듯
#       999의 경우는?
#         +1, -1000
#       92의 경우는?
#         -1 * 2 + +10 * 1 + -100 * 1 = 4
#       95의 경우는? <- 반례다 반례
#         -1 * 5 + +10 * 2 + -100 * 1 = 8
#         +1 * 5 + -100 * 1 = 6
#         5인 경우는 올라가나 내려가나 똑같으므로 올라가서 이득인 경우도 생각해야
#         어떤 때에 이득인가? 올라가서 더 높은 자리의 자릿수가 5 이상이면? => 6 이상이면
#       55의 경우는?
#         -1 * 5 + -10 * 5 => 10
#         +1 * 5 + +10 * 4 + 100 * 1 => 10 똑같음
#       45의 경우는?
#         -1 * 5 + -10 * 4 => 9 손해임
#       556? 455
# 
# 구현
#   주어진 정수를 자리수로 분할하기
#     storey.to_str.split('').map(&:to_i)
#     파이썬은 왤케 괄호를 앞뒤로 왔다갔다 해야하나요
#   올림=0
#   낮은 자리수부터 무식하게 계산하기
#     이번 자리수 + 올림이 0이면 누를 필요가 없음
#       올림 초기화
#     이번 자리수 + 올림이 5보다 같거나 작으면
#       count += n, 올림 초기화
#     이번 자리수 + 올림이 5보다 크면
#       count += (10 - n), 올림 = 1
def solution(storey):
    count = 0
    def to_list(nums):
        return [int(digit) for digit in str(nums)[::]]
    i = 0
    while storey > 0:
        back_index = len(str(storey)) - 1 - i
        digits = to_list(storey)
        if digits[back_index] == 0:
            pass
        elif digits[back_index] == 5:
            if digits[back_index - 1] + 1 > 5: # <- 6이 아니라 5였음
                storey += 5 * 10 ** i
            else:
                storey -= 5 * 10 ** i
            count += digits[back_index]
        elif digits[back_index] < 5:
            storey -= digits[back_index] * 10 ** i
            count += digits[back_index]
        else:
            storey += (10 - digits[back_index]) * 10 ** i
            count += (10 - digits[back_index])
        i += 1

    return count