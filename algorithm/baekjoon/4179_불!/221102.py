import sys
sys.stdin = open('input.txt')
from collections import deque

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
que = deque()
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 'IMPOSSIBLE'

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            que.append((0, i, j))
        elif arr[i][j] == 'F':
            que.append((-1, i, j))

while que:
    time, x, y = que.popleft()
    if time > -1 and arr[x][y] != 'F' and (x == 0 or y == 0 or x == R-1 or y == C-1):
        res = time + 1
        break

    for k in range(4):
        ni, nj = x+di[k], y+dj[k]
        if 0<=ni<R and 0<=nj<C and arr[ni][nj] != '#':
            if time>-1 and arr[ni][nj] == '.':
                arr[ni][nj] = '_'
                que.append((time+1, ni, nj))
            if time == -1 and arr[ni][nj] != 'F':
                arr[ni][nj] = 'F'
                que.append((-1, ni, nj))


print(res)