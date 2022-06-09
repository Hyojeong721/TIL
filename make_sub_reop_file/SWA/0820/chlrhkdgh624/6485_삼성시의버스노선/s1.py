import sys
sys.stdin = open("s_input.txt")


def count_bus(bus_stop):
    cnt = 0
    for i in range(N):
        if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_route = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())
    result = []

    for i in range(P):
        C = int(input())
        result.append(count_bus(C))

    print(f'#{tc}', end=' ')
    print(' '.join(map(str, result)))




