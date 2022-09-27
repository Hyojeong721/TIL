import sys
input = sys.stdin.readline
# sys.stdin =open('input.txt')
sys.setrecursionlimit(15000)
def is_range(i, j):
    if 0<=i<h and 0<=j<w:
        return True
    return False

def dfs(i, j):
    global visited

    for k in range(8):
        ni, nj = i+di[k], j+dj[k]
        if is_range(ni, nj) and arr[ni][nj]:
            if not visited[ni][nj]:
                visited[ni][nj] = True
                dfs(ni, nj)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = list(list(map(int, input().split())) for _ in range(h))
    visited = [[False]*w for _ in range(h)]

    di, dj = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    res = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                res += 1
    print(res)