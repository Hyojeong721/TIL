import sys
sys.stdin = open('input.txt')

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
]

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # 지도
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    Q = [(R, C)]
    visited[R][C] = 1

    ans = 0

    while Q:
        i, j = Q.pop(0)
        ans += 1

        if visited[i][j] >= L:
            continue

        for d in range(4):
            if pipe[tunnel[R][C]][d] == 0:
                continue

            next_i = i + di[d]
            next_j = j + dj[d]

            if next_i < 0 or next_i >= N or next_j < 0 or next_j >= M:
                continue

            nd = (d+2) % 4
            np = tunnel[next_i][next_j]

            if visited[next_i][next_j] or pipe[np][nd] == 0:
                continue

            visited[next_i][next_j] = visited[next_i][next_j] + 1
            Q.append((next_i, next_j))

    print('#{} {}'.format(tc, ans))

