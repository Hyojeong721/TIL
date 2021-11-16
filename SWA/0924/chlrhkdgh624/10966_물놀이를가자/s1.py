import sys
sys.stdin = open('input.txt')

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    dist = [[987654321]*M for _ in range(N)]

    Q = deque()

    # 시작점인 물 위치
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                Q.append((i, j))
                dist[i][j] = 0

    while Q:
        i, j = Q.popleft()
        for d in range(4):
            next_i = i + di[d]
            next_j = j + dj[d]

            if next_i < 0 or next_i >= N or next_j < 0 or next_j >= M:
                continue

            if arr[next_i][next_j] == 'L' and dist[next_i][next_j] == 987654321:
                dist[next_i][next_j] = dist[i][j] + 1
                Q.append((next_i, next_j))

    ans = 0

    for i in dist:
        ans += sum(i)

    print('#{} {}'.format(tc, ans))