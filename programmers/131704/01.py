# 문제 참 길다
# 주어짐: 정수 배열 order (최대 1,000,000 / 1이상 order 이하의 길이)
# 구하기: 실을 수 있는 상자의 개수
# 1. 컨테이너 벨트에는 1, 2, 3, ...으로 정수 배열이 있음
# 2. 이걸 order처럼 만들어야함
# 3. 보조 컨테이너 쓸 수 있음. LIFO, 스택임.
# 하라는 대로 하면 되는 듯?
def solution(order):
    order_index = 0
    subcon = []
    truck = []
    
    for i in range(1, len(order) + 1):
        while subcon and subcon[-1] == order[order_index]:
            truck.append(subcon.pop())
            order_index += 1
        if i == order[order_index]:
            truck.append(i)
            order_index += 1
        else:
            subcon.append(i)

    # 남은 스택 비우기
    while subcon and subcon[-1] == order[order_index]:
        truck.append(subcon.pop())
        order_index += 1
            
    return len(truck)
