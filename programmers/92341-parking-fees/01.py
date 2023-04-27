# 한 번만 돌면 끝날듯
# fees = [기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)]
# records = ["시각 차량번호 내역"]
# return = [청구할 주차 요금].sort_by(차량번호, ASC)
# 입차정보 = {차량번호 => 입차시간}
# 누적시간 = {차량번호 => 주차한 누적 시간}
# records 파싱해서 for 돌리기
#   입차했으면 입차정보에 시간 써넣기
#   출차했으면 입차정보 참고하여 누적시간 계산해서 누계하기
#           입차정보는 삭제
# 다 돌았는데 입차정보가 남아있으면 23:59에 출차한것으로 처리해서 출차정보에 누계
# 출차정보 이용해서 정산 후 차 번호로 정렬하여 출력
# 주의:
#   키로 정렬해서 출력!
#   중복 있을 수 있음!
#   바로바로 요금 계산하면 안되고 시간 누적한 다음 한 번에 계산해야함!
# defaultdict 생각하자! 편리한 라이브러리!
import datetime
from collections import defaultdict
from math import ceil

def solution(fees, records):
    입차시간 = {}
    누적시간 = defaultdict(int)
    
    for record in records:
        time, number, type = (parse_record(record))
        if type == "IN":
            입차시간[number] = time
        else:
            누적시간[number] = 누적시간.get(number, 0) + 시간계산(입차시간[number], time)
            del 입차시간[number]
            
    for number, time in 입차시간.items():
        누적시간[number] += 시간계산(입차시간[number], "23:59")
    
    주차요금 = [정산(fees, elpased_min) for number, elpased_min in sorted(누적시간.items())]

    return 주차요금

def 시간계산(in_time, out_time):
    in_time = parse_time(in_time)
    out_time = parse_time(out_time)
    elpased_min = (out_time - in_time).total_seconds() // 60
    return int(elpased_min)

def 정산(fees, elpased_min):
    기본시간, 기본요금, 단위시간, 단위요금 = fees
    if elpased_min <= 기본시간:
        return 기본요금
    else:
        청구시간 = ceil((elpased_min - 기본시간) / 단위시간)
        return 기본요금 + 청구시간 * 단위요금

def parse_time(time):
    h, m = time.split(":")
    return datetime.timedelta(hours=int(h), minutes=int(m))

def parse_record(record):
    """
    return: datetime.time(h, m), 'number', 'type'
    """
    time, number, type = record.split(" ")
    return time, number, type
