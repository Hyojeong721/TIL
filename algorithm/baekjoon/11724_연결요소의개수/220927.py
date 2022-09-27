import sys
sys.stdin = open('input.txt')

limit_number = 15000
sys.setrecursionlimit(limit_number)
from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visitied = [False for _ in range(N+1)]

def dfs(i):
    global visitied

    if not visitied[i]:
        visitied[i] = True
        for k in arr[i]:
            if not visitied[k]:
                dfs(k)

# 연결선 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
# 연결선 갯수 체크
que = deque()

for i in range(1, N+1):
    if not visitied[i]:
        dfs(i)
        cnt += 1



print(arr)
print(cnt)



