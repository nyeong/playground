# 접근
# 두 가지 문제를 풀어야 한다:
#   1. 많이 재생된 순으로 장르 정렬하기
#   2. 각 장르 별로 재생수 순으로 정렬하기
# 주어진 genres와 plays를 순회하며 아래처럼 songs를 정리한다.
#   songs = {genres: [(id, plays)]}
# songs의 각 k, v를 순회하며 아래처럼 rank를 구하고 total_plays에 따라 정렬한다.
#   ranks = [("genre", total_plays)]
# ranks 순서대로 songs에서 genre를 키로 최상위 곡 두 개를 뽑아서 반환한다.
def solution(genres, plays):
    songs = get_songs(genres, plays)
    ranks = get_ranks(songs)
    result = []
    for (genre, _) in ranks:
        s = [i for (i, p) in songs[genre]][:2]
        result += s
    return result
    
    
def get_songs(genres, plays):
    songs = {}
    for i, _ in enumerate(genres):
        g = genres[i]
        p = plays[i]
        if g not in songs:
            songs[g] = []
        songs[g].append((i, p))
    s = {k: sorted(v, key= lambda x: x[1], reverse=True) for k, v in songs.items()}
    return s

def get_ranks(songs):
    ranks = []
    for k, v in songs.items():
        plays = sum([p for (i, p) in v])
        ranks.append((k, plays))
    return sorted(ranks, key= lambda x: x[1], reverse=True)
