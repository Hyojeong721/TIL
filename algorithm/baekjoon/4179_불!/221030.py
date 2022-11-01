import sys
from collections import deque
input = sys.stdin.readline

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
res = 'IMPOSSIBLE'
que = deque()

# 지훈과 불 위치 저장
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            que.append((0, i, j))
        elif arr[i][j] == 'F':
            que.append((-1, i, j))

def isrange(i, j):
    if 0 <= i < R and 0 <= j < C:
        return True
    return False


while que:
    time, x, y = que.popleft()
    if time > -1 and arr[x][y] != 'F' and (x == 0 or y == 0 or x == R-1 or y == C-1):
        res = time + 1
        break


    for k in range(4):
        ni, nj = x+di[k], y+dj[k]
        if isrange(ni, nj) and arr[ni][nj] != '#':
            if time > -1 and arr[ni][nj] == '.':
                arr[ni][nj] = '_'
                que.append((time+1, ni, nj))
            elif time == -1 and arr[ni][nj] != 'F':
                arr[ni][nj] = 'F'
                que.append((-1, ni, nj))



print(res)

