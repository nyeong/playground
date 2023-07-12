from sys import stdin

def 예산예상(예산요청, 예산상한):
    sum = 0
    for 예산 in 예산요청:
        sum += min(예산, 예산상한)
    return sum

n = int(stdin.readline())
예산요청 = sorted(map(int, stdin.readline().split()))
총예산 = int(stdin.readline())

if sum(예산요청) <= 총예산:
    print(예산요청[-1])
else:
    예산상한경계 = [총예산 // len(예산요청), 예산요청[-1]]
    예상 = None
    예산상한 = None
    while 예산상한경계[0] <= 예산상한경계[1]:
        예산상한 = sum(예산상한경계) // 2
        예상예산 = 예산예상(예산요청, 예산상한)
        print(f'예산상한 = {예산상한} in {예산상한경계}')
        print(f'예상예산 = {예상예산}')
        if 예상예산 <= 총예산:
            예상 = 예산상한
            예산상한경계[0] = 예산상한 + 1
        else:
            예산상한경계[1] = 예산상한 - 1
    print(예상)
