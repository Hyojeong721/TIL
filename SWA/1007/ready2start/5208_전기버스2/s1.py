import sys
sys.stdin = open('input.txt')


def get_min_exchange(count, idx):
    """
    목적지에 도착하기 위한 충전지 최소 교체 횟수를 구한다. (전역변수 min_count에 저장)
    Args:
        count: 현재까지의 충전지 교체 횟수
        idx: 현재 위치 인덱스
    """
    global N, batteries, min_count

    # 백트래킹 - 현재까지의 교체 횟수가 min_count 이상이라면 탐색 종료
    if count >= min_count:
        return

    # 목적지에 도착한 경우
    if idx >= N - 1:
        min_count = min(min_count, count)
        return

    # DFS 알고리즘을 이용하여 갈 수 있는 경로들을 탐색한다.
    for k in range(1, batteries[idx] + 1):
        get_min_exchange(count + 1, idx + k)


T = int(input())

for tc in range(1, T + 1):
    N, *batteries = map(int, input().split())
    min_count = 1000

    get_min_exchange(0, 0)
    print("#{} {}".format(tc, min_count - 1))
