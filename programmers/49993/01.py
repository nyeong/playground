# 문제 조건 상 효율이 필요 없기 때문에 그냥 해봐도 된다.
def solution(skill, skill_trees):
    count = 0
    for st in skill_trees:
        skill_stack = list(skill)
        for char in st:
            if char in skill and char != skill_stack.pop(0):
                break
        else:
            count += 1
    return count
