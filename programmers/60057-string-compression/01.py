# 몇 개 씩 잘라야할까? 1..(len(s) // 2)
#   1개씩인 경우 aaaaaaaaaaa... => na
#   2개씩인 경우 abab..... => nab
#   ...
#   len(s) // 2인 경우 => 2abcd...
#   그 이상은 없을까? => 그 이상으로 자르면 애초에 축약이 안 되어서 원래 문자열과 결과가 같음.
# 직접 해보면 어떨까?
#   압축 매커니즘 O(n)
#     먼저 문자열을 n 사이즈로 자름
#     앞에서부터 읽으며 연속되는 것은 n + '연속된 문자열의 형태'로 바꿈
#     중간에 최선의 경우가 나오는 건 상관 없나?
#       xababcdcdababcdcd => x2ab2cd2ab2cd가 최선일텐데 결과가 17인 거 보니 그냥 앞에서부터 하는 듯.
#   이걸 1..(len(s)//2)만큼 해보기
#     대략 O(n^2)일 것 같음. max = 1000^2 = 1,000,000 할만한가?
# 런타임 에러...
#   len(s) == 1인 경우
def solution(s):
    if len(s) == 1: return 1
    def compress(s, n):
        """
        문자열 s를 n사이즈로 압축하여 반환
        """
        sliced = [s[r : r + n] for r in range(0, len(s), n)]
        compressed = ''
        before_pattern = ''
        pattern_count = 1
        for s in sliced + ['']:
            if s == before_pattern:
                pattern_count += 1
            else:
                if pattern_count == 1:
                    compressed += before_pattern
                else:
                    compressed +=  f'{pattern_count}{before_pattern}'
                pattern_count = 1
                before_pattern = s
        return compressed
    return min(len(compress(s, i)) for i in range(1, len(s)//2 + 1))