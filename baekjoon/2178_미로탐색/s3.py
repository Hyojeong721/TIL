import sys
sys.stdin = open('input.txt')
from collections import deque

n, m = map(int,(input().split()))
arr = []
for i in range(n):
    arr.append(list(input()))

q = deque()
q.append([0, 0])
arr[0][0]=1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while q:
    temp = q.popleft()
    a, b = temp[0], temp[1]

    for i in range(4):
        x, y = a+dx[i], b+dy[i]
        if 0<=x<n and 0<=y<m and arr[x][y] =='1':
            arr[x][y] = arr[a][b] + 1
            q.append([x,y])
print(arr[n-1][m-1])

