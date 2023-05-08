# 구현 문제일 것 같다. 그대로 구현하면 될 듯.
# w를 u와 v로 분리해야함.
# 구현
#   p의 여는 괄호`(`와 닫는 괄호`)`의 개수를 샌다
#   p의 앞에서부터 균형잡힌 괄호 문자열이 될 때까지 슬라이싱한다. 이를 u라 하자:
#     u가 올바른 괄호 문자열이면 다음 문자열을 찾는다.
#     u가 올바르지 않으면 하라는 대로 문자열을 처리한다.
# 하라면 대로 하면 된다
def solution(p):
    if not p: return ''
    u, v = divide_uv(p)
    if is_correct_bracket_string(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + invert(u[1:-1])

def invert(s):
    answer = ''
    for c in s:
        if c == '(': answer += ')'
        elif c == ')': answer += '('
    return answer

def is_correct_bracket_string(p):
    bracket_count = 0
    for c in p:
        if c == '(':
            bracket_count += 1
        elif c == ')':
            bracket_count -= 1
        if bracket_count < 0:
            return False
    if bracket_count == 0:
        return True
    
def divide_uv(p):
    # (의개수, )의개수
    bracket_count = [0, 0]
    idx = 1
    for c in p:
        if c == '(':
            bracket_count[0] += 1
        elif c == ')':
            bracket_count[1] += 1
        if bracket_count[0] == bracket_count[1]:
            break
        idx += 1
    return (p[:idx], p[idx:])
