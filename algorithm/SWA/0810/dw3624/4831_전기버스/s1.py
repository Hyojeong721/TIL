import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
     # 입력값 변수 할당
    k, n, M = map(int, input().split())
    M_list = list(map(int, input().split()))

    # 충전소 위치 리스트 생성
    station = [0] * (n+1)
    for m in M_list:
        station[m] = 1
    print(station)


    cnt = 0   # 충전 횟수
    bus = k   # 버스의 현재 위치

    # 버스가 충전없이 한번에 종점에 도착하는 경우
    if bus > n:
        cnt = 1

    # 버스가 종점에 도착할때까지 반복
    while bus < n:
        # 하나씩 왼쪽으로 이동하며 충전기가 있는 정류장 탐색
        for i in range(bus, bus-k, -1):
            # 충전기 있는 정류장 찾은 경우, 충전횟수 1회 추가 & 버스 위치 재설정
            if station[i]:
                cnt += 1
                bus = i
                break

        # 충전기 있는 정류장을 못 찾은 경우, 충전횟수 0회 반환 & break
        else:
            cnt = 0
            break

        # 최대 이동거리 이동
        bus += k

    print('#{} {}'.format(t, cnt))