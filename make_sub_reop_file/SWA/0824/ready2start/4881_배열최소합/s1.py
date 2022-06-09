# 재귀 (시간 초과 풀이)
# 210825 => 가지치기를 도입하여 시간 초과 해결

import sys
sys.stdin = open('input.txt')


def get_min_sum(board, N, r, cursum):
    """
    배열에서 한 줄에 하나씩 숫자를 골랐을 때의 합의 최소값을 구한다.
      - 단, 같은 행(세로)에서 두 개 이상의 숫자를 고를 수 없다.
    Args:
        board: 2차원 배열
        N: 배열의 가로, 세로 길이
        r: 현재 탐색중인 열
        cursum: 현재까지의 합
    Returns:
        min_sum: 한 줄에 하나씩 숫자를 골랐을 때의 최소합
    """
    # 함수 바깥의 min_sum 전역변수에 접근
    global min_sum

    # 아직 탐색 중인데 현재까지의 합이 min_sum 이상이 된 경우 => 탐색 종료 (가지치기)
    if cursum >= min_sum:
        return

    # 마지막 열까지 탐색을 마친 경우
    # => 현재까지의 합이 min_sum보다 작으면 min_sum에 현재까지의 합 대입
    if r == N:
        if cursum < min_sum:
            min_sum = cursum
    else:
        for c in range(N):
            if not col_selected[c]:
                col_selected[c] = True
                get_min_sum(board, N, r + 1, cursum + board[r][c])
                col_selected[c] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]

    col_selected = [False] * N
    min_sum = 100

    get_min_sum(board, N, 0, 0)

    print("#{} {}".format(tc, min_sum))
