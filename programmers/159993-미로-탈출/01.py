'''
출발 -> 레버 -> 문
길 찾기 알고리즘 -> DFS, BFS
아직 레버를 당기지 않았더라도 출구가 있는 칸을 지날 수 있다 -> 지나가기만 할 수 있다는 건가?
1. S, L, E 위치 구하기
2. S -> L까지 경로 찾기
3. L -> E까지 경로 찾기
4. 시간 합산하여 반환
'''
from collections import deque

def solution(maps):
    s, l, e = get_sle(maps)
    s_to_l = calculate_minpath_time(maps, s, l)
    l_to_e = calculate_minpath_time(maps, l, e)
    
    if s_to_l and l_to_e:
        return s_to_l + l_to_e
    else:
        return -1

def calculate_minpath_time(m, f, t):
    q = deque([f])
    #time = [[None for _ in range(len(m[0]))] for _ in range(len(m))]
    time = [[None for _ in range(len(m[0]))] for _ in range(len(m))]
    time[f[1]][f[0]] = 0
    while q:
        x, y = q.popleft()
        elpased = time[y][x]
        if (x, y) == t:
            return elpased
        else:
            for (dx, dy) in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
                if 0 <= x + dx < len(m[0]) and \
                   0 <= y + dy < len(m) and \
                   m[y + dy][x + dx] != 'X' and \
                   time[y + dy][x + dx] == None:
                    time[y + dy][x + dx] = elpased + 1
                    q.append((x + dx, y + dy))
    else:
        return None

def get_sle(maps):
    s, l, e = None, None, None
    for yi, y in enumerate(maps):
        for xi, cell in enumerate(y):
            if cell == 'S':
                s = (xi, yi)
            elif cell == 'L':
                l = (xi, yi)
            elif cell == 'E':
                e = (xi, yi)
    return s, l, e
