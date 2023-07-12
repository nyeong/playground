from sys import stdin

def bfs(graph, start):
    from collections import deque
    log = []
    q = deque([start])
    while q:
        p = q.popleft()
        log.append(p)

    return log

def dfs(graph, start):
    log = []
    visited = {i: False for i in graph.keys()}
    def search(curr):
        visited[curr] = True
        log.append(curr)
        for node in graph[curr]:
            if not visited[node]:
                search(node)
    search(start)

        
    return log

if __name__ == '__main__':
    n, m, v = map(int, stdin.readline().split())
    graph = [[] for _ in ' ' * (n + 1)]
    for
    print(n, m, v)
    print(graph)
