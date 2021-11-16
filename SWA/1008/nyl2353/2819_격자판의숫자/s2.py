'''
    LIVE - 문자열
        68,212 kb / 390 ms / 634 lines
'''
import sys
sys.stdin = open('input.txt')


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def DFS(r, c, line):
    if len(line) == 7:
        ans.add(line)
        # if line not in ans:
        #     ans.append(line)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        DFS(nr, nc, line + board[nr][nc])


T = int(input())
for tc in range(1, T + 1):
    N = 4
    board = [list(input().split()) for _ in range(N)]

    # ans = []
    ans = set()
    for i in range(N):
        for j in range(N):
            DFS(i, j, board[i][j])
    print('#{} {}'.format(tc, len(ans)))