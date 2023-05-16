from heapq import heappush, heappop

def solution(book_times):
    max_room_count = 0
    rooms = []
    for [start, end] in sorted(book_times, key=lambda x: x[0]):
        end = add_cleaning_time(end)
        if rooms and rooms[0] <= start:
            heappop(rooms)
        heappush(rooms, end)
        max_room_count = max(max_room_count, len(rooms))
    return max_room_count

def add_cleaning_time(string):
    hour, min = map(int, string.split(':'))
    min += 10
    if min >= 60:
        min -= 60
        hour += 1
    return f'{hour:02}:{min:02}'
