import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [list(input()) for _ in range(N)]

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def is_range(i, j):
    if 0<=i<N and 0<=j<N:
        return True
    return False

def person(i, j):
    global visited
    temp = [(i, j)]
    color = arr[i][j]
    visited[i][j] = True
    while temp:
        x, y = temp.pop(0)
        for k in range(4):
            ni, nj = x + di[k], y+dj[k]
            if is_range(ni, nj) and arr[ni][nj] == color and not visited[ni][nj]:
                visited[ni][nj] = True
                temp.append((ni, nj))
cnt, cnt_rg = 0, 0

visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            person(i, j)
            cnt += 1
for i in range(N):
    for j in range(N):
        visited[i][j] = False
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            person(i, j)
            cnt_rg += 1

print(cnt, cnt_rg)