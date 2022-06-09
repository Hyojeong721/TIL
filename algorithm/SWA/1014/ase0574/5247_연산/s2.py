# 6/ 10

import sys
sys.stdin = open('input.txt')

def cal(n, m):
    if m == 0:
        return n+1
    elif m == 1:
        return n-1
    elif m == 2:
        return n*2
    elif m == 3:
        return n-10

def bfs(n):
    global ans, M
    q.append(n)
    q.append(0)
    visited[n] = 1

    while q:
        num = q.pop(0)
        ans = q.pop(0)

        for i in range(4):
            next_n = cal(num, i)
            if next_n == M:
                return ans + 1
            elif 0 < next_n < 1000000 and visited[next_n] != 1:
                q.append(next_n)
                q.append(ans + 1)
                visited[next_n] = 1

T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    N, M = int(N), int(M)
    q = []
    visited = [0]*1000001

    print("#{} {}".format(tc, bfs(N)))