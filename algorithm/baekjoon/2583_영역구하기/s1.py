import sys
sys.stdin = open("input.txt")
from collections import deque

M, N, K = map(int, input().split())
arr = [[0]*(N+1) for _ in range(M+1)]
points = [list(map(int, input().split())) for _ in range(K)]
cnt = 0
size = []
que = deque()

# 직사각형 색칠
for k in range(K):
    a, b, x, y = points[k]
    for i in range(a, x):
        for j in range(b, y):
            arr[j][i] = 1

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

# 독립공간 갯수 체크
def bfs():
    temp = 1
    while que:
        (x, y) = que.popleft()
        for k in range(4):
            nx, ny = x+di[k], y+dj[k]
            if 0<=nx<M and 0<=ny<N and arr[nx][ny] == 0:
                que.append((nx, ny))
                arr[nx][ny] = 2
                temp += 1

    return temp


for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] = 2
            que.append((i, j))
            size.append(bfs())
            cnt += 1

size.sort()

print(cnt)
print(*size)

for q in range(M):
    print(*arr[q])