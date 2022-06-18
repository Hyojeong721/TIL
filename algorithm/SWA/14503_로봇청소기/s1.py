import sys
sys.stdin = open("input.txt")


def left_dir(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


def back_dir(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


def is_range(i, j):
    if 0<=i<N and 0<=j<M:
        return True
    return False


def process():
    global res, d, r, c

    while True:
        if not visited[r][c] and arr[r][c] == 0:
            visited[r][c] = True
            res += 1
        # a
        for i in range(4):
            d = left_dir(d)
            ni, nj = r+di[d], c+dj[d]
            if is_range(ni, nj) and not visited[ni][nj] and arr[ni][nj] == 0:
                r, c = ni, nj
                break
        else:
            dir = back_dir(d)
            bi, bj = r + di[dir], c+dj[dir]
            if is_range(bi, bj) and arr[bi][bj] == 1:
                return
            else:
                r, c = bi, bj




N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

res = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            visited[i][j] = True
process()

print(res)