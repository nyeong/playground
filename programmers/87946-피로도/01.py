# 구하는 거 : 탐험할 수 있는 최대 던전 수
# 다 돌아봐야 하지 않을까?
#   던전은 최대 8개. 8개를 늘여놓는 방법의 수 = 8! = 40,320 = 순열
#   충분히 작은 수
# 무식하게 다 해봐도 풀리겠다. 중복도 고려할 필요 없을 듯
#   그래프로 따지자면 모두가 서로 연결된 그래프 = 완전 그래프
#   중요한 거 = 어디서 시작하냐
#   피로도 바닥날 때까지 돌아보자
#     방문 해야 할 던전을 앞에서부터 보면서 들어갈 수 있으면 들어가기
#     방문할 수 없는 던전은 따로 뺀다. 어차피 나중에도 방문할 수 없다.
#     방문한 던전은 따로 모아서 센다.
# 순열이니까 그냥 순열로 경우의 수를 담은 index 만들어서 다 해보면 되지 않을까?
#   길이가 2인 경우의 수 = [[0, 1], [1, 0]] -> 이 순서대로 방문시키기
#   itertools에 permutations이 있네?
#   그냥 이거 쓰면 경우의 수를 나열해주네??
from itertools import permutations

def solution(k, dungeons):
    '''
    k=피로도
    dungeons=[[최소 필요 피로도, 소모 피로도]]
    '''
    def visit(k, dungeons):
        count = 0

        for 최소피로도, 소모피로도 in list(dungeons):
            if k < 최소피로도:
                return count
            else:
                k -= 소모피로도
                count += 1
        return count

    return max([visit(k, case) for case in permutations(dungeons)])
