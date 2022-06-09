"""
Y 시간초과?...
"""

import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    pools = []
    visited = [[987654321] * M for _ in range(N)]
    for r in range(N):
        temp = input()
        matrix.append(temp)
        for c, value in enumerate(temp):
            if value == 'W':
                pools.append([r, c])
                visited[r][c] = 0

    while pools:
        r, c = pools.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if matrix[nr][nc] == 'L' and visited[nr][nc] == 987654321:
                visited[nr][nc] = visited[r][c] + 1
                pools.append([nr, nc])

    ans = 0
    for r in visited:
        for c in r:
            ans += c

    print('#{} {}'.format(tc, ans))