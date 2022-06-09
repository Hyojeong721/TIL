import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # K : 한번 충전으로 이동가능한 정류장 수
    # N : 종점 정류장 번호
    # M : 충전기가 설치된 정류장 갯수
    K, N, M = list(map(int, input().split()))
    charge_stations = list(map(int, input().split()))
    charge_cnt = 0
    next_charge_station_idx = 0
    pre_station_no = 0

    fuelCnt = K
    while fuelCnt >= 0 and pre_station_no != N:
        # 다음 충전소가 아직 남아있다면
        if next_charge_station_idx+1 <= M-1:
            # 충전 할 필요가 없는 상황
            if fuelCnt >= charge_stations[next_charge_station_idx+1] - pre_station_no:
                # 충전을 하지 않았지만, 현재 충전소가 있는 위치라면, 충전소 idx 1 증가
                for i in range(M):
                    if pre_station_no == charge_stations[i]:
                        next_charge_station_idx += 1
            # 충전 O
            elif pre_station_no == charge_stations[next_charge_station_idx]:
                fuelCnt = K
                next_charge_station_idx += 1
                charge_cnt += 1
        # 마지막 충전소
        elif fuelCnt < N - pre_station_no:

            for i in range(M):
                if pre_station_no == charge_stations[i]:
                    fuelCnt = K
                    charge_cnt += 1
                    break
        pre_station_no += 1
        fuelCnt -= 1

    if pre_station_no != N:
        charge_cnt = 0
    print('#{} {}'.format(test_case, charge_cnt))