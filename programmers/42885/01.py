# 정렬해서 순서대로 태우면 되나?
#   [40 50 50 60], 100인 경우
#   50 50 / 40 60이면 두 번이면 되는데 순서대로 태우면 40 50 / 50 / 60으로 세 번이므로 반례임
# 최대 두 명 태울 수 있으므로, n명이 나올 수 있는 경우의 수는 nC2 = n * (n-1) / 2
#   n<=50_000이므로 최악의 경우의 수는 적어도 1,249,975,000... 너무 많은데
# 정렬하고 무거운 사람 먼저 태우고 가벼운 사람 태워보기
#   [40 50 50 60], 100인 경우
#   60 40 / 50 50 바로 나옴
#   반례가 있을까?
#   고민 안 하고 해봤는데 통과됨
def solution(people, limit):
    people = sorted(people)
    most_light_index = 0
    boat_count = 0
    while people and most_light_index < len(people):
        heavy = people[-1]
        light = people[most_light_index]
        if heavy + light <= limit:
            most_light_index += 1
        people.pop()
        boat_count += 1
    return boat_count
