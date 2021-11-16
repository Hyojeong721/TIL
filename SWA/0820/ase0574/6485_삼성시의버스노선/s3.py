#런타임 에러 수정본
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 버스 노선 갯수

    # 계산한 버스 정류장 / 출발/도착 리스트
    bus_stop = list(0 for _ in range(5001))
    start =[0 for _ in range(5001)]
    end = [0 for _ in range(5001)]

    # 버스 노선
    bus = list(list(map(int, input().split())) for _ in range(N))
    for i in bus:
        start[i[0]] += 1
        end[i[1]] += 1

    for i in range(len(bus_stop)-1):
        bus_stop[i + 1] = bus_stop[i] + start[i + 1] - end[i]

    P = int(input())
    print("#{}".format(tc), end=" ")

    for i in range(P):
        C = int(input())
        print(bus_stop[C], end=" ")
    print()



