import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    stations = list(map(int, input().split()))

    # 이동횟수
    count = 0
    # 이동거리(위치)
    dist = 0
    # 현재 위치한 station index
    station = 0

    # 종점에 도착할 때까지 진행 (첫 정류장 멀면 출발 안 함)
    while dist <= N and stations[0] <= K:
        # 1. 다음 station 이 존재하지만 멀어서 이동 불가능한 경우, count 초기화 및 while 문 종료
        if station + 1 < M:
            if stations[station + 1] - stations[station] > K:
                count = 0
                break

        # 2. 다음 station 으로 이동 가능한 경우
        count += 1

        # 2-1. 한 번만 더 가면 종점 도착하는 경우, while 문 종료
        if dist + K >= N:
            break

        # 2-2. 갈 수 있는 가장 먼 정류장 확인
        else:
            # 감소할 station index
            s_idx = M - 1
            # 마지막 정류장부터 가까워지며 검사
            for s in stations[::-1]:
                if dist + K >= s:
                    dist = s
                    station = s_idx
                    break
                else:
                    s_idx -= 1

    # 충전횟수 = 이동횟수 - 1
    charge = 0 if count == 0 else count - 1
    print('#{} {}'.format(t, charge))