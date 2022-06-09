import sys
sys.stdin = open('input.txt')

T = int(input())

# K, N, station 값을 받아서 충전횟수 출력하는 함수 선언
def bus(K,N,station):

    # stop: 현재 위치
    # result: 충전횟수
    stop, result = 0, 0

    # 현재위치가 N 전이면 반복
    while stop <= N:

        # 현재위치에서 최대 이동거리가 N 보다 크면 반복문 탈출
        if stop + K >= N:
            return result
        # 현재위치에서 최대이동거리를 더한 값이 station안에 있는 값이라면
        # 위치이동하고 충전횟수 추가
        elif stop + K in station:
            stop += K
            result += 1

        # 현재위치에서 최대이동거리를 더한 값이 station안에 있는 값이 아니라면
        # 1~k 값을 역순으로 더 해서 최대값과 현재 위치 사이에 station이 있는지 확인
        elif stop + K not in station:
            for k in range(K-1,0,-1):
                if stop + k in station:
                    stop += k
                    result += 1
                    break
            # 없을 경우 0 리턴
            else:
                return 0

# 충전소 위치를 station으로 선언
for test_case in range(1,T+1):
    K, N, M = list(map(int,input().split()))
    station = list(map(int,input().split()))
    print('#%d %d' %(test_case, bus(K,N,station)))
