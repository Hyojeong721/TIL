import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K: 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N: 종점
    # M: 충전기 설치 정류장 수
    K, N, M = map(int, input().split())
    battery = list(map(int, input().split()))
    stations = [0] * N
    now = 0
    charge = 0
    for i in battery:
        stations[i] += 1

    while now < N:
        back = 0
        now += K

        if now >= N:
            break
        else:
            while stations[now] != 1:
                now -= 1
                back += 1

        if back >= K:
            charge = 0
            break

        charge += 1


    print('#{0} {1}'.format(tc, charge))