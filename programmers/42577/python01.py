# 먼저 정렬한다
#   정렬하면 아래처럼 되므로 접두사 판별이 쉬워진다
#   119
#   1195524421
# i번째 내용이 i + 1번째 내용의 일부면 접두사다
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i, number in enumerate(phone_book[:-1]):
        if phone_book[i + 1].startswith(number):
            return False
    return True
