'''
    LIVE - 숫자
        63,896 kb / 327 ms / 595 lines
'''
import sys
sys.stdin = open('input.txt')


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def DFS2(r, c, num, idx):
    if idx == 7:
        ans.add(num)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        DFS2(nr, nc, num*10 + board[nr][nc], idx+1)


T = int(input())
for tc in range(1, T + 1):
    N = 4
    board = [list(map(int, input().split())) for _ in range(N)]

    # ans = []
    ans = set()
    for i in range(N):
        for j in range(N):
            DFS2(i, j, board[i][j], 1)
    print('#{} {}'.format(tc, len(ans)))