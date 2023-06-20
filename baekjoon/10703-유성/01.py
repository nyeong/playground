"""
문제:
    - 유성이 떨어지기 전 사진이 주어졌을 때, 유성이 떨어지고 난 후의 상황을 출력하라.
조건:
    - 사진은 유성, 땅, 공기로만 이루어져 있음.
    - 유성, 땅은 각각 하나의 덩어리임.
    - 떨어지고 난 후의 첫줄은 공기, 마지막줄은 땅으로 이루어져있음.
    - 모든 유성 조각들은 연결되어 있다. 즉, 두 부분 유성이 존재한다면, 한 쪽에서 유성
      조각을 통해 상하좌우로 이동해서 다른 부분 유성에 도달할 수 있다. 땅 또한 같은
      방식으로 연결되어 있다. -> 이거 뭔소린지 모르겠음
    - 유성은 수직으로 낙하한다. 유성이 땅에 떨어졌을 때, 유성과 땅은 원형을 유지한다
풀이:
    - 유성이 땅에 닿았느냐를 어떻게 판단할까?
        - 중간에 공기층이 없어야함
"""
from typing import List, Self
from sys import stdin, stdout
from enum import Enum

class PixelType(Enum):
    AIR = '.'
    SHOOTING_STAR = 'X'
    TERRAN = '#'

class Photo():
    terran_data: List[List[PixelType]]
    star_data: List[List[PixelType]]
    width: int
    height: int

    @classmethod
    def from_string(cls, data: str) -> Self:
        photo = Photo()
        data = [list(line) for line in data.split('\n')]
        width = len(data[0])
        height = len(data)
        terran_data = []
        star_data = []
        for i in range(height):
            terran_data.append([])
            star_data.append([])
            for j in range(width):
                if data[i][j] == PixelType.SHOOTING_STAR.value:
                    star_data[i].append(PixelType.SHOOTING_STAR)
                    terran_data[i].append(PixelType.AIR)
                elif data[i][j] == PixelType.TERRAN.value:
                    star_data[i].append(PixelType.AIR)
                    terran_data[i].append(PixelType.TERRAN)
                else:
                    star_data[i].append(PixelType.AIR)
                    terran_data[i].append(PixelType.AIR)
        cls.terran_data = terran_data
        cls.star_data = star_data
        cls.width = width
        cls.height = height
        return photo

    @classmethod
    def from_before(cls, before_photo: Self) -> Self:
        # find_minimum_distance
        distance = before_photo.get_star_distance()
        new_photo = cls()
        new_photo.terran_data = before_photo.terran_data
        new_photo.star_data = [
            [PixelType.AIR for _ in range(before_photo.width)] \
            for _ in range(before_photo.height)
        ]
        for i in range(new_photo.height):
            for j in range(new_photo.width):
                if before_photo.star_data[i][j] == PixelType.SHOOTING_STAR:
                    new_photo.star_data[i + distance][j] = PixelType.SHOOTING_STAR
        new_photo.width = before_photo.width
        new_photo.height = before_photo.height
        return new_photo

    def get_star_distance(self) -> int:
        distance = self.height
        for j in range(self.width):
            last_star_index = -1
            for i in range(self.height):
                if self.star_data[i][j] == PixelType.SHOOTING_STAR:
                    last_star_index = i
                elif self.terran_data[i][j] == PixelType.TERRAN:
                    if last_star_index >= 0:
                        distance = min(i - last_star_index - 1, distance)
                    break

        return distance

    def __str__(self) -> str:
        s = ''
        for i in range(self.height):
            for j in range(self.width):
                if self.star_data[i][j] == PixelType.SHOOTING_STAR:
                    s += self.star_data[i][j].value
                else:
                    s += self.terran_data[i][j].value
            s += '\n'
        return s

if __name__ == '__main__':
    stdin.readline()
    before_photo = Photo.from_string(stdin.read())
    after_photo = Photo.from_before(before_photo)
    stdout.write(str(after_photo))
