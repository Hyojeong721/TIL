# pass
import sys
sys.stdin = open('input.txt')

from collections import deque

def cal(n, l):
    if l == 0:
        return n + 1
    elif l == 1:
        return n - 1
    elif l == 2:
        return n * 2
    elif l == 3:
        return n - 10


def bfs(n, m):
    global tc
    Q = deque()
    Q.append((n, 0))
    visited[n] = 1
    while Q:
        num, ans = Q.popleft()
        for i in range(4):
            next_n = cal(num, i)
            if next_n == m:
                return ans + 1
            elif 0 < next_n <= 1000000 and visited[next_n] != 1:
                Q.append((next_n, ans + 1))
                visited[next_n] = 1

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    print("#{} {}".format(tc, bfs(N, M)))