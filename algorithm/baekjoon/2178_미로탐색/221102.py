import sys
sys.stdin = open('input.txt')
from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
res = -1
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
que = deque()
# visitied = [[False]*M for _ in range(N)]


que.append((1, 0, 0))
# visitied[0][0] = True


def isrange(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    return False

while que:
    # print(que)
    # for k in range(N):
    #     print(*arr[k])

    cnt, i, j = que.popleft()

    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if isrange(ni, nj) and arr[ni][nj] == 1:
            arr[ni][nj] = max(cnt+1, arr[ni][nj])
            que.append((cnt+1, ni, nj))


print(arr[N-1][M-1])