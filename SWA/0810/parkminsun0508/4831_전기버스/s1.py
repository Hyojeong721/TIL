# swea 4831 전기버스
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램 만들기
import sys
sys.stdin = open('input.txt')
# 먼저, 노선 수 T를 받는다.
T = int(input())
# 각 노선마다 반복하여 확인한다.
for c in range (1, T+1):
    # K, N, M을 받아온다.
    K, N, M = map(int, input().split())
    # 버스충전에 대한 리스트를 받는다.
    bus_charge = list(map(int, input().split()))

    # 충전횟수와 버스 위치에 대한 초기 설정
    charge = 0
    location = 0
    # 현재 위치에서 한 번 충전으로 최대 이동할 수 있는 K가 종점인 N보다 작다면,
    # 계속 반복하여 실행한다.
    while location + K < N:
        # 만약 종점까지의 거리가 현재 위치에서의 이동가능거리 이하라면 충전할 필요없다.
        if location + K >= N:
            break
        # 최대 갈 수 있는 거리인 K부터 한칸씩 줄이며 반복 작업하며 생각한다.
        for i in range(K, -1, -1):
            # i 가 0이라면 이동 가능 거리 중 충전기가 없다는 뜻이기에 charge 를 0으로 바꾸고 while문에서 벗어나게한다.
            if i == 0:
                charge = 0
                location += N
            elif (i + location) in bus_charge:
                charge += 1
                location += i
                break

    print('#{} {}'.format(c, charge))








