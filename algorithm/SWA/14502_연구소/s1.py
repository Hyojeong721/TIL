import sys
from collections import deque
import copy
sys.stdin = open("input.txt")



def is_range(ni, nj):
    if 0 <= ni < N and 0 <= nj < M:
        return True
    return False


def virus():
    que = deque()
    temp = copy.deepcopy(arr)


    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                que.append((i, j))

    while que:
        x, y = que.popleft()
        for k in range(4):
            ni, nj = x+di[k], y+dj[k]
            if not is_range(ni, nj):
                continue
            if temp[ni][nj] == 0:
                temp[ni][nj] = 2
                que.append((ni, nj))
    global ans

    cnt = 0
    for i in range(N):
        cnt += temp[i].count(0)
    ans = max(ans, cnt)


def makewall(cnt):
    if cnt == 3:
        virus()
        return

    for n in range(N):
        for m in range(M):
            if arr[n][m] == 0:
                arr[n][m] = 1
                makewall(cnt+1)
                arr[n][m] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

makewall(0)
print(ans)