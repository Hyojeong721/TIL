import sys
input = sys.stdin.readline
from collections import deque


def is_range(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    return False


# NxN, 1<= 바이러스<=K
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# S초 뒤에 X, Y 자리에 있는 바이러스는? res
S, X, Y = map(int, input().split())
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
que = deque()

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            que.append((0, arr[i][j], i, j))


while que:
    time, virus, i, j = que.popleft()
    if time == S:
        break

    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if is_range(ni, nj) and arr[ni][nj] == 0:
            arr[ni][nj] = virus
            que.append((time+1, virus, ni, nj))

print(arr[X-1][Y-1])

