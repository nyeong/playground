def solution(tickets):
    ts = {a: [] for a, _ in tickets}
    for a, b in tickets:
        ts[a].append(b)
    ts = {k: sorted(v, reverse=True) for k, v in ts.items()}
    
    visited = ["ICN"]
    path = []

    while visited:
        current = visited[-1]
        if current not in ts or not ts[current]:
            path.append(visited.pop())
        else:
            visited.append(ts[current].pop())
    return path[::-1]
