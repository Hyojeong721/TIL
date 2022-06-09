import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    for c in range(1, N):
        board[0][c] = board[0][c-1] + board[0][c]

    for r in range(1, N):
        board[r][0] = board[r-1][0] + board[r][0]
        for c in range(1, N):
            board[r][c] += min(board[r-1][c], board[r][c-1])

    print('#{} {}'.format(tc, board[N-1][N-1]))