from typing import Tuple, List
from collections import deque

class Worker():
    # [duration]
    queue: deque
    # [work_index]
    done: List[int]
    duration: int
    work_index: int

    def __init__(self, duration: int):
        self.duration = duration
        self.queue = deque()
        self.done = []

    def work(self) -> bool:
        if self.queue and self.queue[0]:
            self.queue[0] -= 1
            if self.queue[0] == 0:
                self.done.append(self.queue.popleft())
            return True

    def consume_work_queue(self, work_index: int):
        self.work_index = work_index

    def add_work(self, index: int, duration: int):
        self.queue.append(duration)

    def is_working(self):
        return len(self.queue) != 0

def parse_line(line: str) -> Tuple[int, str, int]:
    a, b, c = line.split()
    return [int(a), b, int(c)]

if __name__ == '__main__':
    import sys
    a, b, _ = map(int, sys.stdin.readline().split())
    orders = deque(map(parse_line, sys.stdin.read().split('\n')))

    sangmin = Worker(a)
    jisu = Worker(b)

    elpased = 0
    work_index = 1
    while True:
        if orders and orders[0][0] == elpased:
            order_at, color, amount = orders.popleft()
            for _ in range(amount):
                if color == 'B':
                    sangmin.add_work(amount)
                else:
                    jisu.add_work(amount)
        if not sangmin.work():
            sangmin.consume_work_queue(work_index)
        if not jisu.work():
            jisu.consume_work_queue(work_index)
        elpased += 1

        if not sangmin.is_working() and not jisu.is_working() and not orders:
            break
    print(len(sangmin.done))
    print(' '.join(map(str, sangmin.done)))
    print(len(jisu.done))
    print(' '.join(map(str, jisu.done)))
