import sys
sys.stdin = open('input.txt')

from collections import deque

res_fox, res_sheep = 0, 0
c, r = map(int, input().split())
arr = [list(input()) for _ in range(c)]
di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]
visited = [[False]*r for _ in range(c)]
visited[0][0] = True

def is_range(i, j):
    if 0<=i<c and 0<=j<r:
        return True
    return False


def bfs(i, j):
    que = deque()
    que.append((i, j))
    fox, sheep = 0, 0
    while que:
        now_i, now_j = que.popleft()
        if arr[now_i][now_j] == 'v':
            fox += 1
        elif arr[now_i][now_j] == 'k':
            sheep += 1

        for k in range(4):
            ni, nj = now_i+di[k], now_j+dj[k]
            if is_range(ni, nj) and arr[ni][nj] != '#' and not visited[ni][nj]:
                que.append((ni, nj))
                visited[ni][nj] = True
    return sheep, fox


for x in range(c):
    for y in range(r):
        if arr[x][y] != '#' and not visited[x][y]:
            visited[x][y] = True
            s, f = bfs(x, y)
            if f < s:
                res_sheep += s
            else:
                res_fox += f

print(res_sheep, res_fox)