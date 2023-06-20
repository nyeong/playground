from sys import stdin, stdout

h, w = map(int, stdin.readline().split())
before_photo = [line for line in stdin.read().split('\n')]

# get minimum distances
distance = h
for i in range(w):
    current_distance = h
    for j in range(h):
        if before_photo[j][i] == 'X':
            current_distance = 0
        elif before_photo[j][i] == '.':
            current_distance += 1
        elif before_photo[j][i] == '#':
            distance = min(distance, current_distance)
            break

line = ''
for j in range(h):
    for i in range(w):
        if 0 <= j - distance and before_photo[j - distance][i] == 'X':
            line += 'X'
        elif before_photo[j][i] == '#':
            line += '#'
        else:
            line += '.'
    line += '\n'
stdout.write(line)
