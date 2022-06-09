import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):

    T = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    result = []

    # 행의 합
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += board[i][j]
        result.append(sum_row)

    # 열의 합
    for j in range(100):
        sum_col = 0
        for i in range(100):
            sum_col += board[i][j]
        result.append(sum_col)

    # 대각선1의 합 (왼쪽 위 -> 오른쪽 아래)
    sum_diag1 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum_diag1 += board[i][j]
    result.append(sum_diag1)

    # 대각선2의 합 (오른쪽 위 -> 왼쪽 아래)
    sum_diag2 = 0
    for i in range(100):
        for j in range(99, -1, -1):
            if i + j == 99:
                sum_diag2 += board[i][j]
    result.append(sum_diag2)

    # 대각선2의 합 (왼쪽 아래 -> 오른쪽 위)
    # sum_diag2 = 0
    # for i in range(100):
    #     for j in range(100):
    #         if i == 99 - j:
    #             sum_diag2 += board[i][j]
    # result.append(sum_diag2)

    # 행, 열, 대각선의 합 중 최대값
    answer = 0
    for r in result:
        if answer < r:
            answer = r

    print('#{} {}'.format(tc, answer))