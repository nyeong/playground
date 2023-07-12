def solve(tables):
    tables.sort(key=lambda x: x[0])
    tables.sort(key=lambda x: x[1])
    before_end = tables[0][1]
    count = 1
    for (begin, end) in tables[1:]:
        if begin >= before_end:
            count += 1
            before_end = end
    return count


if __name__ == '__main__':
    from sys import stdin
    _ = int(stdin.readline())
    tables = [
        tuple(map(int, line.split())) \
        for line in stdin.read().rstrip().split('\n')
    ]
    print(solve(tables))
