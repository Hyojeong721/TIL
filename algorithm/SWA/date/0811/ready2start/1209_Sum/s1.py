import sys
sys.stdin = open('input.txt')


def get_max_value(board, N):
    """
    2차원 배열 board의 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구한다.
    N: board의 행/열의 개수

    max_value: 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값
    """
    max_value = 0

    # 1. 각 행의 합
    for r in range(N):
        sub_total = 0
        for c in range(N):
            sub_total += board[r][c]

        if sub_total > max_value:
            max_value = sub_total

    # 2. 각 열의 합
    for c in range(N):
        sub_total = 0
        for r in range(N):
            sub_total += board[r][c]

        if sub_total > max_value:
            max_value = sub_total

    # 3. 각 대각선의 합
    # sub_total1: (왼쪽 위 => 오른쪽 아래) 대각선의 합
    # sub_total2: (오른쪽 위 => 왼쪽 아래) 대각선의 합
    sub_total1, sub_total2 = 0, 0

    for r in range(N):
        sub_total1 += board[r][r]
        sub_total2 += board[r][N - 1 - r]

    if sub_total1 > max_value:
        max_value = sub_total1
    if sub_total2 > max_value:
        max_value = sub_total2

    return max_value


T = 10

for _ in range(T):
    tc = int(input())
    N = 100
    board = []

    for _ in range(N):
        sub_board = list(map(int, input().split()))
        board.append(sub_board)

    max_value = get_max_value(board, N)
    print("#{} {}".format(tc, max_value))
