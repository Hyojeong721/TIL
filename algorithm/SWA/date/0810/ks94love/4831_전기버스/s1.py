import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    K, N, M = list(map(int, input().split()))
    station_numbers = list(map(int, input().split()))
    # s는 현재위치, count는 충전한 횟수
    s = 0
    count = 0

    for j in range(M):
        # 첫번째 충전소가 K보다 크면 안됨
        if station_numbers[0] > K:
            count = 0
            break

        # 충전소 끼리의 거리가 K보다 크면 충전 안됨
        if station_numbers[j] - station_numbers[j-1] > K:
            count = 0
            break

        # 마지막 충전소 위치와 도착지 사이의 거리가 K보다 크면 안됨
        if N - station_numbers[-1] > K:
            count = 0
            break

        # 이동한 곳에 충전소 있으면 거기서 충전함
        if s + K == station_numbers[j]:
            s = station_numbers[j]
            count += 1

        # 현재 위치에서 K만큼 이동했을 때 충전소의 위치가 더 멀면 그 앞의 충전소에서 충전함
        if s + K < station_numbers[j]:
            s = station_numbers[j-1]
            count += 1

        # [-2]째 충전소에서 충전하고 도착지에 도착하지 못하면 [-1]째 충전소에서 충전함
        if station_numbers[-1] < s + K < N:
            s = station_numbers[-1]
            count += 1

        # 현재 위치가 도착지보다 크거나 같으면 반복문 종료
        if s >= N:
            break


    print('#{} {}'.format(i+1, count))
