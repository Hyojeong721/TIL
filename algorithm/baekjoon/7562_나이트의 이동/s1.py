import sys
sys.stdin = open("input.txt")
from collections import deque

di = [-2, -2, -1, -1, 1, 1, 2, 2]
dj = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs():
    global que, visited
    while que:
        (x, y, cnt)  = que.popleft()
        if (x, y) == (want_x, want_y):
            return cnt
        for k in range(8):
            ni, nj = x + di[k], y + dj[k]
            if 0 <= ni < L and 0 <= nj < L and visited[ni][nj] == 0:
                visited[ni][nj]=1
                que.append((ni, nj, cnt + 1))
    return cnt

N = int(input())
for _ in range(N):
    L  = int(input())
    now_x, now_y = map(int, input().split())
    want_x, want_y = map(int, input().split())
    visited = [[0]*L for _ in range(L)]
    que = deque()
    que.append((now_x, now_y, 0))

    res = bfs()
    print(res)


