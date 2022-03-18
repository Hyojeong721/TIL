from collections import deque
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
print(arr)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
q.append([0, 0])
arr[0][0] =1
while q:
    a, b = q.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and arr[x][y] == '1':
            arr[x][y] = arr[a][b]+1
            q.append([x, y])
print(arr)
print(arr[n-1][m-1])


