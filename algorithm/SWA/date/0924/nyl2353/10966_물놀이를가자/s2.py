"""
deque가 list로 queue 직접 구현하는 것보다 빠르구나
"""

import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    visited = [[987654321] * M for _ in range(N)]

    pools = deque()
    # pools = [0] * (N * M)
    # front, rear = -1, -1


    for r in range(N):
        for c in range(M):
            if mat[r][c] == 'W':
                pools.append([r, c])
                # rear += 1
                # pools[rear] = [r, c]
                visited[r][c] = 0
    # print(pools)


    while pools:
    # while front != rear:
        r, c = pools.popleft()
        # front += 1
        # r, c = pools[front]

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if mat[nr][nc] == 'L' and visited[nr][nc] == 987654321:
                visited[nr][nc] = visited[r][c] + 1
                pools.append([nr, nc])
                # rear += 1
                # pools[rear] = [nr, nc]
    # print(visited)


    ans = 0
    for r in visited:
        for c in r:
            ans += c
    print('#{} {}'.format(tc, ans))