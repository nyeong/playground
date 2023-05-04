# 미리 빼고 매핑해봤는데 그러면 안 됨 ㅠ..
#   문제대로 하면 역함수가 안 나오기 때문에...
# 하나하나 계산했는데 더 나은 방법이 있을까?
def solution(s, skip, index):
    def create_encode_map(skip, index):
        skip = set(skip)
        chars = 'abcdefghijklmnopqrstuvwxyz'[:]
        encode_map = {}
        def skip_char(idx):
            count = 0
            while count < index:
                idx += 1
                if not chars[idx % len(chars)] in skip:
                    count += 1
            return chars[idx % len(chars)]
        return {c: skip_char(idx) for idx, c in enumerate(chars)}
    
    encode_map = create_encode_map(skip, index)
    print(encode_map)
    return ''.join(map(lambda x: encode_map[x], s))
