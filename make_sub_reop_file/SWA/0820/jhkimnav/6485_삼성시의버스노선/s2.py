import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    # N : 버스 노선
    N = int(input())
    bus_station = [0] * 5001
    start_bus = [0] * 5001
    end_bus = [0] * 5001
    for _ in range(N):
        a, b = list(map(int, input().split()))
        start_bus[a] += 1
        end_bus[b] += 1
    # P : 버스 정류장 수
    P = int(input())
    p_num = [0]
    for _ in range(P):
        p_num.append(int(input()))



    # bus_station[i] == arr
    # bus_station[i-1] : 직전 버스정류장에서 오는 버스 수
    for i in range(1, len(bus_station)):
        bus_station[i] = bus_station[i-1] + start_bus[i] - end_bus[i-1]
    print('#{} '.format(TC), end='')
    for i in range(P):
        print(bus_station[p_num[i+1]], end=' ')
    print()
