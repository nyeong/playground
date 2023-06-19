from typing import List, Tuple, NewType, Self
from enum import Enum

class CellType(Enum):
    UNCLEAN = 0
    WALL = 1
    CLEAN = 2

    def __str__(self) -> str:
        if self == self.UNCLEAN:
            return "."
        elif self == self.WALL:
            return "X"
        elif self == self.CLEAN:
            return " "

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def anticlockwise(self) -> Self:
        if self == self.NORTH:
            return self.WEST
        elif self == self.WEST:
            return self.SOUTH
        elif self == self.SOUTH:
            return self.EAST
        elif self == self.EAST:
            return self.NORTH

class Position(Tuple[int, int]):
    delta_map = {
        Direction.NORTH: (0, -1),
        Direction.EAST: (+1, 0),
        Direction.SOUTH: (0, +1),
        Direction.WEST: (-1, 0),
    }

    @classmethod
    def forward(cls, pos: Self, dir: Direction) -> Self:
        x, y = pos
        dx, dy = cls.delta_map[dir]
        return (x + dx, y + dy)

    @classmethod
    def backward(cls, pos: Self, dir: Direction) -> Self:
        x, y = pos
        dx, dy = cls.delta_map[dir]
        return (x - dx, y - dy)

class Room():
    room: List[List[CellType]]
    def __init__(self, str: str):
        """
        Parse a given string and create new Room
        """
        lines = str.split("\n")
        self.room = [
            [CellType(int(cell)) for cell in line.split()] for line in lines
        ]

    def is_unclean(self, position: Position) -> bool:
        x, y = position
        return self.room[y][x] == CellType.UNCLEAN

    def is_wall(self, position: Position) -> bool:
        x, y = position
        return self.room[y][x] == CellType.WALL

    def set_clean(self, position: Position):
        x, y = position
        self.room[y][x] = CellType.CLEAN

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, line)) for line in self.room])

class Roomba:
    current: Position
    heading: Direction
    room: Room
    clean_count: int

    def __init__(self, position: Position, room: Room, heading: Direction):
        """
        :param position: 초기 시작 위치 (x, y)
        """
        self.current = position
        self.room = room
        self.heading = heading
        self.clean_count = 0

    def run(self):
        while self.next_step():
            pass

    def next_step(self) -> bool:
        """
        Returns False if there is no next step.
        """
        if self.room.is_unclean(self.current):
            self.room.set_clean(self.current)
            self.clean_count += 1
        adjacents = self.adjacent_positions()
        if not any(map(lambda x: self.room.is_unclean(x), adjacents)):
            backward = Position.backward(self.current, self.heading)
            if not self.room.is_wall(backward):
                self.current = backward
            else:
                return False
        else:
            self.heading = self.heading.anticlockwise()
            forward = Position.forward(self.current, self.heading)
            if self.room.is_unclean(forward):
                self.current = forward
        return True

    def adjacent_positions(self) -> List[Position]:
        x, y = self.current
        deltas = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
        return [(x + xd, y + yd) for (xd, yd) in deltas]

if __name__ == '__main__':
    import sys
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    room = Room(sys.stdin.read())
    roomba = Roomba((c, r), room, Direction(d))
    roomba.run()
    print(roomba.clean_count)
