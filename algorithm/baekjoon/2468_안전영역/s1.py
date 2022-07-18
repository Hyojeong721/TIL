import sys
from collections import deque
sys.stdin = open('input.txt')
limit_number = 15000
sys.setrecursionlimit(limit_number)

def dfs(i, j, k):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for m in range(4):
        ni, nj = i+di[m], j+dj[m]
        if 0<=ni<N and 0<=nj<N and not sink[ni][nj] and arr[ni][nj] > k:
            sink[ni][nj] = True
            dfs(ni, nj, k)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    k, max_k = 0, 0
    for i in range(N):
        max_k = max(max(arr[i]), max_k)

    while k < max_k:
        cnt = 0
        sink = [[False] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if arr[i][j] > k and not sink[i][j]:
                    cnt += 1
                    sink[i][j]=True
                    dfs(i, j, k)
        k += 1
        ans = max(ans, cnt)


    print("#{} {}".format(tc, ans))