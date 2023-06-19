from typing import List, Self, Tuple
from enum import Enum, auto

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def __str__(self):
        return self.name

    def clockwise(self) -> Self:
        if self.name == 'UP':
            return self.RIGHT
        elif self.name == 'RIGHT':
            return self.DOWN
        elif self.name == 'DOWN':
            return self.LEFT
        elif self.name == 'LEFT':
            return self.UP

def next(x: int, y: int, direction: Direction) -> Tuple[int, int]:
    if direction == Direction.UP:
        return (x, y - 1)
    elif direction == Direction.DOWN:
        return (x, y + 1)
    elif direction == Direction.LEFT:
        return (x - 1, y)
    elif direction == Direction.RIGHT:
        return (x + 1, y)

class Snail():
    ns: List[List[int]]
    target_number_position: Tuple[int, int]

    def __init__(self, n: int, target_number: int):
        self.ns = [[0 for _ in range(0, n)] for _ in range(0, n)]

        x = y = n // 2
        # current_level: means the root of the target number of the inner
        # cycle square.
        # TODO
        current_level = 1
        stack = []
        for i in range(1, n * n + 1):
            self.ns[y][x] = i
            if i == target_number:
                self.target_number_position = (x, y)
            if i == current_level ** 2:
                current_level += 2
                stack += [Direction.UP] * (current_level - 1)
                stack += [Direction.LEFT] * (current_level - 1)
                stack += [Direction.DOWN] * (current_level - 1)
                stack += [Direction.RIGHT] * (current_level - 2)
                stack.append(Direction.UP)
            x, y = next(x, y, stack.pop())
 
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.ns])
    
if __name__ == '__main__':
    n = int(input())
    target_number = int(input())

    if n % 2 == 0:
        raise ValueError('input can not be even number.')

    s = Snail(n, target_number)
    print(s)
    x, y = s.target_number_position
    print(y + 1, x + 1)
