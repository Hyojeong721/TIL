import sys
sys.stdin = open('sample_input.txt')
from collections import deque

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    Q = deque()
    dist = [[987654321] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'W':
                Q.append((i,j))
                dist[i][j] = 0
    while Q:
        v = Q.popleft()
        r = v[0]
        c = v[1]
        for i in range(4):
            if 0 <= r + dr[i] < N and 0 <= c + dc[i] < M:
                if dist[r+dr[i]][c+dc[i]] > dist[r][c] + 1:
                    dist[r + dr[i]][c + dc[i]] = dist[r][c] + 1
                    Q.append((r+dr[i], c+dc[i]))

    result = sum([sum(row) for row in dist])
    print(f'#{tc} {result}')
