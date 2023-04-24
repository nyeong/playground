# O(n)
def solution(participant, completion):
    ps = {}
    for p in participant:
        ps[p] = ps.get(p, 0) + 1
    for p in completion:
        ps[p] -= 1
    for k, v in ps.items():
        if v > 0:
            return k
