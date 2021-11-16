import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    # N : 버스 노선
    N = int(input())
    A = [0]
    B = [0]
    bus_station = [0] * 5001
    for _ in range(N):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
        for i in range(A[-1], B[-1]+1):
            bus_station[i] += 1
    # P : 버스 정류장 수
    P = int(input())
    p_num = [0]
    for _ in range(P):
        p_num.append(int(input()))

    print('#{} '.format(TC), end='')
    for i in range(P):
        print(bus_station[p_num[i+1]], end=' ')
    print()