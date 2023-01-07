# 접근
# 하라는 대로 하면 된다.
def solution(priorities, location):
    count = 0
    while priorities:
        j = priorities[0]
        priorities = priorities[1:]
        if has_higher(j, priorities):
            priorities.append(j)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            count += 1
            if location == 0:
                return count
            
            location -= 1
            
def has_higher(j, last):
    for l in last:
        if l > j:
            return True
    return False
