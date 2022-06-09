# s1.py의 코드가 SWEA에서는 통과했으나, 백준에서는 시간 초과가 떴다.
# N이 최대 15인 조건에서도 통과할 수 있는 코드를 짜고자 시도했으나, 역시 시간 초과가 떴다.

import sys
sys.stdin = open('input.txt')


def get_n_queen(count, points):
    """
    n x n의 보드에 n개의 퀸을 서로 공격하지 못하게 놓는 경우의 수를 구한다.
    Args:
        count: 현재까지 놓은 퀸의 개수
        points: 현재까지 놓은 퀸의 위치 (list)
                ex. (0, 0)과 (1, 6)에 놓았다면 [0, 6]
    """
    global N

    if count == N:
        global total
        total += 1
        return

    promising = set(range(N))
    to_delete = set()

    # 현재 탐색하는 열에서 현재까지 놓은 퀸이 공격 가능한 행을 모두 to_delete에 추가한다.
    for r, c in enumerate(points):
        # 1. 위쪽 위치 검사
        to_delete.add(c)
        # 2. 왼쪽 위 대각선 검사
        to_delete.add(c + count - r)
        # 3. 오른쪽 위 대각선 검사
        to_delete.add(c - count + r)

    # promising에 현재까지 놓은 퀸이 공격할 수 없는 행만 남긴다.
    promising -= to_delete

    for i in promising:
        get_n_queen(count + 1, points + [i])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    total = 0

    get_n_queen(0, [])
    print("#{} {}".format(tc, total))
