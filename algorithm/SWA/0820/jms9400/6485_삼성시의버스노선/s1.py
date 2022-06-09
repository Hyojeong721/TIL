import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 버스의 수
    bus_list = [list(map(int, input().split())) for _ in range(N)]  # 버스 노선 정보
    P = int(input())  # 정류장의 수
    bus_stop = [0] * P  # 정류장 리스트
    bus_line = [0] * P  # 정류장별 지나가는 버스 수

    # 정류장 리스트 넣기
    for i in range(P):
        bus_stop[i] = int(input())

    # 버스가 정류장 지나가는지 숫자 세기
    for i in range(N):
        for n in range(P):
            if bus_stop[n] in range(bus_list[i][0], bus_list[i][1]+1):
                bus_line[n] += 1

    print('#{} {}'.format(tc, ' '.join(map(str, bus_line))))