# 접근
# 리스트의 앞부터 순회하며 스택에 넣고 꺼내고 하면 검증할 수 있다.
#   여는 괄호 `(`면 스택에 넣는다
#   닫는 괄호 `)`면 스택에서 뺀다
#   빈 스택에서 빼려고 하면 맞는 괄호쌍이 아니다
#   다 돌았는데 스택이 비지 않았으면 맞는 괄호쌍이 아니다
# 정말로 스택으로 할 필요는 없고 +1, -1로 쌓인 것만 표현해도 된다.
def solution(s):
    acc = 0
    for parenthesis in s:
        if parenthesis == "(":
            acc += 1
        if parenthesis == ")":
            acc -= 1
        if acc < 0:
            return False
    if acc == 0:
        return True
    return False
    
