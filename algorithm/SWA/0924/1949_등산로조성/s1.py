import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if mountain[x][y] > mountain[nx][ny]:
                dfs(nx, ny)
            elif:
                pass


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    top = 0
    for i in range(N):
        for j in range(N):
            if top < mountain[i][j]:
                top = mountain[i][j]

