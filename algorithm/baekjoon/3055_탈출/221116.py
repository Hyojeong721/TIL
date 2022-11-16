import sys
input = sys.stdin.readline
from collections import deque


def is_range(i, j):
    if 0<=i<N and 0<=j<M:
        return True
    return False

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
res = "KAKTUS"
water = deque()
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
# 고슴도치 위치 담은 que = (x, y, cnt)
que = deque()
go = True

for i in range(N):
    for j in range(M):
        if arr[i][j] == '*':
            water.append((i, j))
        if arr[i][j] == 'S':
            que.append((i, j, 0))
go = True
# S : 두더지 / D : 동굴 / X : 돌 / * : 물
while go:
    temp_cnt = 0
    cnt_water = len(water)
    while temp_cnt < cnt_water:
        temp_cnt += 1
        wi, wj = water.popleft()
        for k in range(4):
            nwi, nwj = wi+di[k], wj+dj[k]
            if is_range(nwi, nwj) and arr[nwi][nwj] not in ('X', '*', 'D'):
                arr[nwi][nwj] = '*'
                water.append((nwi, nwj))

    temp_cnt = 0
    cnt_que = len(que)
    while temp_cnt < cnt_que and go:
        temp_cnt += 1
        si, sj, cnt = que.popleft()
        for k in range(4):
            ni, nj = si+di[k], sj+dj[k]
            if is_range(ni, nj) and arr[ni][nj] not in ('X', '*', 'S'):
                if arr[ni][nj] == 'D':
                    res = cnt+1
                    go = False
                    break
                arr[ni][nj] = 'S'
                que.append((ni, nj, cnt+1))

    if not que and not water:
        go = False

print(res)