import sys
sys.stdin = open('input.txt')

T = int(input())

dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]

def move(r, c, moved):
    global result
    visited[r][c] = 1
    if mat[r][c] == 'L':
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]: continue

            if mat[nr][nc] == 'L':
                move(nr, nc, moved + 1)
            elif mat[nr][nc] == 'W':
                result += moved
    visited[r][c] = 0

for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    result = 0
    for i in range(M):
        for j in range(N):
            move(j, i, 0)

    print(result)

