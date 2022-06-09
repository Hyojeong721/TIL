import sys
sys.stdin = open('input.txt')


# 최소한으로 충전하기 = 매번 갈 수 있는 최대한 가기
def get_min_charge(K, distance, stations):
    """
    종점에 가기 위해 필요한 최소한의 충전 횟수를 구한다.
    K: 버스가 한 번 충전으로 이동 가능한 정류장 수
    distance: 버스가 이동해야 하는 정류장 수
    stations: 충전기가 설치된 정류장 번호 (배열)

    current: 현재 탐색 중인 버스의 위치
    count: 충전 횟수
    """
    current, count = 0, 0

    # 더 이상 충전이 필요없을 때까지 반복
    while current + K < distance:
        # 매번 갈 수 있는 가장 먼 충전기로 이동하여 충전
        for i in range(K, 0, -1):
            if (current + i) in stations:
                current += i
                count += 1
                break
        # 종점에 도착할 수 없는 경우 => 0 반환
        else:
            return 0

    return count


T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print("#{0} {1}".format(tc, get_min_charge(K, N, numbers)))
