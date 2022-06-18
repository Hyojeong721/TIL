import sys
sys.stdin = open("input.txt")
"""
문제: 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는가?

K = 한 번의 충전으로 최대 이동할 수 있는 정류장의 수
N = 종점 정류장 번호 (N 숫자에 도착 종료)
M = 충전기가 설치된 정류장 수
배열 = 충전기가 설치된 정류장 번호
"""

def getMinCharge(K, distance, stations):
    """
    :param K : 한 번의 충전으로 이동 가능한 정류장 수
    :param stations: 충전기가 설치된 정류장 번호의 1차원 리스트
    :param distance: 버스가 이동해야 하는 정류장 수

    :return: 도착지까지의 최소 충전 횟수, 미도착시 0

    current = 버스의 현위치
    count = 충전 횟수
    """
    current, count = 0, 0

    # 더 이상 충전이 필요 없을 때까지 반복
    while current + K < distance:
        # 매번 최대 이동거리만큼 이동, 충전기가 없으면 최대이동거리 -1 만큼 이동, 반복
        for i in range(K, 0, -1):
            # 만약 정류장을 발견하면 충전하고 for문을 빠져나가 다시 K만큼 이동 (while문 반복)
            # 발견하지 못하면, 거리를 1씩 줄여나가며 이동
            if current + i in stations:
                current += i
                count += 1
                break
        # 정류장에 도착하지 못하는 경우 0을 반환
        else: return 0

    return count


T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print("#{} {}".format(tc, getMinCharge(K, N, numbers)))

