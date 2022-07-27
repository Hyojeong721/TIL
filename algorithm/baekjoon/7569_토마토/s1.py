import sys
sys.stdin = open("input.txt")
from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
res = 0
#앞, 뒤, 오른쪽, 왼쪽, 위, 아래
di, dj, dh = [-1, 1, 0, 0, 0, 0 ], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

que = deque()


for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j]==1:
                que.append((i,j,h))



while que:
    (x, y, h) = que.popleft()
    for k in range(6):
        nx, ny, nh = x + di[k], y + dj[k], h + dh[k]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H and arr[nh][nx][ny] == 0:
            arr[nh][nx][ny] = arr[h][x][y] + 1
            que.append((nx, ny, nh))



for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j]==0:
                print(-1)
                exit(0)
        res = max(res, max(arr[h][i]))

print(res-1)