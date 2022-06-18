import sys
sys.stdin = open('input.txt')

def check(r, c, board):
    # 가로 검사
    if board[r].count(1) >= 2:
        return True

    # 세로 검사
    cnt1 = 0
    for i in range(0, N):
        if board[i][c] == 1:
            cnt1 += 1
            if cnt1 == 2:
                return True

    # 대각선 검사
    cnt2 = 1
    cnt3 = 1
    for i in range(1, N):
        if 0 <= r-i < N and 0 <= c-i < N and board[r-i][c-i]:
            cnt2 += 1
            if cnt2 == 2:
                return True
        if 0 <= r+i < N and 0 <= c+i < N and board[r+i][c+i]:
            cnt2 += 1
            if cnt2 == 2:
                return True

        if 0 <= r+i < N and 0 <= c-i < N and board[r+i][c-i]:
            cnt3 += 1
            if cnt3 == 2:
                return True
        if 0 <= r-i < N and 0 <= c+i < N and board[r-i][c+i]:
            cnt3 += 1
            if cnt3 == 2:
                return True
    return False

def find(r, c, board):
    global cnt
    if r > 0 and check(r-1, c, board):
        return

    if r == N:
        cnt += 1
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            board[r][i] = 1
            find(r + 1, i, board)
            visited[i] = 0
            board[r][i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    cnt = 0
    visited = [0] * N
    find(0, 0, arr)
    print('#{} {}'.format(tc, cnt))