import sys
from collections import deque

input = sys.stdin.readline

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
res = 'IMPOSSIBLE'

for i in range(R):
    if 'J' in arr[i] or 'F' in arr[i]:
        for j in range(C):
            if arr[i][j] == 'J':
                x, y = i, j
                visited[i][j] = 1
            if arr[i][j] == 'F':
                fx, fy = i, j
                visited[i][j] = 0

def isrange(i, j):
    if 0<=i<R and 0<=j<C:
        return True
    return False

def fire(i, j):
    global arr
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if isrange(ni, nj) and  arr[ni][nj] != '#':
            arr[ni][nj] = 'F'


def dfs(i, j):
    return

print(res)
