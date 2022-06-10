import sys
import copy
sys.stdin = open("input.txt")

N = int(input())
arr_p = [list(input()) for _ in range(N)]
arr_r = copy.deepcopy(arr_p)
# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def is_range(i, j):
    if 0<=i<N and 0<=j<N:
        return True
    return False

def person(i, j):
    global arr_p

    temp = [(i, j)]
    color = arr_p[i][j]
    arr_p[i][j] = 0
    while temp:
        x, y = temp.pop(0)
        for k in range(4):
            ni, nj = x + di[k], y+dj[k]
            if is_range(ni, nj) and arr_p[ni][nj] == color:
                arr_p[ni][nj] = 0
                temp.append((ni, nj))
def redgreen(i, j):
    global arr_r
    color = arr_r[i][j]
    temp = [(i, j)]
    arr_r[i][j] = 0
    while temp:
        # print(temp)
        x, y = temp.pop(0)
        for k in range(4):
            ni, nj = x + di[k], y + dj[k]
            if is_range(ni, nj):
                if color != 'B' and arr_r[ni][nj] == 'R' or arr_r[ni][nj] == 'G':
                    arr_r[ni][nj] = 0
                    temp.append((ni, nj))
                elif color == 'B' and arr_r[ni][nj] == 'B':
                    arr_r[ni][nj] = 0
                    temp.append((ni,nj))
cnt, cnt_rg = 0, 0

for i in range(N):
    for j in range(N):
        if arr_p[i][j] != 0:
            person(i, j)
            cnt += 1
        # print(arr_p)
        if arr_r[i][j] != 0:
            redgreen(i, j)
            cnt_rg += 1
print(cnt, cnt_rg)