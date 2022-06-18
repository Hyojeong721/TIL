import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = [0] * (N + 1)
    temp = map(int, input().split())
    for tmp in temp:
        stations[tmp] += 1

    bus = K
    cnt = 0

    if bus > N:
        cnt = 1

    while bus < N:
        for i in range(bus, bus-K, -1):
            if stations[i] == 1:
                bus = i
                cnt += 1
                break
        else:
            cnt = 0
            break
        bus += K

    print(cnt)