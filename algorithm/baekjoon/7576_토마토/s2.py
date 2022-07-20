import sys
from collections import deque

sys.stdin = open("input.txt")
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
res = 0
que = deque([])
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append([i, j])


def bfs():
    while que:
        x, y = que.popleft()
        for k in range(4):
            ni, nj = x+di[k], y+dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                arr[ni][nj] = arr[x][y]+1
                que.append([ni, nj])

bfs()
for ar in arr:
    for i in ar:
        if i == 0:
            print(-1)
            exit(0)
    res = max(res, max(ar))

print(res-1)