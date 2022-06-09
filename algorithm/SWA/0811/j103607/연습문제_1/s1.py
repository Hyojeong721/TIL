import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 우 하 좌 상 (시계방향)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    # 현재 위치 = board[i][j]
                    total += abs(board[i][j] - board[ni][nj])
    print('#{} {}'.format(tc, total))
