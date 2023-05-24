'''
최소공배수만큼 반복이 나온다. 가장 기본형은 w/gcd, h/gcd.
기본형에서 못 쓰는 사각형의 개수는 w + h - 1. 사각형 하나가 겹치기 때문에.
기본형을 모든 경우에 대해 확장하면 (w/gcd + h/gcd - 1) * gcd. gcd만큼 반복하니까
쓸 수 있는 영역 = 전체 - 못 쓰는 영역이므로 답은 아래와 같음
'''
from math import gcd
def solution(w,h):
    return w * h - w - h + gcd(w, h)
