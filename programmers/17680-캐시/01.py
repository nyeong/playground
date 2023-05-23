'''
너무 느려서 캐시를 적용할 건데 얼마가 적정 사이즈인지 모르는 상황
목표: 캐시 크기에 따른 실행시간 측정하기
문제: LRU, 가장 최근에 쓴 걸 캐시에 저장하는데, cacheSize만큼 저장하기
     읽으면서 hit하면 1, miss하면 5만큼 시간 더하기
예제 분석:
  1. hit한 적이 없으니 10 * 5
  2. 처음 세 번은 miss, 나머지 6번은 hit = 5 * 3 + 6
무식하게 해도 되나요?
  cache에서 선형으로 찾기? 100000 * 30이어도 충분히 작겠는데
어려운 지점
  LRU, 최근에 안 쓴 놈을 대체함. 가장 최근에 본 놈들이 캐시에 남아야 함
  본지 오래된 걸 어떻게 알지??? LIFO => queue?
  queue 사이즈 30이면 괜춘하죠잉
테스트 케이스
  2 [jeju jeju jeju seoul seoul] => 13
'''
from collections import deque

def solution(cache_size, cities):
    repo = Repo(cache_size=cache_size)
    for city in cities:
        repo.get(city)

    return repo.elpased_time

class Repo():
    def __init__(self, **args):
        self.max_cache_size = args['cache_size']
        self.elpased_time = 0
        self.cache = set()
        self.cache_order = deque()
    
    def get(self, city):
        city = city.lower()
        if city in self.cache:
            self.elpased_time += 1
        else:
            self.elpased_time += 5
        self.cache_it(city)
    
    def cache_it(self, city):
        # 캐시를 쓰지 않는 경우
        if not self.max_cache_size:
            return
        # 이미 가장 최근에 캐시한 경우
        elif self.cache_order and self.cache_order[-1] == city:
            return
        # 이미 캐시되었으나 최근에 캐시한 것이 아닐 경우
        elif city in self.cache:
            self.cache.remove(city)
            self.cache_order.remove(city)
        # 캐시 된 적 없고 캐시가 가득 찬 경우
        elif len(self.cache) >= self.max_cache_size:
            lru = self.cache_order.popleft()
            self.cache.remove(lru)
        self.cache_order.append(city)
        self.cache.add(city)
