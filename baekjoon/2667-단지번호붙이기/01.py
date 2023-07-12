from typing import List, Tuple
from collections import deque

def check_hjkl(map: List[List[int]], point: Tuple[int, int]) -> List[Tuple[int, int]]:
    hjkl = [
        (+1, 0),
        (-1, 0),
        (0, +1),
        (0, -1),
    ]
    result = []
    i, j = point
    height = len(map)
    width = len(map[0])
    for (di, dj) in hjkl:
        ni = i + di
        nj = j + dj
        if 0 <= ni and ni < width and 0 <= nj and nj < height and map[nj][ni] == 1:
            result.append((ni, nj))
    return result

def find_group(map: List[List[int]], point: Tuple[int, int]) -> int:
    queue = deque([point])
    size = 0
    while queue:
        i, j = queue.popleft()
        if map[j][i] == 1:
            map[j][i] = 2
            size += 1
            for new_points in check_hjkl(map, (i, j)):
                queue.append(new_points)
    return size

def solve(map: List[List[int]]) -> List[int]:
    groups = []
    for j, line in enumerate(map):
        for i, cell in enumerate(line):
            if cell == 1:
                groups.append(find_group(map, (i, j)))
    return groups
    
if __name__ == '__main__':
    import sys
    sys.stdin.readline()
    map = [[int(c) for c in line] for line in sys.stdin.read().strip().split('\n')]
    result = solve(map)
    print(len(result))
    for i in sorted(result):
        print(i)
    
