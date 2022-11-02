import sys
sys.stdin = open('input.txt')
from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
res = -1
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
que = deque()
que.append((0, 0))

def isrange(i, j):
    if 0<=i<N and j <= j < M:
        return True
    return False

while que:
    i, j = que.popleft()
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if isrange(ni, nj) and arr[ni][nj] == 1:
            que.append((ni, nj))
            arr[ni][nj] = arr[i][j] + 1

print(arr[N-1][M-1])