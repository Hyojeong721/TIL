import sys
from collections import deque

sys.stdin = open("input.txt")

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
que = deque([])
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append([i, j])


def bfs():
    global que

    while que:
        x, y = que.popleft()
        for k in range(4):
            ni, nj = x+di[k], y+dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                arr[ni][nj] = arr[x][y] + 1
                que.append([ni, nj])


bfs()
print(arr)
for i in arr:
    for k in i:
        if k == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans-1)