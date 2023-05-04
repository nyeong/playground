# 문제 요건
#   중복된 원소가 있을 수 있음
#   순서가 중요함
# 튜플의 배열을 표현한 문자열이 주어지는데 그 튜플들이 어떤 튜플을 표현하는지 맞추기
#   [2, 1, 3, 4] => {2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}가 될 수 있는데
#   이를 역으로 오른쪽을 보고 왼쪽을 맞추기
#   뭔소리여?
#     {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}} => 2 1 3 4 OK
#     {{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}} => 2 1 3 4 OK
#     {{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}} => 2 1 3 4 왜???
#       1 2 4 3 튜플로 어떻게 2 1 3 4를 유추해내?
#       집합은 원소의 순서가 바뀌어도 상관 없으나, 튜플은 바뀌면 안된다고 해놓고
#       왜 튜플 속의 원소 순서가 바뀌어??
#       {} => 이게 set이라 괜찮다?
#       순서가 다른데 어떻게 원래 튜플의 순서를 유추하지
#       어쨌든 앞에서부터 끊을 수 밖에 없다는 사실을 이용해야함
#       {{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}} => {2}가 있으니 무조건 첫번째는 2
# s를 일단 파싱함
#   [각 집합] => 요걸 크기 순서대로 오름차순으로 정렬시켜놓기
# 위의 리스트를 앞에서부터 보자
#   크기가 1인 집합은 튜플의 0번째 값만 들어있음
#   크기가 2인 집합은 튜플의 0, 1번째 값이 들어있으므로 크기가 1인 집합을 빼면 됨
#   등등
def solution(s):
    def parse(string):
        '''
        return: [{int}] 
        '''
        sets = []
        for c in string[1:-1]:
            if c == '{':
                sets.append(set())
                sets.append('')
            elif c in c.isdigit():
                sets[-1] += c
            elif c == ',' and type(sets[-1]) is str:
                num = sets.pop()
                sets[-1].add(int(num))
                sets.append('')
            elif c == '}':
                num = sets.pop()
                sets[-1].add(int(num))
        return sets
        
    sets = sorted(parse(s), key=len)
    nums = [list(sets[0])[0]]
    if len(sets) > 1:
        for i in range(1, len(sets)):
            nums.append((sets[i] - sets[i - 1]).pop())
    return nums