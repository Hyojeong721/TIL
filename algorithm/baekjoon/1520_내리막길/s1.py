import sys
sys.stdin = open("input.txt")

sys.setrecursionlimit(10000000)
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

visited = [[-1 for _ in range(N)] for __ in range(M)]

# 아래, 왼쪽, 오른쪽
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(i, j):
    if (i, j) == (M-1, N-1):
        return 1

    if visited[i][j] != -1:
        return visited[i][j]

    visited[i][j] = 0
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] < arr[i][j]:
            visited[i][j] += dfs(ni, nj)
    return visited[i][j]

print(dfs(0, 0))
