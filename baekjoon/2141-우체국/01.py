if __name__ == '__main"__':
    from sys import stdin
    _ = stdin.readline()
    postoffices = [
        tuple(map(int, line.split())) for line in stdin.read().rstrip().split('\n')
    ]
    print(postoffices)
