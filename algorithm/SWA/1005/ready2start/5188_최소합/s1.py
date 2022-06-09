import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = []

    for _ in range(N):
        board.append([int(x) for x in input().split()])

    for i in range(1, N):
        # 맨 윗 줄의 최소 합계를 구한다.
        board[0][i] += board[0][i - 1]
        # 맨 왼쪽 줄의 최소 합계를 구한다.
        board[i][0] += board[i - 1][0]

    # 나머지 칸의 최소 합계를 구한다.
    for r in range(1, N):
        for c in range(1, N):
            # 어떤 칸의 최소 합계 = 위 칸의 최소 합계와 왼쪽 칸의 최소 합계 중 더 작은 값 + 해당 칸의 값
            board[r][c] += min(board[r - 1][c], board[r][c - 1])

    print("#{} {}".format(tc, board[N - 1][N - 1]))
