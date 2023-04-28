# enqueue와 dequeue만 써서 각 큐의 원소의 합이 같도록 만들기.
# enqueue-dequeue가 1회임
# 될 때까지 해봐도 되나?
#   매 순간 할 수 있는 행동은 두 개. 1을 dequeue 할 것인가, 2를 dequeue할 것인가.
#     경우의 수가 매 분기마다 2배가 된다. 근데 중복도 숨어있음.
#   자칫하면 무한히 할 수도 있음
#   불가능하면 -1을 반환해야해
# 이론상 원하는 대로 수를 배치할 수는 있지 않나?
#   이동 횟수가 많더라도 하려고 하면 내가 원하는 대로 수를 배치할 수 있을 듯
#   따라서 불가능하다는 뜻은 enqueue-dequeue 연산으로 불가능하다는 게 아니라
#   수 자체가 [1], [2] 이런 식이라서 불가능하다
# 아니 이게 되네
#   sum을 iteration 구하면 n^2이라 시간초과 나니까 직접 구해주고...
#   그냥 크기비교해서 해보는 게 최적해인 이유??가 뭘까??
#   MAX_TRY는 몇이 제일 적절할까?
#     아무 생각 없이 제한사항의 최대 길이로 풀려서 당황스러움 

from collections import deque

def solution(queue1, queue2):
    MAX_TRY = 300_000 * 4
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    count = 0
    while sum1 != sum2 and count < MAX_TRY:
        count += 1
        if sum1 > sum2:
            pop = q1.popleft()
            q2.append(pop)
            sum1 -= pop
            sum2 += pop
        else:
            pop = q2.popleft()
            q1.append(pop)
            sum2 -= pop
            sum1 += pop

    return count if count < MAX_TRY else -1
