#런타임 에러
import sys
sys.stdin = open('s_input.txt')

T = int(input())

def check(P):
    global start, end, bus_stop, bus

    for i in bus:
        start[i[0]] += 1
        end[i[1]] += 1

    for i in range(P):
        bus_stop[i + 1] = bus_stop[i] + start[i + 1] - end[i]

    return bus_stop[1:P+1]

for tc in range(1, T+1):
    N = int(input()) # 버스 노선 갯수
    # 버스 노선
    bus = list(list(map(int, input().split())) for _ in range(N))
    # 알고자하는 버스정류장 갯수
    P = int(input())
    # 버스 정류장 리스트
    bus_stop = list(0 for _ in range(5001))
    # 출발/도착 리스트
    start =[0 for _ in range(5001)]
    end = [0 for _ in range(5001)]

    print("#{} {}".format(tc, check(P)))




