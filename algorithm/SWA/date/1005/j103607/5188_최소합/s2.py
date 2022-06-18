import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split()))+[999] for _ in range(N)] + [[999]*(N+1)]

    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):

            if i == N-1 and j == N-1:   # 보드 맨 오른쪽 아래는 패스
                pass
            elif board[i][j+1] < board[i+1][j]:
                board[i][j] = board[i][j] + board[i][j+1]
            else:
                board[i][j] = board[i][j] + board[i+1][j]

    print('#{} {}'.format(tc, board[0][0]))
