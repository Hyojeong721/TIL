import sys
# input = sys.stdin.readline
sys.setrecursionlimit(15000)
sys.stdin = open('input.txt')
from collections import deque

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def is_range(i, j):
    if 0<=i<n and 0<=j<m:
        return True
    return False

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
# visited = [[0]*m for _ in range(n)]
que = deque()
que.append((0, 0))
arr[0][0] = 1

while que:
    i, j = que.popleft()

    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if is_range(ni, nj) and arr[ni][nj]=='1':
            que.append((ni, nj))
            arr[ni][nj] = arr[i][j] + 1


print(arr[n-1][m-1])