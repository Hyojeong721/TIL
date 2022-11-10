import sys
sys.stdin = open('input.txt')

def check(c, now, i, j):
    col = ['W', "B"]
    color = {'W':"B", 'B':"W"}
    cnt = 0
    idx = c
    exp = col[c]
    for p in range(8):
        for q in range(8):
            ni, nj = i+p, j+q
            if arr[ni][nj] != exp:
                if q != 7:
                    exp = arr[ni][nj]
            else:
                cnt += 1
                exp = color[arr[ni][nj]]
        if p % 2 == 0:
            idx = (idx+1)%2
            exp = col[idx]
        else:
            idx = (idx+1)%2
            exp = col[idx]
    return cnt


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
res = 1e9

for i in range(0, N-7):
    for j in range(0, M-7):
        if arr[i][j] == 'W':
            res = min(check(1, "W", i, j), res, check(0, "B", i, j))
        else:
            res = min(res, check(0, "B", i, j), check(1, "W", i, j))

print(res)